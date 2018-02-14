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

def drama_list(request, tag_pk=None):
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
    url = drama.styurl
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+jpg', url)

    ctx = {
        'drama': drama,
        'comment_form': comment_form,
        'did_like_article': drama.liker_set.filter(pk=request.user.pk),
        'urls':urls,
        'len':len(drama.summary)
    }
    if request.method == "POST" and comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.article = article
        new_comment.author = request.user
        new_comment.save()
        return redirect(article.get_absolute_url())

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
