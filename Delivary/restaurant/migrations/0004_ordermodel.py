# Generated by Django 4.0.5 on 2022-06-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_foods_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=15)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
    ]
