# Generated by Django 2.0.3 on 2018-03-24 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180324_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot_save',
            name='by',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]