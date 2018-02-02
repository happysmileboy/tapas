from django.db import models
from django.conf import settings
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Genre(models.Model):
    kind_of_genre = models.CharField(max_length=10, verbose_name="장르")

    def __str__(self):
        return self.kind_of_genre


class Discount(models.Model):
    rate_of_discount = models.IntegerField(default=0, verbose_name='할인율', blank=True)
    name_of_discount = models.CharField(max_length=20, verbose_name='할인명', blank=True)
    discounted_price = models.IntegerField(blank=True)


class Site_reservation(models.Model):
    site_name = models.CharField(max_length=20)
    site_url = models.URLField(max_length=200,)
    site_location = models.ImageField(blank=True)

    def __str__(self):
        return self.site_name


class Price(models.Model):
    site = models.ForeignKey(Site_reservation, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='가격')
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    def discounted_price(self):
        return self.price*(100-self.rate_of_discount)/100


class Seat_photo(models.Model):
    main_seat_photo = models.ImageField()
    sub_seat_photo = models.ImageField()


class Actor(models.Model):
    name = models.CharField(max_length=10, verbose_name='배우이름')
    actor_photo = models.ImageField(null=True)

class Place(models.Model):
    place =models.CharField(max_length=20)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        full_path = [self.place]

        k = self.parent

        while k is not None:
            full_path.append(k.place)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Sequence(models.Model):
    sequence_num = models.CharField(max_length=10, verbose_name='회차') #월요일=1 화요일=2~일요일3
    sequence_time = models.TimeField()

    ordering =['sequence_num']

    def __str__(self):
        a = self.sequence_num
        b = str(self.sequence_time)
        return a+b


class Drama(models.Model):
    title = models.CharField(max_length=30, verbose_name='제목')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    open_Date = models.DateField()
    end_Date = models.DateField(blank=True)
    running_time = models.IntegerField()
    sequence = models.ManyToManyField(Sequence)
    genre = models.ManyToManyField(Genre)
    content = models.TextField()
    price = models.ManyToManyField(Price)
    seat_photo = models.ForeignKey(Seat_photo, on_delete=models.CASCADE)
    Actor = models.ManyToManyField(Actor)
    liker_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_article_set',
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


























