from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=450)  # Заголовок поста
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now=True)
    body = models.TextField()  # Поле нашего поста

    def __str__(self):  # Метод
        return self.title

