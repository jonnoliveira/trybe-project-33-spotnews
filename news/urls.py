from django.urls import path
from news.views import index, details, category_form


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", details, name="news-details-page"),
    path("categories/", category_form, name="categories-form"),
]
