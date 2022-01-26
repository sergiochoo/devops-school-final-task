from django.db import models


class Planet(models.Model):
    url = models.URLField(primary_key=True)
    name = models.CharField(max_length=70)
    gravity = models.CharField(max_length=70)
    climate = models.CharField(max_length=70)

    def get_json(self):
        return {
            "url": self.url,
            "name": self.name,
            "gravity": self.gravity,
            "climate": self.climate,
            "characters": [{
                "url": ch.url,
                "name": ch.name,
                "gender": ch.gender,
            } for ch in self.character_set.all()]
        }

    def __str__(self):
        return self.name


class Character(models.Model):
    url = models.URLField(primary_key=True)
    name = models.CharField(max_length=200)
    MALE = "Male"
    FEMALE = "Female"
    GENDERS = [
        (MALE, "Male"),
        (FEMALE, "Female"),
    ]
    gender = models.CharField(
        choices=GENDERS,
        max_length=6
    )
    homeworld = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
