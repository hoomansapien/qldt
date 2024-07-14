from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from st_mn_sys_app.models import nguoiDung, nhanVien, giaoVien, monHoc, lop

# Create your views here.
def staff_page(request):
    return render(request,"staff_templates/staff_page.html")
def staff_add_courses(request):
    return render(request,"staff_templates/add_courses.html")
def staff_add_courses_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        tenmonhoc = request.POST.get("tenmonhoc")
        sotiet = request.POST.get("sotiet")
    try:
        monhoc_new = monHoc(tenmonhoc = tenmonhoc, sotiet = sotiet)
        monhoc_new.save()
        messages.success(request,"Thêm môn học thành công")
        return HttpResponseRedirect('/staff_add_courses')
    except:
        messages.error(request,"Không thành công, vui lòng kiểm tra lại")
        return HttpResponseRedirect('/staff_add_courses')
def staff_manage_courses(request):
    courses = monHoc.objects.all()
    return render(request,"staff_templates/manage_courses.html",{"courses":courses})
def staff_add_classes(request):
    return render(request, "staff_templates/add_classes.html")
def staff_add_classes_save(request):
    if(request.method != "POST"):
        return HttpResponse("Method Not Allowed")
    else:
        tenlop = request.POST.get("tenlop")
    try:
        lop_new = lop(tenlop = tenlop)
        lop_new.save()
        messages.success(request,"Thêm lớp thành công")
        return HttpResponseRedirect('/staff_add_classes')
    except:
        messages.error(request,"Thêm lớp không thành công, vui lòng kiểm tra lại")
        return HttpResponseRedirect('/staff_add_classes')
def staff_manage_classes(request):
    classes = lop.objects.all()
    return render(request, "staff_templates/manage_classes.html",{"classes":classes})
def staff_add_teachers(request):
    monhoc= monHoc.objects.all()
    lophoc = lop.objects.all()
    return render(request, "staff_templates/add_teachers.html",{"monHoc":monhoc, "lop":lophoc})

def staff_add_teachers_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        hovaten=request.POST.get("hovaten")
        username=request.POST.get("username")
        password=request.POST.get("password")
        ngaysinh=request.POST.get("ngaysinh")
        gioitinh=request.POST.get("gioitinh")
        diachi=request.POST.get("diachi")
        cccd=request.POST.get("cccd")
        email=request.POST.get("email")
        sdt=request.POST.get("sdt")
        ngaybatdau=request.POST.get("ngaybatdau")
        mongd=request.POST.get("mongd")
        lopgd=request.POST.get("lopgd")    
    try:
        giaovien_new = nguoiDung.objects.create_user(hovaten=hovaten,username=username,password=password,ngaysinh=ngaysinh,gioitinh=gioitinh,diachi=diachi,cccd=cccd,email=email,sdt=sdt,ngaybatdau=ngaybatdau,user_type=3)
        monhoc_obj=monHoc.objects.get(mamonhoc=mongd)
        giaovien_new.giaovien.mongd=monhoc_obj
        lop_obj=lop.objects.get(malop=lopgd)
        giaovien_new.giaovien.lopgd=lop_obj
        giaovien_new.save()
        messages.success(request,"Thành công")
        return HttpResponseRedirect("/staff_add_teachers")
    except:
        messages.error(request,"Không thành công, vui lòng kiểm tra lại")
        return HttpResponseRedirect("/staff_add_teachers")  
def staff_manage_teachers(request):
    teachers = giaoVien.objects.all()
    return render(request, "staff_templates/manage_teachers.html",{"teachers":teachers})
def staff_edit_teacher(request,teacher_id):
    teachers = giaoVien.objects.get(admin=teacher_id)
    monhoc= monHoc.objects.all()
    lophoc = lop.objects.all()
    return render(request,"staff_templates/edit_teacher.html",{"teachers":teachers, "monHoc":monhoc, "lop":lophoc})
def staff_edit_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        mand=request.POST.get("mand")
        hovaten=request.POST.get("hovaten")
        username=request.POST.get("username")
        ngaysinh=request.POST.get("ngaysinh")
        gioitinh=request.POST.get("gioitinh")
        diachi=request.POST.get("diachi")
        cccd=request.POST.get("cccd")
        email=request.POST.get("email")
        sdt=request.POST.get("sdt")
        ngaybatdau=request.POST.get("ngaybatdau")
        mongd=request.POST.get("mongd")
        lopgd=request.POST.get("lopgd")
    try:
        nguoidung = nguoiDung.objects.get(mand=mand)
        nguoidung.username = username
        nguoidung.hovaten = hovaten
        nguoidung.ngaysinh = ngaysinh
        nguoidung.gioitinh = gioitinh
        nguoidung.diachi = diachi
        nguoidung.cccd = cccd
        nguoidung.email = email
        nguoidung.sdt = sdt
        nguoidung.ngaybatdau = ngaybatdau
        nguoidung.save()
        
        teacher = giaoVien.objects.get(admin = mand)
        monhoc_obj=monHoc.objects.get(mamonhoc = mongd)
        teacher.mongd=monhoc_obj
        lop_obj=lop.objects.get(malop = lopgd)
        teacher.lopgd=lop_obj
        teacher.save() 
        
        messages.success(request,"Chỉnh sửa giáo viên thành công")
        return HttpResponseRedirect("/staff_edit_teacher/" + str(nguoidung.mand))
    except:
        messages.error(request,"Chỉnh sửa giáo viên không thành công")
        return HttpResponseRedirect("/staff_edit_teacher/" + str(nguoidung.mand))
def staff_delete_teacher(request,teacher_id):
    teachers = giaoVien.objects.get(admin=teacher_id)
    return render(request,"staff_templates/delete_teachers.html",{"teachers":teachers})
def staff_delete_teacher_save(request):
        if request.method!="POST":
            return HttpResponse("Method Not Allowed")
        else:
            mand=request.POST.get("mand")
        try:
            teacher=nguoiDung.objects.get(mand=mand)
            teacher.delete()
            return HttpResponseRedirect("/staff_manage_teachers")
        except:
            return HttpResponseRedirect("/staff_manage_teachers")    
def staff_edit_course(request,course_id):
    courses = monHoc.objects.get(mamonhoc = course_id)
    return render(request,"staff_templates/edit_course.html", {"courses":courses})
def staff_edit_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        mamonhoc = request.POST.get("mamonhoc")
        tenmonhoc = request.POST.get("tenmonhoc")
        sotiet = request.POST.get("sotiet")
    try:
        course = monHoc.objects.get(mamonhoc = mamonhoc)
        course.tenmonhoc = tenmonhoc
        course.sotiet = sotiet
        course.save()
        
        messages.success(request,"Chỉnh sửa môn học thành công")
        return HttpResponseRedirect("/staff_edit_course/" + str(course.mamonhoc))
    except:
        messages.error(request,"Chỉnh sửa môn học không thành công")
        return HttpResponseRedirect("/staff_edit_course/" + str(course.mamonhoc))
def staff_delete_course(request,course_id):
    courses = monHoc.objects.get(mamonhoc = course_id)
    return render(request,"staff_templates/delete_course.html",{"courses":courses})
def staff_delete_course_save(request):
    if request.method != "POST":
       return HttpResponse("Method Not Allowed")
    else:
        mamonhoc = request.POST.get("mamonhoc")
    try:
        course = monHoc.objects.get(mamonhoc = mamonhoc)
        course.delete()
        return HttpResponseRedirect("/staff_manage_courses")
    except:
        return HttpResponseRedirect("/staff_manage_courses")
def staff_edit_class(request,class_id):
    classes = lop.objects.get(malop = class_id)
    return render(request,"staff_templates/edit_class.html",{"classes":classes})
def staff_edit_class_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        malop = request.POST.get("malop")
        tenlop = request.POST.get("tenlop")
    try:
        classes = lop.objects.get(malop = malop)
        classes.tenlop = tenlop
        classes.save ()
        
        messages.success(request,"Chỉnh sửa lớp học thành công")
        return HttpResponseRedirect("/staff_edit_class/" + str(classes.malop))
    except:
        messages.error(request,"Chỉnh sửa lớp học không thành công")
        return HttpResponseRedirect("/staff_edit_class/" + str(classes.malop))
        
def staff_delete_class(request,class_id):
    classes = lop.objects.get(malop = class_id)
    return render(request,"staff_templates/delete_class.html",{"classes":classes})
def staff_delete_class_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        malop = request.POST.get("malop")
    try:
        classes = lop.objects.get(malop = malop)
        classes.delete()
        return HttpResponseRedirect("/staff_manage_classes")
    except:
        return HttpResponseRedirect("/staff_manage_classes")