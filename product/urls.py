from django.urls import path, re_path

from . import views

urlpatterns = [
    path("api/category/", views.CategoryView.as_view()),
    path("api/category/<int:id>/", views.CategoryView.as_view()),
    path("api/subcategory/", views.SubCategoryView.as_view()),
    path("api/subcategory/<int:id>/", views.SubCategoryView.as_view()),
    path("api/product/", views.ProductView.as_view()),
    path("api/product/<int:id>/", views.ProductView.as_view()),
    path("api/product/search/", views.search),
]