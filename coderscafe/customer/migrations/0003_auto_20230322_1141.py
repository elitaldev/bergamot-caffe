# Generated by Django 3.2.18 on 2023-03-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_menuitem_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='item',
            new_name='items',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ManyToManyField(related_name='item', to='customer.Category'),
        ),
    ]
