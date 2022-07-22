from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    sub_content = models.TextField()
    content = models.TextField()
    image = models.URLField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.title