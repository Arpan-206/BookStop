from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = 'BookStop'
admin.site.site_title = 'BookStop'
admin.site.index_title = 'BookStop Admin'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path("", views.index, name="index"),
    path("shelf/<str:category>/", views.shelf_view, name="shelf_view"),
    path("book/<int:pk>/", views.book_view, name="book_view"),
    path("logout", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
]
