# Generated by Django 3.0.8 on 2020-07-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20200715_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='textbook1_1Payed',
            field=models.CharField(default='available', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='textbook1_2Payed',
            field=models.CharField(default='available', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='textbook2_1Payed',
            field=models.CharField(default='available', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='textbook2_2Payed',
            field=models.CharField(default='available', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='textbook3_1Payed',
            field=models.CharField(default='available', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='textbook3_2Payed',
            field=models.CharField(default='available', max_length=255),
        ),
    ]
