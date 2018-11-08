from django.db import models

# Create your models here.
#
# genders = (
#     ('m', 'Male'),
#     ('f', 'Female'),
#     ('o', 'Others'),
# )
#
# courses = (
#     ('btech', 'BTech'),
#     ('mtech', 'MTech'),
# )
#
# branches = (
#     ('me', 'Mechanical'),
#     ('cse', 'Computer Science'),
#     ('it', 'Information Technology'),
#     ('ece', 'Electronics And Communication'),
#     ('eee', 'Electrical And Electronics'),
# )
#
# domains = (
#     ('me', 'Mechanical'),
#     ('cse', 'Computer Science & IT'),
#     ('ece', 'Electronics And Communication'),
#     ('eee', 'Electrical And Electronics'),
#     ('oth', 'Others'),
# )
#
# status = (
#     ('comp', 'Completed'),
#     ('purs', 'Pursuing'),
#     ('noto', 'Not Opted'),
# )
#
# class Placement(models.Model):
#     name = models.CharField(max_length = 50)
#     reg = models.CharField(max_length = 50)
#     email = models.EmailField(max_length=200)
#     gender = models.CharField(max_length=20, choices = genders)
#     course = models.CharField(max_length=20, choices = courses)
#     number = models.CharField(max_length=20)
#     branch = models.CharField(max_length=20, choices = branches)
#     grad = models.DecimalField(max_digits=8)
#     org = models.CharField(max_length=250)
#     desig = models.CharField(max_length=250)
#     domain = models.CharField(max_length=50,choices = domains)
#     degree = models.CharField(max_length = 100)
#     custatus = models.CharField(max_length=50, choices = status)
#     univname = models.CharField(max_length=100)
#     texta = models.TextField()
#     textb = models.TextField()
#     textc = models.TextField()
#     textd = models.TextField()
#     texte = models.TextField()
#     textf = models.TextField()
#     textg = models.TextField()
#
#     def __str__(self):
#         return 'Name: %s Number: %s EMail: %s Course: %s Branch: %s Organisation: %s Designation: %s Graduation: %s' % ( self.name,
#                                                                                                                     self.number,
#                                                                                                                     self.email,
#                                                                                                                     self.course,
#                                                                                                                     self.branch,
#                                                                                                                     self.org,
#                                                                                                                     self.desig,
#                                                                                                                     self.grad,
#                                                                                                                 )
#
#
#
#
#
