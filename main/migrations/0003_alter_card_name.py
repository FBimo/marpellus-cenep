# Generated by Django 4.2.5 on 2023-09-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_card_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Card Name'),
        ),
    ]