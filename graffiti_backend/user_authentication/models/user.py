from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.db import models
from user_authentication.models.user_manager import UserManager
from user_authentication.commons import UserType
from store.models.store import Store
from store.models.address import Address

class User(AbstractBaseUser):
    #PERSONAL_USER = 'PU'
    #COMMERCIAL_USER = 'CU'
    #SUPER_USER = 'SU'
    #USER_TYPE_CHOICES = (
    #    (PERSONAL_USER, 'personal_user'),
    #    (COMMERCIAL_USER, 'commercial_user'),
    #    (SUPER_USER, 'super_user')
    #)

    email = models.EmailField(unique=True, verbose_name='email address', max_length=225, blank=False)
    username = models.CharField(unique=True, max_length=225, null=True)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    #user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default=PERSONAL_USER)
    user_type = models.CharField(max_length=225, default=UserType.PERSONAL_USER)
    #contactInfo = models.OneToOneField(ContactInfo, null = True)
    profile_image = models.ImageField(upload_to='image/profile_image', null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    friends = models.ManyToManyField("self")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    #store = models.ForeignKey('store.Store', on_delete=models.CASCADE, related_name="store", null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'username', 'password', 'user_type']

    class Meta:
        app_label = 'user_authentication'
