from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Role, Users, Courses, Scan, QrCode
from django.contrib import messages
from django.utils import timezone
from .utils import generate_qr_code

def admin_home(request):
    return render(request, "hod_template/home_content.html")

def add_student(request):
    return render(request, "hod_template/add_student_template.html")

def add_student_save(request):
    if request.method != "POST":
        messages.error(request, "Failed")
        return HttpResponseRedirect("/add_student")
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        device = request.POST.get("device")
        password = request.POST.get("password")
        role_name = request.POST.get("role")
        user = Users(name=name, email=email, password=password, device=device, role=role_name)
        user.save()
        role_name = Role(role_name=role_name)
        role_name.save()
        messages.success(request, "Success")
        return HttpResponseRedirect("/add_student")

def add_course(request):
    return render(request, "hod_template/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Failed")
        return HttpResponseRedirect("/add_course")
    else:
        course = request.POST.get("course")
        course_model = Courses(course_name=course)
        course_model.save()
        messages.success(request, "Success")
        return HttpResponseRedirect("/add_course")

def scanner(request):
    return render(request, "hod_template/scanner.html")

def viewusers(request):
    user = Users.objects.all()
    return render(request, "viewusers.html", {'userdata': user})

def viewcourses(request):
    courses = Courses.objects.all()
    return render(request, "viewcourses.html", {'userdata': courses})

def deleteprofile(request, id):
    us = Users.objects.get(id=id)
    us.delete()
    return redirect("/viewusers")

def deletecourse(request, id):
    us = Courses.objects.get(id=id)
    us.delete()
    return redirect("/viewcourses")

def editprofile(request, id):
    user = Users.objects.get(id=id)
    return render(request, "editprofile.html", {'us':user})

def updateprofile(request, id):
    newname = request.POST['name']
    newemail = request.POST['email']
    newpassword = request.POST['password']
    newdevice = request.POST['device']
    us = Users.objects.get(id=id)
    us.name = newname
    us.email = newemail
    us.password = newpassword
    us.device = newdevice
    us.save()
    return redirect("/viewusers")

def createqrcode(request, course_id):
    course = Courses.objects.get(id=course_id)
    qr_code_value = course.course_name 

    existing_qr_code = QrCode.objects.filter(code_value=qr_code_value).first()
    
    if existing_qr_code:
        return redirect('viewcourses')

    qr_code_image = generate_qr_code(qr_code_value)
    
    qr_code = QrCode(course=course, code_value=qr_code_value)
    qr_code.image.save(f"{qr_code_value}_qr.png", qr_code_image)
    qr_code.save()
    
    return redirect('viewcourses')

def showqrcode(request, qr_code_id):
    qr_code = get_object_or_404(QrCode, id=qr_code_id)
    return render(request, "showqrcode.html", {'qr_code': qr_code})
