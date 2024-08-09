from django.core.exceptions import PermissionDenied

def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
