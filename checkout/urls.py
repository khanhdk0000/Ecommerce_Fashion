from django.urls import path, include

from checkout import views

urlpatterns = [
    path("api/checkout/order/", views.OrderView.as_view()),
    path("api/checkout/order/id/<int:order_id>/", views.OrderView.as_view()),
    path("api/checkout/order/customer/<str:customer_id>/",
         views.OrderView.as_view()),
    path("api/checkout/order/<int:order_id>/<str:customer_id>/",
         views.OrderView.as_view()),
    path("api/checkout/cart/", views.OrderDetailView.as_view()),
    path(
        "api/checkout/cart/product/<int:product_id>/",
        views.OrderDetailView.as_view(),
    ),
    path(
        "api/checkout/cart/order/<int:order_id>/",
        views.OrderDetailView.as_view(),
    ),
    path(
        "api/checkout/cart/<int:order_id>/<int:product_id>/",
        views.OrderDetailView.as_view(),
    ),
    path("api/user/", views.RegisteredCustomerView.as_view()),
    path("api/user/<str:customer_id>", views.RegisteredCustomerView.as_view()),
]
