# Generated by Django 3.1.5 on 2021-01-21 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0013_auto_20210121_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacorrente',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]