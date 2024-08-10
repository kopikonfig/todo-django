from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Daftar halaman publik yang bisa diakses tanpa autentikasi
        public_pages = [
            '/login/',
            '/users/register/',
            '/logout/',
            '/help/',
            '/privacy/',
            '/admin/login/',
            '/terms/',
            '/',
        ]

        # Cek apakah user sudah logout (tidak terautentikasi)
        if not request.user.is_authenticated:
            # Cegah akses ke halaman non-publik
            if request.path not in public_pages and not request.path.startswith('/static/'):
                return redirect('/login/')

    def process_response(self, request, response):
        # Tambahkan header untuk mencegah cache halaman
        public_pages = [
            '/login/',
            '/users/register/',
            '/logout/',
            '/help/',
            '/privacy/',
            '/terms/',
            '/admin/login/',
            '',
        ]

        if not request.user.is_authenticated or request.path in public_pages:
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
        return response
