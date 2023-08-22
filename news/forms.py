from django import forms
from news.models.category_model import Categories
from news.models.user_model import Users
from news.models.news_model import News


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label="Nome", max_length=200)

    class Meta:
        model = Categories
        fields = ["name"]


class NewsForm(forms.ModelForm):
    title = forms.CharField(label="Título", max_length=200)
    content = forms.CharField(
        widget=forms.Textarea, label="Conteúdo", max_length=200
    )
    author = forms.ModelChoiceField(
        label="Autoria", queryset=Users.objects.all()
    )
    created_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "date"}), label="Criado em"
    )
    image = forms.ImageField(label="URL da Imagem")
    categories = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label="Categorias",
        queryset=Categories.objects.all(),
    )

    class Meta:
        model = News
        fields = ["title", "content", "author", "created_at", "image"]
