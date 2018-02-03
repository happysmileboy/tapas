from django.db import models
from django.conf import settings
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Kopis1(models.Model):
    field1 = models.CharField(max_length=150,blank=True, null=True)
    field2 = models.CharField(max_length=150,blank=True, null=True)
    field3 = models.CharField(max_length=150,blank=True, null=True)
    field4 = models.CharField(max_length=150,blank=True, null=True)
    field5 = models.CharField(max_length=150,blank=True, null=True)
    field6 = models.CharField(max_length=150,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kopis1'

class Drama(models.Model):
    title = models.CharField(max_length=30, verbose_name='제목')
    place = models.CharField(max_length=150,blank=True, null=True)
    open_Date = models.DateField(blank=True, null=True)
    end_Date = models.DateField(blank=True, null=True)
    running_time = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=150,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    Actor = models.CharField(max_length=150,blank=True, null=True)
    liker_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_drama_set',
    )
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    drama = models.ForeignKey(
        Drama,
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

class Drama22(models.Model):
    field1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    field2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    field3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    field4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    field5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    field6 = models.TextField(blank=True, null=True)  # This field type is a guess.
    field7 = models.TextField(blank=True, null=True)  # This field type is a guess.
    field8 = models.TextField(blank=True, null=True)  # This field type is a guess.
    field9 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'drama22'

    def __str__(self):
        return self.field2






















