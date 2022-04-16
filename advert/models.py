from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Подкатегория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Advert(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Тема')
    content = models.TextField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_publushed = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
