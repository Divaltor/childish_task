# Generated by Django 4.0.3 on 2022-03-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='carbrand',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='carbrand',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
