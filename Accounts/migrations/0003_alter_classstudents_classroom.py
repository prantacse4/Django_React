# Generated by Django 3.2.4 on 2021-07-01 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_classstudents_classroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classstudents',
            name='classroom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.myclassroom'),
        ),
    ]