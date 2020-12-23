from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.serializers import Serializer
from . import forms
from rest_framework import generics, permissions
from . import serializers
from . import my_permissions
from . import models


# class SignUpView(CreateView):
#     form_class = forms.MyUser
#     success_url = reverse_lazy('login')
#     template_name = 'registration/register.html'


#  api views

class CommitteeUserCreationView(generics.CreateAPIView):
    #! post_save add it to the group -> 'committee_group' for granting permissions # 
    serializer_class = serializers.CommitteeSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(role='committee')


class TenantUserCreationView(generics.CreateAPIView):
    serializer_class = serializers.TenantSerializer
    # must have this for user identity search
    queryset = models.CustomUser.objects.all()

    permission_classes = [
        permissions.IsAuthenticated, my_permissions.IsCommittee
    ]

    def perform_create(self, serializer):
        serializer.save(role='tenant')


class TenantsListView(generics.ListAPIView):
    serializer_class = serializers.ListTenantsSerializer
    queryset = models.CustomUser.objects.filter(role='tenant').all()

    permission_classes = [
        permissions.IsAuthenticated, my_permissions.IsCommittee
    ]


class TenantDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ListTenantsSerializer
    queryset = models.CustomUser.objects.filter(role='tenant').all()
    permission_classes = [
        permissions.IsAuthenticated, my_permissions.UpdateTenant
    ]
