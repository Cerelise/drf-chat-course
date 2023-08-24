from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return f"/{self.slug}/"

    def __str__(self) -> str:
        return self.name