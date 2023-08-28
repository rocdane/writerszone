from django.db import models
from social.models import Profile

class Article(models.Model):
    title = models.CharField(max_length=255)
    resume = models.TextField()
    content = models.TextField()
    views = models.IntegerField()
    likes = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title
