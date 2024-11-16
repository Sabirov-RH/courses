from django.db import models
from django.utils import timezone

# Модель категория для курсов
class Category(models.Model):
    title = models.CharField(max_length = 255) # Поле заголовок
    created_at = models.DateTimeField(default=timezone.now) # Поле будет создоваться автоматический

    def __str__(self):
        return self.title

# Модель для курсов
class Course(models.Model):
    title = models.CharField(max_length=300) #  Название курса
    price = models.FloatField() # Цена курса (число с плавающей точкой)
    student_qty = models.IntegerField() # Количество сутдентов (целое число)
    reviews_qty = models.IntegerField() # Колоичество отзывов (целое число)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # ключ из другой таблицы
    # on_delete=models.CASCADE - говорит, что при удалении категории 
    # будут удалены все курсы в этой категории
    created_at = models.DateTimeField(default=timezone.now) # Поле будет создоваться автоматический

    def __str__(self):
        return self.title