# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('line_total', models.DecimalField(decimal_places=2, default=10.99, max_digits=1000)),
                ('basket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Item')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='basket',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecom.Basket'),
            preserve_default=False,
        ),
    ]
