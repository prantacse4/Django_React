# Generated by Django 3.2.4 on 2021-07-01 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classstudents',
            name='classroom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.teacher'),
        ),
    ]
