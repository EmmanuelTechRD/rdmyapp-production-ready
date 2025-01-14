from django.contrib import admin
from blog import models as blog_models

# Register your models here.
admin.site.register(blog_models.Post)