# Generated by Django 3.2.18 on 2023-03-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20230322_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ManyToManyField(related_name='item', to='customer.Category'),
        ),
    ]
