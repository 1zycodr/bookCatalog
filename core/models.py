from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from model_utils.models import TimeStampedModel


class Book(TimeStampedModel):
    title = models.CharField(
        max_length=255,
        verbose_name='Название книги',
    )
    author = models.ForeignKey(
        'Author',
        related_name='books',
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    genre = models.ForeignKey(
        'Genre',
        related_name='books',
        on_delete=models.CASCADE,
        verbose_name='Жанр',
    )
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    publish_date = models.DateField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Review(TimeStampedModel):
    book = models.ForeignKey(
        Book,
        related_name='reviews',
        on_delete=models.CASCADE,
        verbose_name='Книга',
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Рейтинг',
    )
    text = models.TextField(verbose_name='Текст отзыва')

    class Meta:
        unique_together = ('book', 'user')
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.user} - {self.book}'


class Author(TimeStampedModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя автора',
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Genre(TimeStampedModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Название жанра',
        unique=True,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Featured(TimeStampedModel):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name='Книга',
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    class Meta:
        unique_together = ('book', 'user')
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f'{self.user} - {self.book}'
