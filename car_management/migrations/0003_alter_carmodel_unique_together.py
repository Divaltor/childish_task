# Generated by Django 4.0.3 on 2022-03-05 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_management', '0002_alter_carbrand_managers_alter_carbrand_deleted_at'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together={('name', 'car_brand')},
        ),
    ]
