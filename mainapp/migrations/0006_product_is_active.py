# Generated by Django 2.2.24 on 2021-11-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_productcategory_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="продукт активен"),
        ),
    ]
