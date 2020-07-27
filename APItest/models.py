from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=7, null=False, blank=False)
    firstname = models.CharField(max_length=25, null=False, blank=False)
    lasttname = models.CharField(max_length=25, null=False, blank=False)
    dateofbirth = models.DateField(null=False, blank=False)
    genderGroup = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=8, choices=genderGroup, null=False, blank=False)
    result = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])


