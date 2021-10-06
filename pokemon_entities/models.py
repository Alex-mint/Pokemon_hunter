from django.db import models


class Pokemon(models.Model):
    title = models.CharField('название', max_length=200)
    title_en = models.CharField('название на английском', max_length=200,
                                blank=True)
    title_jp = models.CharField('название на японском', max_length=200,
                                blank=True)
    image = models.ImageField('картинка', upload_to='images')
    description = models.TextField('описание', blank=True)
    previous_evolution = models.ForeignKey("self", on_delete=models.SET_NULL,
                                           related_name='next_evolution',
                                           blank=True, null=True,
                                           verbose_name='из кого эволюционировал')

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                verbose_name='покемон',
                                related_name='entities')
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')
    appeared_at = models.DateTimeField('появился в', null=True, blank=True)
    disappeared_at = models.DateTimeField('исчезнет в', null=True, blank=True)
    level = models.IntegerField('уровень', null=True, blank=True)
    health = models.IntegerField('здоровье', null=True, blank=True)
    strength = models.IntegerField('сила', null=True, blank=True)
    defence = models.IntegerField('защита', null=True, blank=True)
