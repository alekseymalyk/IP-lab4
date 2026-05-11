from django.db import models
from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    first_name = models.CharField(_("Ім'я"), max_length=200)
    last_name = models.CharField(_("Прізвище"), max_length=200)
    bio = models.TextField(_("Біографія"))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Автор")
        verbose_name_plural = _("Автори")

class Genre(models.Model):
    name = models.CharField(_("Назва жанру"), max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Жанр")
        verbose_name_plural = _("Жанри")

class Book(models.Model):
    title = models.CharField(_("Назва книги"), max_length=200)
    summary = models.TextField(_("Опис"))
    published_year = models.IntegerField(_("Рік видання"))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_("Автор"))
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name=_("Жанр"))

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("Книга")
        verbose_name_plural = _("Книги")