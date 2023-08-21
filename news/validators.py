import datetime
from django.core.exceptions import ValidationError


def validate_counter_words(title):
    if len(str(title).split()) <= 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


def validate_date(date):
    try:
        datetime.datetime.strptime(str(date), "%Y-%m-%d")
    except ValueError:
        raise ValidationError(
            "Use o formato AAAA-MM-DD e uma data igual ou anterior a hoje."
        )
