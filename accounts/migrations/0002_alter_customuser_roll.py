# Generated by Django 4.0.1 on 2022-01-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='roll',
            field=models.CharField(choices=[('admin', 'ADMIN USER'), ('user', 'USER')], default='user', max_length=50),
        ),
    ]
