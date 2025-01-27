from django.db import models
from .functions import media_upload_location

class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='Author', on_delete=models.CASCADE, blank=False, null=False)
    media = models.FileField(verbose_name='Insert an Image or Video', upload_to=media_upload_location, blank=True, null=True)
    title = models.CharField(verbose_name='Title', max_length=150, blank=False, null=False)
    text_field = models.TextField(verbose_name='Text Field', blank=False, null=False)
    published_date = models.DateTimeField(verbose_name='Published Date', auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} | {self.author}"