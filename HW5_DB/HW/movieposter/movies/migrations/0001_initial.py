# Generated by Django 3.2.8 on 2021-11-05 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('genre', models.ForeignKey(default='ERROR, PLS PUT GENRE', on_delete=django.db.models.deletion.SET_DEFAULT, to='genres.genre')),
                ('main_actor', models.ForeignKey(default='ERROR, PLS PUT ACTOR', on_delete=django.db.models.deletion.SET_DEFAULT, to='actors.actor')),
            ],
        ),
    ]
