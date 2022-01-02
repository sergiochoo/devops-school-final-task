from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=70)
    gravity = models.CharField(max_length=70)
    climate = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=200)
    MALE = "Male"
    FEMALE = "Female"
    GENDERS = [
        (MALE, "Male"),
        (FEMALE, "Female"),
    ]
    gender = models.CharField(
        choices=GENDERS,
    )
    homeworld = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
