from django.urls import path, re_path

from . import views

urlpatterns = [
    path("api/favorite/", views.FavoriteView.as_view()),
    path("api/favorite/<str:customer_id>", views.FavoriteView.as_view()),
    path("api/contains/", views.ContainsView.as_view()),
    path("api/contains/<int:product_id>/<str:customer_id>", views.ContainsView.as_view()),
    path("api/wishlist/<str:customer_id>", views.wishlist)
]