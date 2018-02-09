from django.urls import path

from . import views


app_name = 'yeonsonam'

urlpatterns = [
    path('tag/<int:tag_pk>', views.drama_list, name='drama_list_by_tag'),
    path('', views.drama_list, name='drama_list'),
    path('<int:pk>/', views.drama_detail, name='drama_detail'),
    path('<int:pk>/like/', views.drama_like, name='drama_like'),
]
