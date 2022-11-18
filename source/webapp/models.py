from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    author = models.CharField(max_length=50, verbose_name="Автор", default="Unknown")
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f'{self.pk}. {self.title}'


class Comment(models.Model):
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=50, default='Unknown', verbose_name='Автор')
    article = models.ForeignKey('webapp.Article', on_delete=models.CASCADE, related_name='comments',
                                verbose_name="Статья")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f'{self.pk}. {self.text[:20]}'

