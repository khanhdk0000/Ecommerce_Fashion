# Generated by Django 3.2.9 on 2021-11-05 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('favorite_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_favorite', to='checkout.registeredcustomer')),
            ],
            options={
                'db_table': 'favorite',
            },
        ),
    ]
