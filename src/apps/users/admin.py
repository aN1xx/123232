from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.users.forms import UserChangeForm
from apps.users.forms import UserCreationForm


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    # list_display = ['phone', 'iin', 'is_superuser']
    search_fields = ['phone']
    ordering = ['phone']

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)
