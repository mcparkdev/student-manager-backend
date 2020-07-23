# Generated by Django 3.0.8 on 2020-07-10 05:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('englishName', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('fee', models.DecimalField(decimal_places=0, max_digits=12)),
                ('salary', models.DecimalField(decimal_places=0, default=400000, max_digits=12)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('startTime', models.TimeField(default=datetime.time(14, 0))),
                ('endTime', models.TimeField(default=datetime.time(17, 0))),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2020)),
                ('name', models.CharField(max_length=255)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.IntegerField(unique=True)),
                ('registerDate', models.DateField(default=datetime.date.today)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('birthDate', models.DateField()),
                ('gender', models.CharField(max_length=255)),
                ('documentID', models.DecimalField(decimal_places=0, max_digits=15)),
                ('documentType', models.CharField(max_length=255)),
                ('phoneNumber', models.DecimalField(decimal_places=0, max_digits=15)),
                ('email', models.EmailField(max_length=255)),
                ('ocupation', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('guardianFirstName', models.CharField(max_length=255)),
                ('guardianLastName', models.CharField(max_length=255)),
                ('guardianRelationship', models.CharField(max_length=255)),
                ('guardianPhoneNumber', models.IntegerField()),
                ('detailMedia', models.CharField(blank=True, max_length=255, null=True)),
                ('detailMotivation', models.CharField(blank=True, max_length=255, null=True)),
                ('detailObjective', models.CharField(blank=True, max_length=255, null=True)),
                ('payedCourse', models.BooleanField(default=False)),
                ('specialFee', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('course', models.ManyToManyField(to='school.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('englishName', models.CharField(max_length=255)),
                ('registerDate', models.DateField(default=datetime.date.today)),
                ('contractStartDate', models.DateField(default=datetime.date.today)),
                ('contractEndDate', models.DateField(null=True)),
                ('birthDate', models.DateField()),
                ('gender', models.CharField(max_length=255)),
                ('documentType', models.CharField(max_length=255)),
                ('documentID', models.DecimalField(decimal_places=0, max_digits=15)),
                ('phoneNumber', models.DecimalField(decimal_places=0, max_digits=15)),
                ('email', models.EmailField(max_length=255)),
                ('ocupation', models.CharField(blank=True, max_length=255, null=True)),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('course', models.ManyToManyField(to='school.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Period'),
        ),
    ]