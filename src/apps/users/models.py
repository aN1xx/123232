import phonenumber_field.modelfields
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models


class UserQueryset(models.QuerySet):
    ...


class UserManager(auth_models.BaseUserManager.from_queryset(UserQueryset)):
    def _create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('Phone cannot be empty')
        user = self.model(phone=phone, **extra_fields)
        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)

    def create_user(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)


class User(
    auth_models.PermissionsMixin,
    auth_models.AbstractBaseUser,
):
    phone = phonenumber_field.modelfields.PhoneNumberField(
        'Mobile phone', unique=True,
    )
    iin = models.CharField(max_length=12, validators=[MinLengthValidator(12)])

    is_staff = models.BooleanField('Is staff', default=False)
    is_active = models.BooleanField('Is active', default=True)

    avatar = models.ImageField(null=True, blank=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
