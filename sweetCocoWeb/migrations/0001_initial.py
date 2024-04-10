# Generated by Django 5.0.2 on 2024-04-10 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('isFinish', models.BooleanField(default=False)),
                ('isSent', models.BooleanField(default=False)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('sentDate', models.DateTimeField(blank=True, null=True)),
                ('finishedDate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['orderId', 'createdDate'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('category', models.CharField(default='Cupcake', max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name', 'price', 'id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweetCocoWeb.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweetCocoWeb.product')),
            ],
        ),
    ]
