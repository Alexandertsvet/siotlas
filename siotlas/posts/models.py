from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

GROUP_CHOICES = (
    ('Басни', 'Басни'),
    ('Сказки', 'Сказки'),
    ('Стихотверения', 'Стихотверения'),
)


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="название",
        help_text="Выберите группу",
        choices=GROUP_CHOICES,
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="уникальный фрагмент URL-адреса",
        help_text="Введите уникальный фрагмент URL-адреса для группы",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание группы"
    )

    class Meta:
        verbose_name = ('група')
        verbose_name_plural = ('Группы')

    def __str__(self) -> str:
        return self.title[:15]


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=('название группы'),
        related_name='posts',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = ('пост')
        verbose_name_plural = ('Посты')

    def __str__(self) -> str:
        return self.text[:15]
