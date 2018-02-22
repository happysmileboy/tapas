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
    place = models.TextField(blank=True, null=True)  # This field type is a guess.
    perf_kind = models.TextField(blank=True, null=True)  # This field type is a guess.
    perf_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    openrun = models.TextField(blank=True, null=True)  # This field type is a guess.
    poster = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    perf_state = models.TextField(blank=True, null=True)  # This field type is a guess.
    detail_url = models.TextField(blank=True, null=True)  # This field type is a guess.
    age = models.TextField(blank=True, null=True)  # This field type is a guess.
    casts = models.TextField(blank=True, null=True)  # This field type is a guess.
    crews = models.TextField(blank=True, null=True)  # This field type is a guess.
    theater_company = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Drama2'
# Unable to inspect table 'Drama2_liker_set'
# The error was: list index out of range
# Unable to inspect table 'Drama2_tag2'
# The error was: list index out of range




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


