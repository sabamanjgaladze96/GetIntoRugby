from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    established = models.DateField()
    division = models.IntegerField(validators=[MaxValueValidator(10)])
    subdivision = models.CharField(max_length=1)
    age_group = models.CharField(max_length=100)
    training_ground_address = models.TextField()
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    twitter_link = models.URLField(max_length=200, blank=True, null=True)
    youtube_embed_link = models.URLField(max_length=200, blank=True, null=True)


    def save(self, *args, **kwargs):
        if self.subdivision:  # Check if the field is not empty or None
            self.subdivision = self.subdivision.upper()  # Capitalize the character
        if self.team_name:
            self.team_name = self.team_name.upper()
        if self.age_group:
            self.age_group = self.age_group.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class TeamImages(models.Model):
    logo = models.ImageField()
    cover_photo = models.ImageField()


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    email_address = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name