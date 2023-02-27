from enum import unique
from django.db import models


class Characters(models.Model):
    """Creates table with characters"""
    first_name = models.CharField(max_length=100, verbose_name='First name')
    middle_name = models.CharField(max_length=100, blank=True, verbose_name='Middle name')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Last name')
    title = models.CharField(max_length=100, blank=True, verbose_name='Title')
    race = models.CharField(max_length=100, verbose_name='Race')
    char_class = models.CharField(max_length=100, verbose_name='Class')
    char_age = models.CharField(max_length=100, blank=True, verbose_name='Age')
    eye_color = models.CharField(max_length=100, blank=True, verbose_name='Eye color')
    height = models.CharField(max_length=100, blank=True, verbose_name='Height')
    body_shape = models.CharField(max_length=100, blank=True, verbose_name='Body shape')
    birthplace = models.CharField(max_length=100, blank=True, verbose_name='Birthplace')
    residence = models.CharField(max_length=100, blank=True, verbose_name='Residence')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'Character: pk={self.pk}, name={self.first_name} {self.last_name}'

    class Meta:
        """Used for translation"""
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'


class Factions(models.Model):
    """Creates table with factions"""
    faction_name = models.CharField(max_length=100, verbose_name='Faction')
    faction_image = models.ImageField(upload_to='faction/', null=True, blank=True, verbose_name='Faction icon')
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               verbose_name='Primary-faction',
                               related_name='primaryfaction')

    def __str__(self):
        return self.faction_name

    def __repr__(self):
        return f'Factions: pk={self.pk}, name={self.faction_name}'

    class Meta:
        """Used for translation"""
        verbose_name = 'Faction'
        verbose_name_plural = 'Factions'


class Gallery(models.Model):
    """Creates table for character images"""
    image = models.ImageField(upload_to='character/', verbose_name='Character Image')
    character = models.ForeignKey(Characters, on_delete=models.CASCADE, related_name='images')

    class Meta:
        """Used for translation"""
        verbose_name = 'Character gallery'
        verbose_name_plural = 'Character gallery'
