from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=100)
    legacy = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    followers = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    content = models.TextField()
    media = models.BinaryField()
    views = models.IntegerField()
    likes = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.content

class Comment(models.Model):
    message = models.TextField()
    likes = models.IntegerField()
    unlikes = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.message