# Generated by Django 2.1.1 on 2019-06-30 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('is_ended', models.BooleanField(default=False)),
                ('is_full', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_author', models.BooleanField(default=False)),
                ('is_winner', models.BooleanField(default=False)),
                ('counter_of_tries', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='games', through='game.PlayerGameInfo', to='game.Player'),
        ),
    ]