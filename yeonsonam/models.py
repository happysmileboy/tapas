from django.db import models
from django.conf import settings
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name




class Drama(models.Model):
    title = models.CharField(max_length=30, verbose_name='제목')
    place = models.CharField(max_length=150)
    open_Date = models.DateField()
    end_Date = models.DateField(blank=True)
    running_time = models.IntegerField()
    sequence = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    content = models.TextField()
    price = models.IntegerField()
    Actor = models.CharField(max_length=150)
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


























