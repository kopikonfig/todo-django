from django.contrib.auth.mixins import LoginRequiredMixin

class AdminRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
