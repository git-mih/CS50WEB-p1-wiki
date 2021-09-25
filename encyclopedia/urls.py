from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:query>", views.query, name="query"),
    path("edit/", views.edit, name="edit"),
    path("new-page/", views.new_page, name="new_page"),
    path("changes/", views.save_changes, name="save_changes"),
    path("save-entry/", views.save, name="save_entry"),
    path("random/", views.random_page, name="random"),
    path("", views.search, name="search"),
]
