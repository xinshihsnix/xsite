# coding: utf-8
from Crypto.Cipher import AES

from django.contrib.auth.models import AbstractBaseUser, User, PermissionsMixin, BaseUserManager
from django.db import models
from ..common.models import BaseModel
from django.utils import timezone
from django.conf import settings


class Eye(BaseModel):
    """  """
    img = models.ImageField(upload_to=settings.MONKEY_EYE_IMG_STORE_PATH, verbose_name='图片', default='', null=True, blank=True)

    class Meta:
        app_label = 'monkey'
        db_table = 'monkey_eye'