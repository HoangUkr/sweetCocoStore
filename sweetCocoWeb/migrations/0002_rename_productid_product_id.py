# Generated by Django 5.0.2 on 2024-03-01 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweetCocoWeb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productId',
            new_name='id',
        ),
    ]
