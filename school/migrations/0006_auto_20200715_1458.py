# Generated by Django 3.0.8 on 2020-07-15 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20200715_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.Period'),
        ),
    ]
