from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_student == True:
            return True
        else:
            return False

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_teacher == True:
            return True
        else:
            return False


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser == True:
            return True
        else:
            return False

class IsMember(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_member == True:
            return True
        else:
            return False