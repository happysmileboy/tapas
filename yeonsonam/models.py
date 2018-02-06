from django.db import models
from django.conf import settings
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


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


class Drama2(models.Model):
    place = models.CharField(max_length=150, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. This field type is a guess.
    genre = models.CharField(max_length=150,blank=True, null=True)  # This field type is a guess.
    key = models.CharField(max_length=150,blank=True, null=True)  # This field type is a guess.
    openrun = models.CharField(max_length=150,blank=True, null=True)  # This field type is a guess.
    poster = models.CharField(max_length=300,blank=True, null=True)  # This field type is a guess.
    title = models.CharField(max_length=150,blank=True, null=True)  # This field type is a guess.
    start = models.CharField(max_length=150,blank=True, null=True)  # This field type is a guess.
    end = models.CharField(max_length=150,blank=True, null=True)  # This field type is a guess.
    state = models.CharField(max_length=150,blank=True, null=True)  # This field type is a guess.
    detail_url = models.CharField(max_length=300,blank=True, null=True) 
    place_id = models.CharField(max_length=300,blank=True, null=True) 
    cast = models.CharField(max_length=300,blank=True, null=True) 
    crew = models.CharField(max_length=300,blank=True, null=True) 
    runtime = models.CharField(max_length=300,blank=True, null=True) 
    age = models.CharField(max_length=300,blank=True, null=True) 
    enterprise = models.CharField(max_length=300,blank=True, null=True) 
    price = models.CharField(max_length=300,blank=True, null=True) 
    summary = models.TextField(blank=True, null=True) 
    styurl = models.TextField(blank=True, null=True) 
    time = models.CharField(max_length=300,blank=True, null=True) 
    liker_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_drama2_set',
    )

    class Meta:
        managed = True
        db_table = 'Drama2'
















