from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    description = models.TextField()
    tags = models.TextField()
    alt = models.CharField(max_length=128, default="image alt")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alt

    class Meta:
        ordering = ["-updated_at"]
