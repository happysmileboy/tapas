from django.db import models
from django.conf import settings
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nickname = models.CharField(max_length=20, verbose_name='닉네임')
    image = models.ImageField(
        upload_to='profile/%Y/%m/%d/',
        blank=True,
        null=True,
    )
    birth_day = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    phone_number = models.IntegerField(blank=True)

    def image_url(self):
        if self.image:
            image_url = self.image.url
        else:
            image_url = '/static/img/default_profile_image.jpg'
        return image_url


    def __str__(self):
        return self.nickname