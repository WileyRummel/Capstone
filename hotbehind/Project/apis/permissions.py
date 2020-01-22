from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    # might to to add this to the other classes to allow safe permissions for others
    def has_object_permission(self, request, view, obj):
        #read only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:    
            return True

        # Write Permissions are only allowed to the author of a post
        return obj.author == request.user

class IsApproved(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.approved:
            return True
        return False

class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user