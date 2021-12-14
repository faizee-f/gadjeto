# Generated by Django 4.0 on 2021-12-14 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('vendors', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='photos/product')),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendors')),
            ],
        ),
        migrations.CreateModel(
            name='VarientColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varient_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('ram', models.CharField(choices=[('2 GB', '2 GB'), ('4 GB', '4 GB'), ('6 GB', '6 GB'), ('8 GB', '8 GB'), ('12 GB', '12 GB')], max_length=20)),
                ('storage', models.CharField(choices=[('16 GB', '16 GB'), ('32 GB', '32 GB'), ('64 GB', '64 GB'), ('128 GB', '128 GB'), ('256 GB', '256 GB'), ('512 GB', '512 GB'), ('1 TB', '1 TB')], max_length=50)),
                ('image4', models.ImageField(blank=True, upload_to='photos/product')),
                ('image1', models.ImageField(blank=True, upload_to='photos/product')),
                ('image2', models.ImageField(blank=True, upload_to='photos/product')),
                ('image3', models.ImageField(blank=True, upload_to='photos/product')),
                ('margin_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.varientcolor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='varion', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('review', models.TextField(blank=True, max_length=500)),
                ('rating', models.FloatField()),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('varient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.variation')),
            ],
        ),
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendors')),
            ],
        ),
    ]
