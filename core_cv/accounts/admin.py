from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserRegisterForm_my


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm_my
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
