# Generated by Django 2.2 on 2019-04-26 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0002_auto_20190425_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bathroom',
            name='floor',
        ),
        migrations.RemoveField(
            model_name='floor',
            name='barracks',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Bathroom',
        ),
        migrations.AddField(
            model_name='bathroom',
            name='floor_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='supply.Floor'),
        ),
        migrations.AddField(
            model_name='floor',
            name='barracks_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='supply.Barracks'),
        ),
        migrations.AddField(
            model_name='item',
            name='bathroom_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='supply.Bathroom'),
        ),
    ]