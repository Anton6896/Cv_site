from rest_framework import generics, permissions
from . import serializers
from . import my_permissions
from . import models

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import forms


# regular html view     ====================================================================
class HomeView(generic.View):
    def get(self, *args, **kwarg):
        return render(self.request, 'index.html')


class MyRegisterView(generic.CreateView):
    form_class = forms.UserRegisterForm_my
    template_name = "register.html"
    success_url = reverse_lazy("accounts:login")


class UpdateProfileView(generic.UpdateView):
    # todo user profile update / change form
    pass


#  api views            ====================================================================

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
