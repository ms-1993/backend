# Generated by Django 4.0.1 on 2022-01-31 14:08

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='roll',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('admin', 'ADMIN USER'), ('user', 'USER')], default='user', max_length=50),
        ),
    ]