# Generated by Django 3.1 on 2023-04-15 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20230416_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cart_item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
