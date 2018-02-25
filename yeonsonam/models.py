from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse





class Drama2(models.Model):
    place = models.TextField(blank=True, null=True)  # This field type is a guess.
    perf_kind = models.TextField(blank=True, null=True)  # This field type is a guess.
    perf_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    openrun = models.TextField(blank=True, null=True)  # This field type is a guess.
    poster = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.CharField(blank=True, null=True,  max_length=150)  # This field type is a guess.
    end_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    perf_state = models.TextField(blank=True, null=True)  # This field type is a guess.
    detail_url = models.TextField(blank=True, null=True)  # This field type is a guess.
    age = models.TextField(blank=True, null=True)  # This field type is a guess.
    casts = models.TextField(blank=True, null=True)  # This field type is a guess.
    crews = models.TextField(blank=True, null=True)  # This field type is a guess.
    theater_company = models.TextField(blank=True, null=True)  # This field type is a guess.


    class Meta:
        managed = True
        db_table = 'Drama2'

    def get_absolute_url(self):
        return reverse('yeonsonam:drama_detail', kwargs={
            'pk': self.pk,
        })

    def __str__(self):
        return self.title




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

class PlaceList(models.Model):
    field1 = models.TextField(blank=True, null=True)
    field2 = models.TextField(blank=True, null=True)
    field3 = models.TextField(blank=True, null=True)
    field4 = models.TextField(blank=True, null=True)
    field5 = models.TextField(blank=True, null=True)
    field6 = models.TextField(blank=True, null=True)
    field7 = models.TextField(blank=True, null=True)
    field8 = models.TextField(blank=True, null=True)
    field9 = models.TextField(blank=True, null=True)
    field11 = models.TextField(blank=True, null=True)
    field12 = models.TextField(blank=True, null=True)
    field13 = models.TextField(blank=True, null=True)
    field14 = models.TextField(blank=True, null=True)
    field15 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_list'



class Drama222(models.Model):
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
    field15 = models.IntegerField(blank=True, null=True)
    field16 = models.TextField(blank=True, null=True)
    field18 = models.TextField(blank=True, null=True)
    field19 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Drama222'
