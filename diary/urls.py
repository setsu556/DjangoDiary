from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path("", views.index, name="index"),
    path("page/create/", views.page_create, name="page_create"),
    path("pages/", views.page_list, name="page_list"),
    path("pages/<uuid:page_id>/", views.page_detail, name="page_detail"),
    path("pages/<uuid:page_id>/update/", views.page_update, name="page_update")
]
