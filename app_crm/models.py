from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from shortuuid.django_fields import ShortUUIDField
from django.core.validators import FileExtensionValidator

# Custom User Model
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)  # Should be unique for AbstractUser
    user_type_choices = (
        ('admin', 'admin'),
        ('super admin', 'super admin'),
        ('sales agent', 'sales agent'),
        ('collection agent', 'collection agent'),
    )
    user_type = models.CharField(max_length=255, choices=user_type_choices, default='collection agent', blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Required when creating user via createsuperuser

    def __str__(self):
        return self.first_name or self.email

    def save(self, *args, **kwargs):
        if self.email:
            user_name, _ = self.email.split('@', 1)
            if not self.first_name:
                self.first_name = user_name
            if not self.username:
                self.username = user_name
        super(User, self).save(*args, **kwargs)


# Related model
class FME_Model(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Phone number validator
phone_no_validator = RegexValidator(
    regex=r'^\d{10}$',
    message='Please enter a valid 10 digit mobile number',

)
def nameFile(instance,filename):
    return '/'.join(['images',str(instance.sp_business_name),filename])

# Sale Punch Model
class SalePunchModel(models.Model):


    # sp_fme = models.ForeignKey(FME_Model, on_delete=models.CASCADE, blank=True, null=True)
    sp_fme = models.ForeignKey(FME_Model, on_delete=models.CASCADE, blank=True, null=True)
    sp_fme = models.CharField(max_length=255, blank=True, null=True)
    sp_business_name = models.CharField(max_length=255, blank=True, null=True)
    sp_contact_no = models.CharField(max_length=10, null=True, blank=True, validators=[phone_no_validator])
    sp_email = models.EmailField(unique=True)
    sp_whatsapp_no = models.CharField(max_length=10, null=True, blank=True, validators=[phone_no_validator])
    sp_insta_link = models.URLField(unique=True, null=True, blank=True)
    sp_fb_link = models.URLField(unique=True, null=True, blank=True)
    sp_google_review_link = models.URLField(unique=True, null=True, blank=True)
    sp_gmap_link = models.URLField(unique=True, null=True, blank=True)
    sp_discount_details = models.CharField(max_length=255, null=True, blank=True)
    sp_custom_review_filter_choices = (
        ("Yes","Yes"),
        ("No","No")
    )
    sp_custom_review_filter = models.CharField(max_length=255, null=True, blank=True,choices=sp_custom_review_filter_choices,default="Yes")  
    sp_additional_products = models.CharField(max_length=255, blank=True, null=True)
    # sp_logo = models.FileField(upload_to="logo/", blank=True, null=True,validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg','png'])])
    sp_logo = models.ImageField(upload_to=nameFile, max_length=500,blank=True, null=True)

    status_choices = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )
    
    sp_status = models.CharField(max_length=255, choices=status_choices, default='active', blank=True, null=True)
    sp_web_link = models.URLField(unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.sp_email)
