# Generated by Django 4.2.7 on 2023-11-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='disponibility',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='box',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]