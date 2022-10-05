# Generated by Django 4.0.4 on 2022-08-23 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='', upload_to='pictures')),
            ],
        ),
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('product_price', models.FloatField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.picture')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.productname')),
            ],
        ),
    ]