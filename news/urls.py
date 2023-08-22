from django.urls import path
from news.views import index, details, category, news


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", details, name="news-details-page"),
    path("categories/", category, name="categories-form"),
    path("news/", news, name="news-form"),
]
