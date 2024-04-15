# Generated by Django 4.2.7 on 2023-11-24 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('category', models.CharField(max_length=20, null=True)),
                ('image', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50, null=True)),
                ('disponibility', models.CharField(max_length=50, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.game')),
            ],
            options={
                'permissions': (('peut_marque_retourner', 'declarer_unjeu_comme_retourne'),),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=2000)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('gameinstance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.gameinstance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
