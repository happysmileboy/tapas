from django.urls import path

from . import views

app_name = 'yeonsonam'



urlpatterns = [
    path('/<str:tag_name', views.drama_search, name='drama_search_by_tag'),
    path('tag/<int:tag_pk>', views.drama_list, name='drama_list_by_tag'),
    path('', views.drama_list, name='drama_list'),
    path('test', views.drama_list_test, name='drama_list_tset'),
    path('<int:pk>/', views.drama_detail, name='drama_detail'),
    path('<int:pk>/like/', views.drama_like, name='drama_like'),
    path('place/<int:pk>/', views.place_detail, name='place_detail'),
]
