from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from st_mn_sys_app.models import nguoiDung, nhanVien, giaoVien, monHoc, lop

# Create your views here.
def admin_page(request):
    return render(request, "admin_templates/admin_page.html")
def add_staff(request):
    return render(request, "admin_templates/add_staff.html")
def add_staff_save(request):
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
        vitri=request.POST.get("vitri")
    try:
        nhanvien_new = nguoiDung.objects.create_user(hovaten=hovaten,username=username,password=password,ngaysinh=ngaysinh,gioitinh=gioitinh,diachi=diachi,cccd=cccd,email=email,sdt=sdt,ngaybatdau=ngaybatdau,user_type=2)
        nhanvien_new.nhanvien.vitri = vitri
        nhanvien_new.save()
        messages.success(request,"Thành công")
        return HttpResponseRedirect("/add_staff")
    except:
        messages.error(request,"Không thành công, vui lòng kiểm tra lại")
        return HttpResponseRedirect("/add_staff")
def manage_staff(request):
    staffs=nhanVien.objects.all()
    return render(request, "admin_templates/manage_staff.html",{"staffs":staffs})        
def edit_staff(request,staff_id):
    staffs = nhanVien.objects.get(admin_id=staff_id)
    return render(request,"admin_templates/edit_staff.html",{"staffs":staffs})
def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        mand = request.POST.get("mand")
        username = request.POST.get("username")
        hovaten = request.POST.get("hovaten")
        vitri = request.POST.get("vitri")
        ngaysinh = request.POST.get("ngaysinh")
        gioitinh=request.POST.get("gioitinh")
        diachi=request.POST.get("diachi")
        cccd=request.POST.get("cccd")
        email=request.POST.get("email")
        sdt=request.POST.get("sdt")
        ngaybatdau=request.POST.get("ngaybatdau")
        vitri=request.POST.get("vitri")
    try:    
        staff=nguoiDung.objects.get(mand=mand)
        staff.username = username
        staff.hovaten=hovaten
        staff.ngaysinh = ngaysinh
        staff.gioitinh=gioitinh
        staff.diachi=diachi
        staff.cccd=cccd
        staff.email=email
        staff.ngaybatdau = ngaybatdau
        staff.sdt=sdt
        staff.save()
            
        staff_model=nhanVien.objects.get(admin=mand)
        staff_model.vitri=vitri
        staff_model.save()

        messages.success(request,"Chỉnh sửa nhân viên thành công")
        return HttpResponseRedirect("/edit_staff/" + str(staff.mand))
    except:
        messages.error(request,"Chỉnh sửa nhân viên không thành công")
        return HttpResponseRedirect("/edit_staff/" + str(staff.mand))
def delete_staff(request,staff_id):
    staffs = nhanVien.objects.get(admin_id=staff_id)
    return render(request,"admin_templates/delete_staff.html",{"staffs":staffs})
def delete_staff_save(request):
        if request.method!="POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")
        else:
            mand=request.POST.get("mand")
            try:
                staff=nguoiDung.objects.get(mand=mand)
                staff.delete()
                return HttpResponseRedirect("/manage_staff")
            except:
                return HttpResponseRedirect("/manage_staff")    
    
def add_courses(request):
    return render(request,"admin_templates/add_courses.html")
def add_courses_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        tenmonhoc = request.POST.get("tenmonhoc")
        sotiet = request.POST.get("sotiet")
    try:
        monhoc_new = monHoc(tenmonhoc = tenmonhoc, sotiet = sotiet)
        monhoc_new.save()
        messages.success(request,"Thêm môn học thành công")
        return HttpResponseRedirect('/add_courses')
    except:
        messages.error(request,"Không thành công, vui lòng kiểm tra lại")
        return HttpResponseRedirect('/add_courses')
def manage_courses(request):
    courses = monHoc.objects.all()
    return render(request,"admin_templates/manage_courses.html",{"courses":courses})
def add_classes(request):
    return render(request, "admin_templates/add_classes.html")
def add_classes_save(request):
    if(request.method != "POST"):
        return HttpResponse("Method Not Allowed")
    else:
        tenlop = request.POST.get("tenlop")
    try:
        lop_new = lop(tenlop = tenlop)
        lop_new.save()
        messages.success(request,"Thêm lớp thành công")
        return HttpResponseRedirect('/add_classes')
    except:
        messages.error(request,"Thêm lớp không thành công, vui lòng kiểm tra lại")
        return HttpResponseRedirect('/add_classes')
def manage_classes(request):
    classes = lop.objects.all()
    return render(request, "admin_templates/manage_classes.html",{"classes":classes})
def add_teachers(request):
    monhoc= monHoc.objects.all()
    lophoc = lop.objects.all()
    return render(request, "admin_templates/add_teachers.html",{"monHoc":monhoc, "lop":lophoc})

def add_teachers_save(request):
    if request.method != "POST":
       return HttpResponse("Method Not Allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        hovaten = request.POST.get("hovaten")
        ngaysinh = request.POST.get("ngaysinh")
        gioitinh = request.POST.get("gioitinh")
        diachi = request.POST.get("diachi")
        cccd = request.POST.get("cccd")
        email = request.POST.get("email")
        sdt = request.POST.get("sdt")
        ngaybatdau = request.POST.get("ngaybatdau")
        logpd = request.POST.get("lopgd")
        mongd = request.POST.get("mongd")
    try:
        nguoidung = nguoiDung.objects.create_user(username=username,password=password,hovaten=hovaten,ngaysinh=ngaysinh,gioitinh=gioitinh,diachi=diachi,cccd=cccd,email=email,sdt=sdt,ngaybatdau=ngaybatdau, user_type=3)
        monhoc_obj = monHoc.objects.get(mamonhoc=mongd)
        nguoidung.giaovien.mamonhoc = monhoc_obj
        lophoc_obj = lop.objects.get(malop = logpd)
        nguoidung.giaovien.malop = lophoc_obj
        nguoidung.save()
        
        messages.success(request,"Thêm giáo viên thành công")
        return HttpResponseRedirect('/add_teachers')
    except:
        messages.error(request,"Không thành công, vui lòng kiểm tra lại")
        return HttpResponseRedirect('/add_teachers')
        
        
       
def manage_teachers(request):
    teachers = giaoVien.objects.all()
    return render(request, "admin_templates/manage_teachers.html",{"teachers":teachers})
def edit_teacher(request,teacher_id):
    teachers = giaoVien.objects.get(admin=teacher_id)
    monhoc= monHoc.objects.all()
    lophoc = lop.objects.all()
    return render(request,"admin_templates/edit_teacher.html",{"teachers":teachers, "monHoc":monhoc, "lop":lophoc})
def edit_teacher_save(request):
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
        return HttpResponseRedirect("/edit_teacher/" + str(nguoidung.mand))
    except:
        messages.error(request,"Chỉnh sửa giáo viên không thành công")
        return HttpResponseRedirect("/edit_teacher/" + str(nguoidung.mand))
def delete_teacher(request,teacher_id):
    teachers = giaoVien.objects.get(admin=teacher_id)
    return render(request,"admin_templates/delete_teachers.html",{"teachers":teachers})
def delete_teacher_save(request):
        if request.method!="POST":
            return HttpResponse("Method Not Allowed")
        else:
            mand=request.POST.get("mand")
        try:
            teacher=nguoiDung.objects.get(mand=mand)
            teacher.delete()
            return HttpResponseRedirect("/manage_teachers")
        except:
            return HttpResponseRedirect("/manage_teachers")    
def edit_course(request,course_id):
    courses = monHoc.objects.get(mamonhoc = course_id)
    return render(request,"admin_templates/edit_course.html", {"courses":courses})
def edit_course_save(request):
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
        return HttpResponseRedirect("/edit_course/" + str(course.mamonhoc))
    except:
        messages.error(request,"Chỉnh sửa môn học không thành công")
        return HttpResponseRedirect("/edit_course/" + str(course.mamonhoc))
def delete_course(request,course_id):
    courses = monHoc.objects.get(mamonhoc = course_id)
    return render(request,"admin_templates/delete_course.html",{"courses":courses})
def delete_course_save(request):
    if request.method != "POST":
       return HttpResponse("Method Not Allowed")
    else:
        mamonhoc = request.POST.get("mamonhoc")
    try:
        course = monHoc.objects.get(mamonhoc = mamonhoc)
        course.delete()
        return HttpResponseRedirect("/manage_courses")
    except:
        return HttpResponseRedirect("/manage_courses")
def edit_class(request,class_id):
    classes = lop.objects.get(malop = class_id)
    return render(request,"admin_templates/edit_class.html",{"classes":classes})
def edit_class_save(request):
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
        return HttpResponseRedirect("/edit_class/" + str(classes.malop))
    except:
        messages.error(request,"Chỉnh sửa lớp học không thành công")
        return HttpResponseRedirect("/edit_class/" + str(classes.malop))
        
def delete_class(request,class_id):
    classes = lop.objects.get(malop = class_id)
    return render(request,"admin_templates/delete_class.html",{"classes":classes})
def delete_class_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        malop = request.POST.get("malop")
    try:
        classes = lop.objects.get(malop = malop)
        classes.delete()
        return HttpResponseRedirect("/manage_classes")
    except:
        return HttpResponseRedirect("/manage_classes")