from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator,MinValueValidator,MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from shortuuid.django_fields import ShortUUIDField

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255)
    user_type_choices = (
        ('admin','admin'),
        ('super admin','super admin'),
        ('sales agent','sales agent'),
        ('collection agent','collection agent'),
        ('customer','customer'),
    )
    user_type = models.CharField(max_length=255,choices=user_type_choices,default='customer',blank=True,null=True)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(unique=True,blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.first_name)
    
    def save(self,*args,**kwargs):
        if self.email:
            user_name,mob_name = self.email.split('@')
            if self.first_name == '' or self.first_name == None:
                self.first_name = user_name
            if self.username == '' or self.username == None:
                self.username = user_name
        super(User,self).save(*args,**kwargs)
    

class FME_Model(models.Model):
    name = models.CharField(max_length=255)

class SalePunchModels(models.Model):
    
    phone_no_validator = RegexValidator(
        regex=r'^\d{10}$',
        message='Please enter a valid 10 digit mobile number',
    )
    
    sp_fme = models.ForeignKey(FME_Model,on_delete=models.CASCADE,blank=True,null=True)
    sp_business_name = models.CharField(max_length=255,blank=True,null=True)
    sp_contact_no = models.CharField(max_length=10,validators=[phone_no_validator])
    sp_contact_no = models.CharField(max_length=10,null=True,blank=True,validators=[phone_no_validator])
    sp_email = models.EmailField(unique=True)
    sp_whatsapp_no = models.CharField(max_length=10,null=True,blank=True,validators=[phone_no_validator])
    sp_insta_link = models.URLField(unique=True,null=True,blank=True)
    sp_fb_link = models.URLField(unique=True,null=True,blank=True)
    sp_google_review_link = models.URLField(unique=True,null=True,blank=True)
    sp_gmap_link = models.URLField(unique=True,null=True,blank=True)
    sp_discount_details = models.CharField(max_length=255,null=True,blank=True)
    sp_custom_review_filter = models.BooleanField(default=True)
    sp_additional_products = models.CharField(max_length=255,blank=True,null=True)
    sp_logo = models.FileField(upload_to="logo/")