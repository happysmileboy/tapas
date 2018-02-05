from django.shortcuts import render

# Create your views here.

def profile_detail(request):
    return render(request, 'profile_detail.html')