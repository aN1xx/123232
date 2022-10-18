from django.contrib.auth import models as auth_models
from django.db import models


class UserQueryset(models.QuerySet):
    ...


class UserManager(auth_models.BaseUserManager.from_queryset(UserQueryset)):
    def _create_user(self, username, password):
        if not username:
            raise ValueError('Username cannot be empty')
        user = self.model(username=username)
        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)


class User(
    auth_models.PermissionsMixin,
    auth_models.AbstractBaseUser,
):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
