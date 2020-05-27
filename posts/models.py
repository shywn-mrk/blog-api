from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    summary = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title
