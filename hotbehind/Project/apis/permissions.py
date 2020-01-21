from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    #need to add the CustomUser 'approved' field for only approved users to post!
    
    def has_object_permission(self, request, view, obj):
        #read only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write Permissions are only allowed to the author of a post
        return obj.author == request.user