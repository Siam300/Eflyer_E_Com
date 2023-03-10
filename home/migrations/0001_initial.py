# Generated by Django 4.1.7 on 2023-03-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='computers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productImage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='jhumkas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productImage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='kangans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productImage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productImage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='manShirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productImage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='manTshirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productImage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productImage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='necklaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productImage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='womanScart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productImage', models.ImageField(upload_to='product_images')),
            ],
        ),
    ]
