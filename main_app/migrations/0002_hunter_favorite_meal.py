# Generated by Django 3.1.1 on 2020-10-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hunter',
            name='favorite_meal',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]