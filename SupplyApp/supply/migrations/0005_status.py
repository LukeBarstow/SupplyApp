# Generated by Django 2.2 on 2019-04-26 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0004_remove_bathroom_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('item_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='supply.Item')),
            ],
        ),
    ]