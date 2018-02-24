from django.urls import path

from . import views

app_name = 'yeonsonam'



urlpatterns = [

    path('', views.drama_list, name='drama_list'),

    path('<int:pk>/', views.drama_detail, name='drama_detail'),
    path('<int:pk>/like/', views.drama_like, name='drama_like'),
    path('place/<int:pk>/', views.place_detail, name='place_detail'),
        path('ajax/rating/', views.DramaRatingAjaxView.as_view(), name='ajax_rating'),
]
