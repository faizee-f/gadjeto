# Generated by Django 3.2.8 on 2021-11-25 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_variation_product'),
        ('cart', '0003_remove_cartitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='varient',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='varient',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
