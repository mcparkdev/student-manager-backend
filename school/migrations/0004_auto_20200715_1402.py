# Generated by Django 3.0.8 on 2020-07-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20200715_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='textbook1_1',
            field=models.DecimalField(decimal_places=0, default=10000, max_digits=15),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook1_1Payed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook1_2',
            field=models.DecimalField(decimal_places=0, default=10000, max_digits=15),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook1_2Payed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook2_1',
            field=models.DecimalField(decimal_places=0, default=10000, max_digits=15),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook2_1Payed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook2_2',
            field=models.DecimalField(decimal_places=0, default=10000, max_digits=15),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook2_2Payed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook3_1',
            field=models.DecimalField(decimal_places=0, default=10000, max_digits=15),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook3_1Payed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook3_2',
            field=models.DecimalField(decimal_places=0, default=10000, max_digits=15),
        ),
        migrations.AddField(
            model_name='student',
            name='textbook3_2Payed',
            field=models.BooleanField(default=False),
        ),
    ]
