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
    reg = models.CharField("Registration Number",max_length = 50, null=True)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=20, choices = genders, null=True)
    course = models.CharField(max_length=20, choices = courses)
    number = models.CharField(max_length=20)
    branch = models.CharField(max_length=20, choices = branches)
    grad = models.CharField("Graduation Year",max_length=8)
    org = models.CharField("Current Organization",max_length=250)
    desig = models.CharField("Current Designation",max_length=250)
    domain = models.CharField(max_length=50,choices = domains, null=True)
    degree = models.CharField(max_length = 100, null=True)
    custatus = models.CharField("Current Status",max_length=50, choices = status, null=True)
    univname = models.CharField("University Name",max_length=100, null=True)
    choicea = models.BooleanField("Do you think that has helped in building your career?",default=False)
    choiceb = models.BooleanField("4.Will you be interested in mentoring some of our students in your domain?",default=False)
    choicec = models.BooleanField("	5.Would you be interested in visiting our campus for a technical talk to our present students?",default=False)
    choiced = models.BooleanField("6.Are you aware of any companies in your domain which are looking for freshers?",default=False)
    choicee = models.BooleanField("7.Are you in a position(in your company)to help the recruitments in our campus?",default=False)
    texta = models.TextField("1.What did you do in the year immediately after graduating?",null=True)
    textb = models.TextField("2.What are the skills/tools fresher must acquaint with before entering your field?",null=True)
    textc = models.TextField("3.What are the topics a fresher must prepare for an interview in your domain?",null=True)
    textd = models.TextField("Can you provide the company/HR details?",null=True)
    texte = models.TextField("Will you recomment our institution to the company?",null=True)
    textf = models.TextField(" Can you suggest how we can approach your HR?",null=True)
    textg = models.TextField("Can you share us your HR contact details?",null=True)

    # def __str__(self):
    #     return 'Name: %s Contact Number: %s EMail: %s Course: %s Branch: %s Organisation: %s Designation: %s Graduation: %s Domain: %s Degree: %s Current Status: %s Univaersity Name: %s Registration Number: %s Gender: %s TextA: %s TextB: %s TextC: %s TextD: %s TextE: %s TextF: %s TextG: %s' % ( self.name,
    #                                                                                                                 self.number,
    #                                                                                                                 self.email,
    #                                                                                                                 self.course,
    #                                                                                                                 self.branch,
    #                                                                                                                 self.org,
    #                                                                                                                 self.desig,
    #                                                                                                                 self.grad,
    #                                                                                                                 self.domain,
    #                                                                                                                 self.degree,
    #                                                                                                                 self.custatus,
    #                                                                                                                 self.univname,
    #                                                                                                                 self.reg,
    #                                                                                                                 self.gender,
    #                                                                                                                 self.texta,
    #                                                                                                                 self.textb,
    #                                                                                                                 self.textc,
    #                                                                                                                 self.textd,
    #                                                                                                                 self.texte,
    #                                                                                                                 self.textf,
    #                                                                                                                 self.texte,
    #                                                                                                                 self.textg,
    #                                                                                                             )
