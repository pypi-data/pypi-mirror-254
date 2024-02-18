"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
from django.urls import include, path

from organizations import api, views

app_name = 'organizations'

# TODO: there should be only one patterns list based on API (with api/ prefix removed)
# Page URLs
_urlpatterns = [
    # get organization page
    path('', views.organization_people_list, name='organization-index'),
    ]

# API URLs
_api_urlpattens = [
    # organization list viewset
    path('', api.OrganizationListAPI.as_view(), name='organization-list'),
    # organization detail viewset
    path('<int:pk>', api.OrganizationAPI.as_view(), name='organization-detail'),
    # organization memberships list viewset
    path('<int:pk>/memberships', api.OrganizationMemberListAPI.as_view(), name='organization-memberships-list'),
]

# TODO: these urlpatterns should be moved in core/urls with include('organizations.urls')
urlpatterns = [
    path('organization/', views.simple_view, name='organization-simple'),
    path('organization/webhooks', views.simple_view, name='organization-simple-webhooks'),

    path('people/', include(_urlpatterns)),
    path('api/organizations/', include((_api_urlpattens, app_name), namespace='api')),

    # invite
    path('api/invite', api.OrganizationInviteAPI.as_view(), name='organization-invite'),
    path('api/invite/reset-token', api.OrganizationResetTokenAPI.as_view(), name='organization-reset-token'),
    path('api/organizations/send-invitation/', views.send_invitation, name='send-invitation'),
    path('accept-invitation/<str:token>/', views.accept_invitation, name='accept-invitation'),  # URL for accepting invitations
    path('invitation-success/', views.invitation_success, name='invitation-success'),  # URL for successful invitation acceptance
    path('api/organizations/remove-user/<int:user_id>/', views.remove_user_from_organization, name='remove-user-from-organization'),
    path('api/active-organization/', api.get_user_active_organization_id, name='get-active-organization-and-creator'),
    path('api/organizations/active-members/<int:user_id>/', api.get_active_organization_members, name='get-active-organization-members'),
    path('api/public-organizations/<int:pk>/members/', api.PublicOrganizationMemberListAPI.as_view(), name='public-organization-members'),
]
