from django.shortcuts import render

# Create your views here.
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
import re
from django.views import View


def drama_list(request):
    drama_list = Drama2.objects.all()


    ctx = {
        'drama_list': drama_list,

    }
    return render(request, 'yeonsonam/drama_list.html', ctx)


def drama_list_test(request, tag_pk=None):
    if tag_pk is not None:
        drama_list = Drama2.objects.filter(tag__pk=tag_pk)
        # get_object_or_404 사용하는게 좋음.
        try:
            tag = Tag.objects.get(pk=tag_pk)
        except Tag.DoesNotExist:
            raise Http404('없는 Tag입니다.')
    else:
        drama_list = Drama2.objects.all()
        tag = None

    ctx = {
        'drama_list': drama_list,
        'tag_list': Tag.objects.all(),
        'tag_selected': tag,
    }
    return render(request, 'yeonsonam/drama_list_test.html', ctx)




def drama_detail(request, pk):
    drama = get_object_or_404(Drama2, pk=pk)
    comment_form = CommentForm(request.POST or None)

    ctx = {
        'drama': drama,

    }

    return render(request, 'yeonsonam/drama_detail.html', ctx)






@login_required
def drama_like(request, pk):
    if request.method == "POST":
        drama = get_object_or_404(Drama, pk=pk)
        if request.user.liked_drama_set.filter(pk=pk).exists():
            drama.liker_set.remove(request.user)
        else:
            drama.liker_set.add(request.user)
        return redirect(drama.get_absolute_url())
    else:
        return HttpResponse(status=400)


def place_detail(request, pk):
    place = get_object_or_404(PlaceList, pk=pk)
    ctx = {
        'place': place,
    }
    return render(request, 'yeonsonam/place_detail.html', ctx)




class DramaRatingAjaxView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        print(user)
        drama_id = request.POST.get("drama_id")
        rating_value = request.POST.get("rating_value")
        drama_obj = Drama2.objects.get(id=drama_id)
        rating_obj, rating_obj_created = ProductRating.objects.get_or_create(
                user=user, 
                drama=drama_obj
                )
        rating_obj = ProductRating.objects.get(user=user, drama=drama_obj)
        rating_obj.rating = int(rating_value)
        rating_obj.save()
        data = {
            "success": True
        }
        return JsonResponse(data)













    