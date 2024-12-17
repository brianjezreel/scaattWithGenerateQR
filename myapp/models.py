from django.db import models

class Role(models.Model):
    id = models.AutoField(primary_key=True) 
    role_name = models.CharField(max_length=50)
    objects = models.Manager()

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    device = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    objects = models.Manager()

class QrCode(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    code_value = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    objects = models.Manager()

class Scan(models.Model):
    id = models.AutoField(primary_key=True)
    #qr_code = models.ForeignKey(QrCode, on_delete=models.CASCADE)
    #user = models.ForeignKey(Users, on_delete=models.CASCADE)
    scan = models.BooleanField(default=False)
    scan_time = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    scan = models.ForeignKey(Scan, on_delete=models.SET_NULL, null=True, blank=True)
    objects = models.Manager()