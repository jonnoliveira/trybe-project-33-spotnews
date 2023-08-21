# Generated by Django 4.2.3 on 2023-08-21 21:07

from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0005_alter_news_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(
                max_length=200,
                validators=[news.validators.validate_counter_words],
            ),
        ),
    ]