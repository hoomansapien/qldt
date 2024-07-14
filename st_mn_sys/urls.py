"""
URL configuration for st_mn_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from st_mn_sys_app import views, adminviews, staffviews, teacherviews
from st_mn_sys import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo',views.showDemo),
    path('',views.showLogin),
    path('logout',views.logout_user,name='logout'),
    path('doLogin',views.doLogin),
    path('admin_page',adminviews.admin_page,name='admin_page'),
    path('staff_page',staffviews.staff_page,name='staff_page'),
    path('teacher_page',teacherviews.teacher_page,name='admin_page'),
    
    path('add_student',teacherviews.add_student,name='add_student'),
    path('add_student_save',teacherviews.add_student_save,name='add_student_save'),
    path('manage_student',teacherviews.manage_student,name='manage_student'),
    path('edit_student/<str:student_id>',teacherviews.edit_student,name="edit_student"),
    path('edit_student_save',teacherviews.edit_student_save,name="edit_student_save"),
    path('delete_student/<str:student_id>',teacherviews.delete_student,name="delete_student"),
    path('delete_student_save',teacherviews.delete_student_save,name="delete_student_save"),
    path('add_mark_student/<str:student_id>',teacherviews.add_mark_student,name="add_mark_student"),
    path('add_mark_student_save',teacherviews.add_mark_student_save,name="add_mark_student_save"),
    
    path('staff_add_courses',staffviews.staff_add_courses,name='staff_add_courses'),
    path('staff_add_courses_save',staffviews.staff_add_courses_save,name='staff_add_courses_save'),
    path('staff_manage_courses',staffviews.staff_manage_courses,name="staff_manage_courses"),
    path('staff_add_classes',staffviews.staff_add_classes,name='staff_add_classes'),
    path('staff_manage_classes',staffviews.staff_manage_classes,name="staff_manage_classes"),
    path('staff_add_classes_save',staffviews.staff_add_classes_save,name='staff_add_classes_save'),
    path('staff_add_teachers',staffviews.staff_add_teachers,name='staff_add_teachers'),
    path('staff_add_teachers_save',staffviews.staff_add_teachers_save,name="staff_add_teachers_save"),
    path('staff_edit_teacher/<str:teacher_id>',staffviews.staff_edit_teacher,name='staff_edit_teacher'),
    path('staff_edit_teacher_save',staffviews.staff_edit_teacher_save,name='staff_edit_teacher_save'),
    path('staff_delete_teacher/<str:teacher_id>',staffviews.staff_delete_teacher,name='staff_delete_teacher'),
    path('staff_delete_teacher_save',staffviews.staff_delete_teacher_save,name='staff_delete_teacher_save'),
    path('staff_manage_teachers',staffviews.staff_manage_teachers,name="staff_manage_teachers"),
    path('staff_edit_course/<str:course_id>',staffviews.staff_edit_course,name='staff_edit_course'),
    path('staff_edit_course_save',staffviews.staff_edit_course_save,name='staff_edit_course_save'),
    path('staff_delete_course/<str:course_id>',staffviews.staff_delete_course,name='staff_delete_course'),
    path('staff_delete_course_save',staffviews.staff_delete_course_save,name='staff_delete_course_save'),
    path('staff_edit_class/<str:class_id>',staffviews.staff_edit_class,name='staff_edit_class'),
    path('staff_edit_class_save',staffviews.staff_edit_class_save,name='staff_edit_class_save'),
    path('staff_delete_class/<str:class_id>',staffviews.staff_delete_class,name='staff_delete_class'),
    path('staff_delete_class_save',staffviews.staff_delete_class_save,name='staff_delete_class_save'),
    
    path('add_staff',adminviews.add_staff,name='add_staff'),
    path('add_staff_save',adminviews.add_staff_save,name='add_staff_save'),
    path('manage_staff',adminviews.manage_staff,name='manage_staff'),
    path('edit_staff/<str:staff_id>',adminviews.edit_staff,name='edit_staff'),
    path('edit_staff_save',adminviews.edit_staff_save,name='edit_staff_save'),
    path('delete_staff/<str:staff_id>',adminviews.delete_staff,name='delete_staff'),
    path('delete_staff_save',adminviews.delete_staff_save,name='delete_staff_save'),
    path('add_courses',adminviews.add_courses,name='add_courses'),
    path('add_courses_save',adminviews.add_courses_save,name='add_courses_save'),
    path('manage_courses',adminviews.manage_courses,name="manage_courses"),
    path('add_classes',adminviews.add_classes,name='add_classes'),
    path('manage_classes',adminviews.manage_classes,name="manage_classes"),
    path('add_classes_save',adminviews.add_classes_save,name='add_classes_save'),
    path('add_teachers',adminviews.add_teachers,name='add_teachers'),
    path('add_teachers_save',adminviews.add_teachers_save,name="add_teachers_save"),
    path('edit_teacher/<str:teacher_id>',adminviews.edit_teacher,name='edit_teacher'),
    path('edit_teacher_save',adminviews.edit_teacher_save,name='edit_teacher_save'),
    path('delete_teacher/<str:teacher_id>',adminviews.delete_teacher,name='delete_teacher'),
    path('delete_teacher_save',adminviews.delete_teacher_save,name='delete_teacher_save'),
    path('manage_teachers',adminviews.manage_teachers,name="manage_teachers"),
    path('edit_course/<str:course_id>',adminviews.edit_course,name='edit_course'),
    path('edit_course_save',adminviews.edit_course_save,name='edit_course_save'),
    path('delete_course/<str:course_id>',adminviews.delete_course,name='delete_course'),
    path('delete_course_save',adminviews.delete_course_save,name='delete_course_save'),
    path('edit_class/<str:class_id>',adminviews.edit_class,name='edit_class'),
    path('edit_class_save',adminviews.edit_class_save,name='edit_class_save'),
    path('delete_class/<str:class_id>',adminviews.delete_class,name='delete_class'),
    path('delete_class_save',adminviews.delete_class_save,name='delete_class_save')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
