from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from st_mn_sys_app.models import nguoiDung, nhanVien, giaoVien, monHoc, lop, hocSinh, diem

# Create your views here.
def teacher_page(request):
    return render(request,"teacher_templates/teacher_page.html")
def add_student(request):
    lophoc = lop.objects.all()
    return render(request,"teacher_templates/add_student.html",{"lop":lophoc})
def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        hovaten = request.POST.get("hovaten")
        ngaysinh = request.POST.get("ngaysinh")
        gioitinh = request.POST.get("gioitinh")
        diachi = request.POST.get("diachi")
        lophoc = request.POST.get("lophoc")
        tenbo = request.POST.get("tenbo")
        sdtbo = request.POST.get("sdtbo")
        emailbo = request.POST.get("emailbo")
        tenme = request.POST.get("tenme")
        sdtme = request.POST.get("sdtme")
        emailme = request.POST.get("emailme")
    try:
        hocsinh = hocSinh.objects.create(hovaten=hovaten,ngaysinh=ngaysinh,gioitinh=gioitinh,diachi=diachi,tenbo=tenbo,sdtbo=sdtbo,emailbo=emailbo,tenme=tenme,sdtme=sdtme,emailme=emailme) 
        lop_obj = lop.objects.get(malop=lophoc)
        hocsinh.malop= lop_obj
        hocsinh.save()
        
        messages.success(request,"Thêm học sinh thành công")
        return HttpResponseRedirect('/add_student')
    except:
        messages.error(request,"Không thành công, vui lòng kiểm tra lại")
        return HttpResponseRedirect('/add_student')
def manage_student(request):
    students= hocSinh.objects.all()
    return render(request, "teacher_templates/manage_student.html",{"students":students})
def edit_student(request,student_id):
    students= hocSinh.objects.get(mahs = student_id)
    lophoc = lop.objects.all()
    return render(request,"teacher_templates/edit_student.html",{"students":students, "lop":lophoc})
def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        mahs=request.POST.get("mahs")
        hovaten=request.POST.get("hovaten")
        ngaysinh=request.POST.get("ngaysinh")
        gioitinh=request.POST.get("gioitinh")
        diachi=request.POST.get("diachi")
        tenbo=request.POST.get("tenbo")
        emailbo=request.POST.get("emailbo")
        sdtbo=request.POST.get("sdtbo")
        tenme=request.POST.get("tenme")
        emailme=request.POST.get("emailme")
        sdtme=request.POST.get("sdtme")
        lophoc=request.POST.get("lophoc")
    try:
        hocsinh = hocSinh.objects.get(mahs = mahs)
        hocsinh.hovaten = hovaten
        hocsinh.ngaysinh = ngaysinh
        hocsinh.gioitinh = gioitinh
        hocsinh.diachi = diachi
        hocsinh.tenbo = tenbo
        hocsinh.emailbo = emailbo
        hocsinh.sdtbo = sdtbo
        hocsinh.tenme = tenme
        hocsinh.emailme = emailme
        hocsinh.sdtme = sdtme
    
        lop_obj=lop.objects.get(malop = lophoc)
        hocsinh.malop=lop_obj
        hocsinh.save() 
        
        messages.success(request,"Chỉnh sửa học sinh thành công")
        return HttpResponseRedirect("/edit_student/" + str(hocsinh.mahs))
    except:
        messages.error(request,"Chỉnh sửa học sinh không thành công")
        return HttpResponseRedirect("/edit_student/" + str(hocsinh.mahs))
def delete_student(request,student_id):
    students = hocSinh.objects.get(mahs = student_id)
    return render(request,"teacher_templates/delete_student.html",{"students":students})
def delete_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        mahs = request.POST.get("mahs")
    try:
        hocsinh = hocSinh.objects.get(mahs = mahs)
        hocsinh.delete()
        return HttpResponseRedirect("/manage_student")
    except:
        return HttpResponseRedirect("/manage_student")
        
def add_mark_student(request,student_id):
    students = hocSinh.objects.get(mahs = student_id)
    monhoc = monHoc.objects.all()
    return render(request,"teacher_templates/add_mark.html",{"students":students, "monHoc":monhoc})
def add_mark_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        mahs = request.POST.get("mahs")
        diem_hs = request.POST.get("diem")
        monhoc = request.POST.get("monhoc")
        mucdatduoc = request.POST.get("mucdatduoc")
    try:
        hocsinh = hocSinh.objects.get(mahs = mahs)
        monhoc_moi = monHoc.objects.get(mamonhoc = monhoc)
        diem_moi = diem.objects.create(diem = diem_hs,mucdatduoc = mucdatduoc)
        diem_moi.mahs = hocsinh
        diem_moi.mamonhoc = monhoc_moi
        diem_moi.save()

        messages.success(request,"Thêm điểm thành công")
        return HttpResponseRedirect('/add_mark_student/'+ str(mahs))
    except:
        messages.error(request,"Không thành công, vui lòng kiểm tra lại")
        return HttpResponseRedirect('/add_mark_student/' + str(mahs))
        
def check_mark_student(request):
    pass