from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(UserProfileImage)
admin.site.register(Teacher)



class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'roll']
admin.site.register(Student, StudentsAdmin)




class ClassStudentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'classroom', 'student']


admin.site.register(ClassStudents, ClassStudentsAdmin)

class MyClassroomAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'teacher']

admin.site.register(MyClassroom, MyClassroomAdmin)
