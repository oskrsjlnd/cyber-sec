# Generated by Django 4.1.4 on 2022-12-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_remove_account_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]