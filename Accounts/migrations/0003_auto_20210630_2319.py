# Generated by Django 3.2.4 on 2021-06-30 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20210630_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='classroom',
        ),
        migrations.AddField(
            model_name='myclassroom',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Accounts.teacher'),
            preserve_default=False,
        ),
    ]
