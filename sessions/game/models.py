from django.db import models


class Player(models.Model):

    player_id = models.AutoField(primary_key=True)


class Game(models.Model):

    game_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    is_ended = models.BooleanField(default=False)
    players = models.ManyToManyField(Player, through='PlayerGameInfo', related_name='games')
    is_full = models.BooleanField(default=False)


class PlayerGameInfo(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)
    is_winner = models.BooleanField(default=False)
    counter_of_tries = models.IntegerField(default=0)
