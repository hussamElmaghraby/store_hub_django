from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffReadOnly(BasePermission):
    """"
    - Allow safe methods (GET , HEAD , OPTIONS) for all users.
    - Only allow write methods for stuff users.
    """
    def has_permission(self , request , view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff