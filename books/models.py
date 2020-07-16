from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='books', null = True, blank = True)


    def __str__(self):
        return self.title
