# Generated by Django 4.1.5 on 2023-02-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
    ]
