from django.urls import path, re_path

from . import views

urlpatterns = [
    path("api/favorite/", views.FavoriteView.as_view()),
    path("api/favorite/<int:customer_id>", views.FavoriteView.as_view()),
]