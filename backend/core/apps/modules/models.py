from django.db import models
from .utils import int_to_bool_status_converter as int_to_bool


class TimeBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата обновления")

    class Meta:
        abstract = True


class Module(TimeBaseModel):
    class Status(models.IntegerChoices):
        DRAFT = False, "приватный"
        PUBLISHED = True, "публичный"

    title = models.CharField(max_length=255, verbose_name="имя модуля")
    dictionary = models.JSONField(default=dict, verbose_name="Словарь (англ-рус)")
    is_public = models.BooleanField(
        choices=int_to_bool(Status.choices),
        default=Status.DRAFT,
        verbose_name="Видимость",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"
