from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin

# Create your models here.

class UserProfileManager(BaseUserManager):
    #manager for user profiles

    def create_user(self, email, name, password=None):
        #create a new user profile
        if not email:
            raise ValueError('Email address must not be empty')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        # Create and save new super user with given details
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True,)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        #this appears alongside the username in an object’s history in admin
        return self.name

    def get_short_name(self):
        #this replaces the username in the greeting to the user in the header of admin
        return self.name

    def __str__(self):
        #returning the string representation of our user
        return self.email