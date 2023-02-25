from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


# Create your models here.

class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Активна'
    NOT_ACTIVE = 'BLOCKED', 'Заблокировано'


class GuestBook(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(max_length=1000, null=False, blank=False, verbose_name='Email')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создание')
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')
    status = models.CharField(max_length=100, choices=StatusChoice.choices, verbose_name='Статус',
                              default=StatusChoice.ACTIVE)

    def __str__(self):
        return f'{self.author} - {self.email} - {self.text} - {self.status}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
