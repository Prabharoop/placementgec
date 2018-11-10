from django.db import models

# Create your models here.
#
genders = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Others'),
)

courses = (
    ('btech', 'BTech'),
    ('mtech', 'MTech'),
)

branches = (
    ('me', 'Mechanical'),
    ('cse', 'Computer Science'),
    ('it', 'Information Technology'),
    ('ece', 'Electronics And Communication'),
    ('eee', 'Electrical And Electronics'),
)

domains = (
    ('me', 'Mechanical'),
    ('cse', 'Computer Science & IT'),
    ('ece', 'Electronics And Communication'),
    ('eee', 'Electrical And Electronics'),
    ('oth', 'Others'),
)

status = (
    ('comp', 'Completed'),
    ('purs', 'Pursuing'),
    ('noto', 'Not Opted'),
)

class Placement(models.Model):
    name = models.CharField(max_length = 50)
    reg = models.CharField("Registration Number",max_length = 50)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=20, choices = genders)
    course = models.CharField(max_length=20, choices = courses)
    number = models.CharField(max_length=20)
    branch = models.CharField(max_length=20, choices = branches)
    grad = models.CharField("Graduation Year",max_length=8)
    org = models.CharField("Current Organization",max_length=250)
    desig = models.CharField("Current Designation",max_length=250)
    domain = models.CharField(max_length=50,choices = domains)
    degree = models.CharField(max_length = 100)
    custatus = models.CharField("Current Status",max_length=50, choices = status)
    univname = models.CharField("University Name",max_length=100)
    texta = models.TextField(null=True)
    textb = models.TextField(null=True)
    textc = models.TextField(null=True)
    textd = models.TextField(null=True)
    texte = models.TextField(null=True)
    textf = models.TextField(null=True)
    textg = models.TextField(null=True)

    def __str__(self):
        return 'Name: %s Contact Number: %s EMail: %s Course: %s Branch: %s Organisation: %s Designation: %s Graduation: %s' % ( self.name,
                                                                                                                    self.number,
                                                                                                                    self.email,
                                                                                                                    self.course,
                                                                                                                    self.branch,
                                                                                                                    self.org,
                                                                                                                    self.desig,
                                                                                                                    self.grad,
                                                                                                                )
