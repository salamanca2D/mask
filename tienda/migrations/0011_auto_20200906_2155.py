# Generated by Django 3.1 on 2020-09-07 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_auto_20200906_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='tienda.sizesgeneral'),
        ),
    ]
