# Generated by Django 2.2 on 2019-04-26 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bathroom',
            name='floor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='supply.Floor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='floor',
            name='barracks',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='supply.Barracks'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='Bathroom',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='supply.Floor'),
            preserve_default=False,
        ),
    ]