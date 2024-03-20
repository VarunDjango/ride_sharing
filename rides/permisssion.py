from rest_framework import permissions


class UserTypePermission(permissions.BasePermission):
    """
    Custom permission to allow only certain actions based on user type.
    """

    def has_permission(self, request, view):
        # Allow GET requests (e.g., for listing objects)

        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        # For POST requests (create), check if user is a rider
        if request.method in ['POST', 'PUT', 'PATCH'] and request.user.user_type == 'rider':
            return True

        # For PUT and PATCH requests (update), check if user is a driver
        if request.method in ['PUT', 'PATCH'] and request.user.user_type == 'driver':
            return True

        return False
