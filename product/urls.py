from django.urls import path, re_path

from . import views

urlpatterns = [
  path('category/', views.CategoryView.as_view()),
  path('category/<int:id>/', views.CategoryView.as_view()),
  path('subcategory/', views.SubCategoryView.as_view()),
  path('subcategory/<int:id>/', views.SubCategoryView.as_view()),
  path('product/', views.ProductView.as_view()),
  path('product/<int:id>/', views.ProductView.as_view()),
  path('product/search/', views.search),
]