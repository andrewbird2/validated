# Generated by Django 2.2.7 on 2019-11-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validated', '0004_auto_20191118_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
