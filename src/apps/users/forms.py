from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate_unique(self) -> None:
        return

    def save(self, commit=True):
        return User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password'],
        )

    def save_m2m(self):
        return


class UserChangeForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = ReadOnlyPasswordHashField()
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=False,
    )
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput,
                                required=False,
                                )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password1',
            'password2',
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial['password']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password1 and not password2:
            return None
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        if self.cleaned_data['password2']:
            user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
