import uuid
import os
from djongo import models
from main.models import Site
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class Category(models.Model):
    """Categories of products"""
    category_name = models.CharField(max_length=255)

class Variant(models.Model):
    """Variants for products"""
    variant_name = models.CharField(max_length=255)
    variant_type = models.CharField(max_length=255)

class Product(models.Model):
    """Product details"""
    name = models.CharField(max_length=255)
    categories = models.ArrayModelField(
        model_container=Category
    )
    description = models.TextField()
    price = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    variants = models.ArrayModelField(
        model_container=Variant
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE
    )
