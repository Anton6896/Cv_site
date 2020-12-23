from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import MyUser
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = MyUser
    model = CustomUser
    list_display = ['email', 'username', 'role']

    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'role',
                    'image',
                    'building_community_name',
                    'full_address',
                    'is_voted',
                    'apartment',
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
