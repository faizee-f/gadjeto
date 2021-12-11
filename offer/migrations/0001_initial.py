# Generated by Django 3.2.8 on 2021-12-11 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupen_code', models.CharField(max_length=100, unique=True)),
                ('coupen_count', models.IntegerField()),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('discount', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('vendor_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendors')),
            ],
        ),
        migrations.CreateModel(
            name='VariationOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('variation_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.variation')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('subcategory_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='category.sub_category')),
            ],
        ),
        migrations.CreateModel(
            name='RedeemedCoupen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coupen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.coupen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('product_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('category_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
