# Generated by Django 3.1.1 on 2023-04-23 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230404_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1000, max_length=1000),
            preserve_default=False,
        ),
    ]
