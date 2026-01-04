from django.db import models
from django.contrib.auth.models import AbstractUser

ENDPOINT_TYPE = (
    ('login', 'Login'),
    ('logout', 'Logout'),
    ('doleance', 'Doleance'),
    ('doleances', 'Doleances'),
)

ENDPOINT_METHOD = (
    ('get', 'Get'),
    ('post', 'Post'),
    ('put', 'Put'),
    ('delete', 'Delete'),
)

ENDPOINT_STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
)

ENDPOINT_AUTH = (
    ('basic', 'Basic'),
    ('bearer', 'Bearer'),
)

ENDPOINT_RESPONSE = (
    ('json', 'Json'),
    ('xml', 'Xml'),
    ('html', 'Html'),
    ('text', 'Text'),
)
# Create your models here.
class Organisation(models.Model):
    name_fr = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    acronym = models.SlugField(max_length=10, unique=True)
    description = models.TextField(null=True, blank=True)
    base_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_fr

    class Meta:
        verbose_name = "Organisation"
        verbose_name_plural = "Organisations"


class Endpoints(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=ENDPOINT_TYPE)
    method = models.CharField(max_length=255, choices=ENDPOINT_METHOD)
    status = models.CharField(max_length=255, choices=ENDPOINT_STATUS)
    headers = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    query_params = models.TextField(null=True, blank=True)
    auth = models.CharField(max_length=255, choices=ENDPOINT_AUTH, null=True, blank=True)
    response = models.CharField(max_length=255, choices=ENDPOINT_RESPONSE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.endpoint

    class Meta:
        verbose_name = "Endpoint"
        verbose_name_plural = "Endpoints"

class User(AbstractUser):
    organisation = models.OneToOneField('Organisation', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username