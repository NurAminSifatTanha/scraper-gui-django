# Generated by Django 3.1.3 on 2020-11-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebook',
            name='id',
        ),
        migrations.RemoveField(
            model_name='feefo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='google',
            name='id',
        ),
        migrations.RemoveField(
            model_name='trust',
            name='id',
        ),
        migrations.RemoveField(
            model_name='youtube',
            name='id',
        ),
        migrations.AlterField(
            model_name='facebook',
            name='url',
            field=models.CharField(max_length=3000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feefo',
            name='url',
            field=models.CharField(max_length=3000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='google',
            name='url',
            field=models.CharField(max_length=3000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trust',
            name='url',
            field=models.CharField(max_length=3000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='youtube',
            name='url',
            field=models.CharField(max_length=3000, primary_key=True, serialize=False),
        ),
    ]