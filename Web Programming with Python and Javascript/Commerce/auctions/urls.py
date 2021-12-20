from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("l/<str:listing_id>", views.listing_view, name="listing"),
    path("create", views.create_listing_view, name="create"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
