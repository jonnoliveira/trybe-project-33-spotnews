from django.shortcuts import redirect, render
from news.models import News
from news.forms import CategoryForm, NewsForm


def index(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "home.html", context)


def details(request, id):
    news = News.objects.get(id=id)
    context = {"news": news}
    return render(request, "news_details.html", context)


def category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")

    context = {"form": form}
    return render(request, "categories_form.html", context)


def news(request):
    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home-page")

    context = {"form": form}
    return render(request, "news_form.html", context)
