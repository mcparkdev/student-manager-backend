from django.db import models
import datetime

# Create your models here.


class Admin(models.Model):
    name = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    # objects = models.Manager()

    def __str__(self):
        return self.name


class Period (models.Model):
    year = models.IntegerField(default=2020)
    name = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    # objects = models.Manager()

    def __str__(self):
        return f'{self.year}/{self.name}'


class Course (models.Model):
    period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    fee = models.DecimalField(max_digits=12, decimal_places=0)
    salary = models.DecimalField(
        max_digits=12, decimal_places=0, default=400000)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    startTime = models.TimeField(default=datetime.time(14, 0, 0))
    endTime = models.TimeField(default=datetime.time(17, 0, 0))
    comment = models.CharField(max_length=255, blank=True, null=True)

    # objects = models.Manager()

    def __str__(self):
        return f'{self.period}/{self.name}'


class Staff (models.Model):
    course = models.ManyToManyField(Course)
    name = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255)
    registerDate = models.DateField(default=datetime.date.today)
    contractStartDate = models.DateField(default=datetime.date.today)
    contractEndDate = models.DateField(null=True, blank=True)
    birthDate = models.DateField()
    gender = models.CharField(max_length=255)
    documentType = models.CharField(max_length=255)
    documentID = models.DecimalField(max_digits=15, decimal_places=0)
    phoneNumber = models.DecimalField(max_digits=15, decimal_places=0)
    email = models.EmailField(max_length=255)
    ocupation = models.CharField(max_length=255, blank=True, null=True)
    profileImage = models.ImageField(
        null=True, blank=True, default='media/Anonymous-Avatar.png')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    # objects = models.Manager()

    def __str__(self):
        return self.name


class Student (models.Model):
    course = models.ManyToManyField(Course)
    studentID = models.IntegerField(unique=True)
    registerDate = models.DateField(default=datetime.date.today)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    birthDate = models.DateField()
    gender = models.CharField(max_length=255)
    documentID = models.DecimalField(max_digits=15, decimal_places=0)
    documentType = models.CharField(max_length=255)
    phoneNumber = models.DecimalField(max_digits=15, decimal_places=0)
    email = models.EmailField(max_length=255)
    ocupation = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    profileImage = models.ImageField(
        null=True, blank=True, default='media/Anonymous-Avatar.png')
    guardianFirstName = models.CharField(max_length=255)
    guardianLastName = models.CharField(max_length=255)
    guardianRelationship = models.CharField(max_length=255)
    guardianPhoneNumber = models.DecimalField(max_digits=15, decimal_places=0)
    detailMedia = models.CharField(max_length=255, null=True, blank=True)
    detailMotivation = models.CharField(max_length=255, null=True, blank=True)
    detailObjective = models.CharField(max_length=255, null=True, blank=True)
    payedCourse = models.BooleanField(default=False)
    specialFee = models.DecimalField(
        max_digits=12, decimal_places=0, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    textbook1_1Payed = models.CharField(max_length=255, default="available")
    textbook1_2Payed = models.CharField(max_length=255, default="available")
    textbook2_1Payed = models.CharField(max_length=255, default="available")
    textbook2_2Payed = models.CharField(max_length=255, default="available")
    textbook3_1Payed = models.CharField(max_length=255, default="available")
    textbook3_2Payed = models.CharField(max_length=255, default="available")
    textbook1_1 = models.DecimalField(
        max_digits=15, decimal_places=0, default=10000)
    textbook1_2 = models.DecimalField(
        max_digits=15, decimal_places=0, default=10000)
    textbook2_1 = models.DecimalField(
        max_digits=15, decimal_places=0, default=10000)
    textbook2_2 = models.DecimalField(
        max_digits=15, decimal_places=0, default=10000)
    textbook3_1 = models.DecimalField(
        max_digits=15, decimal_places=0, default=10000)
    textbook3_2 = models.DecimalField(
        max_digits=15, decimal_places=0, default=10000)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    # objects = models.Manager()

    def __str__(self):
        return f'{self.firstName} {self.lastName} - {self.studentID}'
