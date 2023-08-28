from django.db import models
from social.models import Profile

class Chat(models.Model):
    message = models.TextField()
    media = models.BinaryField()
    sended_at = models.DateTimeField()
    readed_at = models.DateTimeField()
    sender = models.ForeignKey(
        Profile,
        related_name="sender",
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.message
