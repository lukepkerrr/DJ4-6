from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo
from .forms import GameForm

import random

def show_home(request):
    context = {}

    player_id = request.session.get('player_id', 0)
    game_id = request.session.get('game_id', 0)

    if player_id == 0:
        player = Player.objects.create()
        request.session['player_id'] = player.player_id
    else:
        player = Player.objects.get(player_id=player_id)

    if game_id == 0:
        game = Game.objects.filter(is_ended=False, is_full=False)
        if game.first() is not None:
            game = game.first()
            player_game_info = PlayerGameInfo.objects.create(
                game=game,
                player=player,
            )
        else:
            game = Game.objects.create(number=random.randint(0, 1000))
            player_game_info = PlayerGameInfo.objects.create(
                game=game,
                player=player,
                is_author=True
            )
        request.session['game_id'] = game.game_id
    else:
        game = Game.objects.filter(is_ended=False, game_id=game_id)
        if game.first() is not None:
            game = game.first()
        else:
            games = Game.objects.filter(game_id=game_id)
            game = games.last()
        player_game_info = PlayerGameInfo.objects.get(game=game, player=player)

    if player_game_info.is_author:
        context['is_author'] = True
        context['number'] = game.number

        if game.is_ended:
            context['game_ended'] = True
            context['counter'] = PlayerGameInfo.objects.get(game=game, is_winner=True).counter_of_tries
    else:
        if request.method == 'GET':
            form = GameForm(request.GET)
            if form.is_valid():
                tried_number = form.cleaned_data['number']
                real_number = game.number
                if tried_number > real_number:
                    context['answer'] = 'Загаданное число меньше'
                elif tried_number < real_number:
                    context['answer'] = 'Загаданное число больше'
                else:
                    context['answer'] = 'Ура!'
                    player_game_info.is_winner = True
                    game.is_ended = True
                    game.save()
                player_game_info.counter_of_tries += 1
                player_game_info.save()
                context['is_winner'] = player_game_info.is_winner
                context['counter'] = player_game_info.counter_of_tries
        else:
            form = GameForm()

        context['form'] = form

    return render(
        request,
        'home.html',
        context
    )
