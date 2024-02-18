"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.urls import reverse
from organizations.models import OrganizationInvitation
from users.models import User
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
import json
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


@login_required
def organization_people_list(request):
    organization = request.user.organization
    return render(request, 'organizations/people_list.html', {'organization': organization})

@login_required
def simple_view(request):
    return render(request, 'organizations/people_list.html')


# @login_required
# # @ratelimit(key='user', rate='10/h', block=True)  # Rate limit to 5 invitations per hour
# def send_invitation(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')

#         # Check if user exists
#         if not User.objects.filter(email=email).exists():
#             # Redirect to signup page of users application
#             signup_url = reverse('user-signup') + f"?email={email}"
#             return redirect(signup_url)

#         # Create invitation and send email
#         token = get_random_string()
#         OrganizationInvitation.objects.create(email=email, organization=request.user.active_organization, token=token)
#         send_invitation_email(request, email, token)
#         messages.success(request, "Invitation sent successfully.")
#         return redirect('organization-people-list')

#     return render(request, 'organizations/send_invitation.html')

# @login_required
# def send_invitation(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         email = data.get('email')

#         try:
#             validate_email(email)
#         except ValidationError:
#             return JsonResponse({'status': 'error', 'message': 'Invalid email address'}, status=400)

#         # Check if user exists, if not, create a pending invitation
#         user_exists = User.objects.filter(email=email).exists()
#         token = get_random_string()

#         if not user_exists:
#             # Logic to handle non-existing user
#             # Save the token with the email and a flag indicating the user is not yet registered
#             # This token should be used later in the signup process
#             return json.dumps({'status': 'failed', 'message': 'User does not exist'})
#         else:
#             # Existing user logic
#             OrganizationInvitation.objects.create(email=email, organization=request.user.active_organization, token=token)
        
#         send_invitation_email(request, email, token, user_exists)

#         return JsonResponse({'status': 'success', 'message': 'Invitation sent successfully'})

#     return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

# def send_invitation_email(request, email, token, user_exists):
#     if user_exists:
#         invitation_url = request.build_absolute_uri(reverse('organizations:accept-invitation', args=[token]))
#     else:
#         # URL for non-registered users, possibly to a signup page with the token as a parameter
#         invitation_url = request.build_absolute_uri(reverse('user-signup') + '?token=' + token)
#     subject = 'Invitation to Join Organization'
#     message = f'Please click on the link to join the organization: {invitation_url}'
#     send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

# @login_required
# def send_invitation(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         email = data.get('email')
#         organization = request.user.active_organization

#         try:
#             invited_user = User.objects.get(email=email)
#             # If user exists, add them to the organization
#             organization.users.add(invited_user)
#             return JsonResponse({'status': 'success', 'message': 'User added to the organization'})
#         except User.DoesNotExist:
#             # If user does not exist, send an invitation email
#             token = get_random_string()
#             OrganizationInvitation.objects.create(email=email, organization=organization, token=token)
#             send_invitation_email(request, email, token)
#             return JsonResponse({'status': 'success', 'message': 'Invitation email sent'})

#     return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

# def send_invitation_email(request, email, token):
#     invitation_url = request.build_absolute_uri(reverse('accept-invitation', args=[token]))
#     subject = 'Invitation to Join Our Organization'
#     message = f'Please click on the link to join our organization: {invitation_url}'
#     send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])


@login_required
def invitation_success(request):
    return render(request, 'invitation_success.html')

@login_required
def send_invitation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        organization = request.user.active_organization

        try:
            # Check if user with the provided email already exists
            invited_user = User.objects.get(email=email)
            if organization.users.filter(email=email).exists():
                # User is already a member of the organization
                return JsonResponse({'status': 'info', 'message': 'User is already a member of the organization'})
            else:
                # Add user to the organization and to the added_to_organizations field
                organization.users.add(invited_user)
                invited_user.added_to_organizations.add(organization)
                invited_user.save()
                send_added_to_organization_email(request, email, organization.title)
                return JsonResponse({'status': 'success', 'message': 'User added to the organization'})
        except User.DoesNotExist:
            # User does not exist, create a new invitation
            token = get_random_string()
            OrganizationInvitation.objects.create(email=email, organization=organization, token=token)
            send_invitation_email(request, email, token)
            return JsonResponse({'status': 'success', 'message': 'Invitation email sent'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def send_invitation_email(request, email, token):
    invitation_url = request.build_absolute_uri(reverse('accept-invitation', args=[token]))
    subject = 'Invitation to Join Our Organization'
    message = f'Please click on the link to join our organization: {invitation_url}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

def send_added_to_organization_email(request, email, organization_name):
    subject = 'You have been added to an organization'
    message = f'You have been added to the organization: {organization_name}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

@login_required
def accept_invitation(request, token):
    invitation = get_object_or_404(OrganizationInvitation, token=token)
    if invitation.is_valid() and invitation.email == request.user.email:
        # Add user to the organization
        invitation.organization.users.add(request.user)
        invitation.status = 'accepted'
        invitation.save()
        messages.success(request, "You have joined the organization successfully.")
        return redirect('organizations:organization-index')
    else:
        messages.error(request, "Invalid or expired invitation.")
        return redirect('organizations:organization-index')

@login_required
def remove_user_from_organization(request, user_id):
    organization = request.user.active_organization
    
    if request.user != organization.created_by:
        return JsonResponse({'status': 'error', 'message': 'Only the organization creator can remove users.'}, status=403)
    
    if user_id == request.user.id:
        return JsonResponse({'status': 'error', 'message': 'You cannot remove yourself.'}, status=403)

    try:
        user_to_remove = User.objects.get(pk=user_id)
        if user_to_remove in organization.users.all():
            organization.users.remove(user_to_remove)
            return JsonResponse({'status': 'success', 'message': 'User successfully removed from the organization'})
        else:
            return JsonResponse({'status': 'error', 'message': 'User not found in the organization'}, status=404)

    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)