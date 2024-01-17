# accounts/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

class UserProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'accounts/user_profile.html'
    context_object_name = 'user'
