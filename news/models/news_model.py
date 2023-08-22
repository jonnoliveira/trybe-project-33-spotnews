from django.db import models

from news.validators import validate_counter_words, validate_date


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[validate_counter_words]
    )
    content = models.TextField()
    author = models.ForeignKey("Users", on_delete=models.CASCADE)
    created_at = models.DateField(validators=[validate_date])
    image = models.ImageField(blank=True, null=True, upload_to="img/")
    categories = models.ManyToManyField("Categories")

    def __str__(self):
        return self.title
