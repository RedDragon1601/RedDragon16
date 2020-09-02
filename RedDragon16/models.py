from django.db import models

# Create your models here.
class HomePost(models.Model):
    title = models.CharField(max_length = 16)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class AboutPost(models.Model):
    title = models.CharField(max_length = 16)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class CodingPost(models.Model):
    title = models.CharField(max_length = 16)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title