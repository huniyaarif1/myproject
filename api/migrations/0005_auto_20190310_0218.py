# Generated by Django 2.1.7 on 2019-03-09 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190309_0255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='ptitle',
        ),
    ]
