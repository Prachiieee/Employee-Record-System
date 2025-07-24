from django.db import models
from django_countries.fields import CountryField
import random
import string
import django_countries

# Create your models here.

def generate_unique_id():
    prefix = 'MEV'
    middle='_'
    suffix = ''.join(random.choice(string.digits,k=10))
    return f'{prefix}{middle}{suffix}'

class EmployeeDetails(models.Model):
    gender_choice=[
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    ]

    country_list=[
        ('USA','USA'),
        ('Britain','Britain'),
        ('Canada','Canada')
    ]

    employment_type_choice=[
        ('FT','Fulltime'),
        ('PT','Parttime'),
        ('FX','Flexible'),
        ('CT','Contract')
    ]
    #bio info
    first_name=models.CharField(max_length=70)
    middle_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    gender=models.CharField(max_length=20,choices=gender_choice)
    date_of_birth=models.DateField()
    #contact info
    email=models.EmailField(unique=True)
    contact_number=models.CharField(max_length=25,unique=True)
    address_line_1=models.CharField(max_length=300)
    address_line_2=models.CharField(max_length=300)
    city=models.CharField(max_length=150)
    nationality=CountryField(blank_label='(select country)',max_length=200)
    # country=models.CharField(max_length=1,choices=country_list)
    
    zip_or_post_code=models.CharField(max_length=20)

    #employment Information
    employment_id=models.CharField(unique=True,max_length=20)
    job_title=models.CharField(max_length=100)
    departments=models.ManyToManyField('Department',blank=True)
    employment_type=models.CharField(max_length=120,choices=employment_type_choice)
    supervisor=models.CharField(null=True,blank=True,max_length=120)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()

    #additional information
    next_of_kin=models.CharField(max_length=200,null=True,blank=True)
    next_of_kin_contact=models.CharField(max_length=30,null=True,blank=True)
    next_of_kin_address=models.CharField(max_length=250,null=True,blank=True)
    relationship=models.CharField(max_length=100,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Employee Detail"
        verbose_name_plural = "Employee Details"


    def save(self,*args,**kwargs):
        if not self.employment_id:
            self.employment_id=self.generate_unique_employee_id()
        super().save(*args, **kwargs)
    
    def generate_unique_employee_id(self):
        the_employee_id = generate_unique_id()
        while EmployeeDetails.objects.filter(employment_id = the_employee_id).exists():
            the_employee_id=generate_unique_id()
            return the_employee_id
        
        #to check if you know


    def __str__(self):
        return f'{self.id} {self.first_name}'


class Department(models.Model):
    name_of_department=models.CharField(max_length=150,unique=True)
    department_code=models.CharField(max_length=20,unique=True)
    department_head=models.OneToOneField('EmployeeDetails',max_length=120,null=True,blank=True,on_delete=models.SET_NULL)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_department

class Skills(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description=models.TextField()
    dept = models.ManyToManyField('Department',max_length=200,null=True,blank=True)

    class Meta:
        verbose_name="Skills"
        verbose_name_plural = "Skills"


    def __str__(self):
        return self.name
    

class Training(models.Model):

    allTrainingLocation=[
        ('ONSITE','onsite'),
        ('REMOTE','Remote'),
        ('HYBRID','Hybrid')
    ]
    name=models.CharField(max_length=200)
    training_provider=models.CharField(max_length=200)
    training_location=models.CharField(max_length=200,choices=allTrainingLocation)
    duration=models.DurationField()
    start_date=models.DateField()
    training_date=models.ManyToManyField('Department',max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name
    

class employeeSkill(models.Model):

    Knowledge_level=[
        ('Advanced','Advanced'),
        ('Midlevel','Midlevel'),
        ('Beginer','Beginer'),
    ]
    employee=models.ForeignKey(EmployeeDetails,on_delete=models.CASCADE)
    skills_obtained=models.ForeignKey(Skills,on_delete=models.CASCADE)
    proficiency_level=models.CharField(max_length=200,choices=Knowledge_level)

    def __str__(self):
        return f"{self.employee}-{self.skills_obtained}"
    
