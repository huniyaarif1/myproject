# Generated by Django 2.1.7 on 2019-03-08 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_favourite_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='ads',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='city',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='contact',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='image',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='negotiable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ads',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ads',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='subcategories',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ads',
            name='used',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ads',
            name='userId',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
