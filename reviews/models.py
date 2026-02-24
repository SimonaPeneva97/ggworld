from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from games.models import Game


class Review(models.Model):
    models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(
        max_length=100,
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.username} - {self.game.title} - {self.rating}"
