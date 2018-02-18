from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Tag2(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Drama2(models.Model):
    field1 = models.TextField(blank=True, null=True)
    field2 = models.TextField(blank=True, null=True)
    field3 = models.TextField(blank=True, null=True)
    field4 = models.TextField(blank=True, null=True)
    field5 = models.TextField(blank=True, null=True)
    field6 = models.TextField(blank=True, null=True)
    field7 = models.TextField(blank=True, null=True)
    field8 = models.TextField(blank=True, null=True)
    field9 = models.TextField(blank=True, null=True)
    field10 = models.TextField(blank=True, null=True)
    field11 = models.TextField(blank=True, null=True)
    field12 = models.TextField(blank=True, null=True)
    field13 = models.TextField(blank=True, null=True)
    field14 = models.TextField(blank=True, null=True)
    field15 = models.TextField(blank=True, null=True)
    tag2 = models.ManyToManyField(Tag2)

    class Meta:
        managed = False
        db_table = 'drama2'



class Comment(models.Model):
    drama = models.ForeignKey(
        Drama2,
        on_delete=models.CASCADE,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('yeonsonam:drama_detail', kwargs={
            'pk': self.pk,
        })


