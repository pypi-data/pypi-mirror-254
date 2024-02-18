"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
import logging
from django.urls import reverse
from django.conf import settings
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view,permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from data_studio.core.permissions import all_permissions, ViewClassPermission
from data_studio.core.utils.params import bool_from_request

from organizations.models import Organization
from organizations.serializers import (
    OrganizationSerializer, OrganizationIdSerializer, OrganizationMemberUserSerializer, OrganizationInviteSerializer,
    OrganizationsParamsSerializer
)
from core.feature_flags import flag_set

logger = logging.getLogger(__name__)


@method_decorator(name='get', decorator=swagger_auto_schema(
        tags=['Organizations'],
        operation_summary='List your organizations',
        operation_description="""
        Return a list of the organizations you've created or that you have access to.
        """
    ))
class OrganizationListAPI(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    permission_required = ViewClassPermission(
        GET=all_permissions.organizations_view,
        PUT=all_permissions.organizations_change,
        POST=all_permissions.organizations_create,
        PATCH=all_permissions.organizations_change,
        DELETE=all_permissions.organizations_change,
    )
    serializer_class = OrganizationIdSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(users=self.request.user).distinct()

    def get(self, request, *args, **kwargs):
        return super(OrganizationListAPI, self).get(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def post(self, request, *args, **kwargs):
        return super(OrganizationListAPI, self).post(request, *args, **kwargs)


class OrganizationMemberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'

    def get_page_size(self, request):
        # emulate "unlimited" page_size
        if self.page_size_query_param in request.query_params and request.query_params[self.page_size_query_param] == '-1':
            return 1000000
        return super().get_page_size(request)


@method_decorator(name='get', decorator=swagger_auto_schema(
        tags=['Organizations'],
        operation_summary='Get organization members list',
        operation_description='Retrieve a list of the organization members and their IDs.',
        manual_parameters=[
            openapi.Parameter(
                name='id',
                type=openapi.TYPE_INTEGER,
                in_=openapi.IN_PATH,
                description='A unique integer value identifying this organization.'),
        ],
    ))
class OrganizationMemberListAPI(generics.ListAPIView):

    parser_classes = (JSONParser, FormParser, MultiPartParser)
    permission_required = ViewClassPermission(
        GET=all_permissions.organizations_view,
        PUT=all_permissions.organizations_change,
        PATCH=all_permissions.organizations_change,
        DELETE=all_permissions.organizations_change,
    )
    serializer_class = OrganizationMemberUserSerializer
    pagination_class = OrganizationMemberPagination

    def get_serializer_context(self):
        return {
            'contributed_to_projects': bool_from_request(self.request.GET, 'contributed_to_projects', False),
            'request': self.request
        }

    def get_queryset(self):
        # Get the requested organization based on the ID in the URL
        org = generics.get_object_or_404(self.request.user.organizations, pk=self.kwargs[self.lookup_field])

        # Check if the requesting user is the only member and the owner
        if org.members.count() == 1 and org.created_by == self.request.user:
            # Return a queryset containing only the user
            return org.members.filter(id=self.request.user.id)

        # Else, return the regular member list
        if flag_set('fix_backend_dev_3134_exclude_deactivated_users', self.request.user):
            serializer = OrganizationsParamsSerializer(data=self.request.GET)
            serializer.is_valid(raise_exception=True)
            active = serializer.validated_data.get('active')
            
            # return only active users (exclude DISABLED and NOT_ACTIVATED)
            if active:
                return org.active_members.order_by('user__username')
            
            return org.members.order_by('user__username')
        else:
            return org.members.order_by('user__username')


@method_decorator(name='get', decorator=swagger_auto_schema(
        tags=['Organizations'],
        operation_summary=' Get organization settings',
        operation_description='Retrieve the settings for a specific organization by ID.'
    ))
@method_decorator(name='patch', decorator=swagger_auto_schema(
        tags=['Organizations'],
        operation_summary='Update organization settings',
        operation_description='Update the settings for a specific organization by ID.'
    ))
class OrganizationAPI(generics.RetrieveUpdateAPIView):

    parser_classes = (JSONParser, FormParser, MultiPartParser)
    queryset = Organization.objects.all()
    permission_required = all_permissions.organizations_change
    serializer_class = OrganizationSerializer

    redirect_route = 'organizations-dashboard'
    redirect_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return super(OrganizationAPI, self).get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super(OrganizationAPI, self).patch(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        return super(OrganizationAPI, self).put(request, *args, **kwargs)


@method_decorator(name='get', decorator=swagger_auto_schema(
        tags=["Invites"],
        operation_summary='Get organization invite link',
        operation_description='Get a link to use to invite a new member to an organization in Data Studio Enterprise.',
        responses={200: OrganizationInviteSerializer()}
    ))
class OrganizationInviteAPI(generics.RetrieveAPIView):
    parser_classes = (JSONParser,)
    queryset = Organization.objects.all()
    permission_required = all_permissions.organizations_change

    def get(self, request, *args, **kwargs):
        org = request.user.active_organization
        invite_url = '{}?token={}'.format(reverse('user-signup'), org.token)
        if hasattr(settings, 'FORCE_SCRIPT_NAME') and settings.FORCE_SCRIPT_NAME:
            invite_url = invite_url.replace(settings.FORCE_SCRIPT_NAME, '', 1)
        serializer = OrganizationInviteSerializer(data={'invite_url': invite_url, 'token': org.token})
        serializer.is_valid()
        return Response(serializer.data, status=200)


@method_decorator(name='post', decorator=swagger_auto_schema(
        tags=["Invites"],
        operation_summary='Reset organization token',
        operation_description='Reset the token used in the invitation link to invite someone to an organization.',
        responses={200: OrganizationInviteSerializer()}
    ))
class OrganizationResetTokenAPI(APIView):
    permission_required = all_permissions.organizations_invite
    parser_classes = (JSONParser,)

    def post(self, request, *args, **kwargs):
        org = request.user.active_organization
        org.reset_token()
        logger.debug(f'New token for organization {org.pk} is {org.token}')
        invite_url = '{}?token={}'.format(reverse('user-signup'), org.token)
        serializer = OrganizationInviteSerializer(data={'invite_url': invite_url, 'token': org.token})
        serializer.is_valid()
        return Response(serializer.data, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_organization_creator(request, organization_id):
    try:
        organization = Organization.objects.get(pk=organization_id)
        creator_id = organization.created_by.id if organization.created_by else None
        return JsonResponse({'creator_id': creator_id})
    except Organization.DoesNotExist:
        return JsonResponse({'error': 'Organization not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_active_organization_id(request):
    """
    Get the active organization ID and creator ID of the current user.
    """
    user = request.user
    if hasattr(user, 'active_organization') and user.active_organization:
        organization = user.active_organization
        organization_id = organization.id
        creator_id = organization.created_by.id if organization.created_by else None
        return Response({
            'organization_id': organization_id,
            'creator_id': creator_id
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Active organization not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_active_organization_members(request, user_id):
    # Only allow authenticated users to access this endpoint
    if not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    # Get the user; if not found, return 404
    target_user = get_object_or_404(User, pk=user_id)

    # Check if the requested user has an active organization
    active_organization = target_user.active_organization
    if not active_organization:
        return Response({'error': 'Active organization not found for the given user'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the requesting user has permission to view the organization members
    if not active_organization.has_user(request.user) and not request.user.is_superuser:
        return Response({'error': 'You do not have permission to view this information'}, status=status.HTTP_403_FORBIDDEN)

    # Serialize and return the active organization members
    serializer = OrganizationMemberUserSerializer(active_organization.members, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class PublicOrganizationMemberListAPI(generics.ListAPIView):
    permission_classes = [AllowAny]
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    serializer_class = OrganizationMemberUserSerializer
    pagination_class = OrganizationMemberPagination

    def get_serializer_context(self):
        return {
            'contributed_to_projects': bool_from_request(self.request.GET, 'contributed_to_projects', False),
            'request': self.request
        }

    def get_queryset(self):
        # Get the requested organization based on the ID in the URL
        org = generics.get_object_or_404(Organization, pk=self.kwargs['pk'])  # Replace 'pk' with your lookup field

        # Return the regular member list
        if flag_set('fix_backend_dev_3134_exclude_deactivated_users', self.request.user):
            serializer = OrganizationsParamsSerializer(data=self.request.GET)
            serializer.is_valid(raise_exception=True)
            active = serializer.validated_data.get('active')
            
            # Return only active users (exclude DISABLED and NOT_ACTIVATED) if requested
            if active:
                return org.active_members.order_by('user__username')
            
            return org.members.order_by('user__username')
        else:
            return org.members.order_by('user__username')