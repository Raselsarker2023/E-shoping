# Generated by Django 5.0 on 2024-04-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_remove_cart_total_price_remove_wishlist_wished_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='produce_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]