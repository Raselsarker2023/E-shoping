# Generated by Django 5.0 on 2024-03-26 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productmodel_category_alter_review_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='reviewer',
        ),
        migrations.AddField(
            model_name='review',
            name='product_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productmodel'),
        ),
    ]