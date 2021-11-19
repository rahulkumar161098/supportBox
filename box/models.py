from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()
    image = models.ImageField(upload_to= 'artImage/image', default='')  #upload_to use to create a folder under any app
    date = models.DateTimeField(auto_now_add=True)
    # slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title
