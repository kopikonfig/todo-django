import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_email(value):
    """
    Validasi format email yang benar.
    """
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, value):
        raise ValidationError(_('Invalid email format'))

def validate_username(value):
    """
    Validasi username yang hanya boleh mengandung huruf, angka, 
    underscore dan harus antara 4 sampai 30 karakter.
    """
    if len(value) < 4 or len(value) > 30:
        raise ValidationError(_('Username must be between 4 and 30 characters'))
    if not re.match(r'^\w+$', value):
        raise ValidationError(_('Username can only contain letters, numbers, and underscores'))

def validate_password(value):
    """
    Validasi password yang kuat. Password harus memiliki minimal 8 karakter,
    mengandung setidaknya satu huruf besar, satu huruf kecil, satu angka, 
    dan satu karakter spesial.
    """
    if len(value) < 8:
        raise ValidationError(_('Password must be at least 8 characters long'))
    if not re.search(r'[A-Z]', value):
        raise ValidationError(_('Password must contain at least one uppercase letter'))
    if not re.search(r'[a-z]', value):
        raise ValidationError(_('Password must contain at least one lowercase letter'))
    if not re.search(r'[0-9]', value):
        raise ValidationError(_('Password must contain at least one digit'))
    if not re.search(r'[@$!%*?&]', value):
        raise ValidationError(_('Password must contain at least one special character (@$!%*?&)'))

def validate_phone_number(value):
    """
    Validasi format nomor telepon yang benar.
    """
    phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
    if not phone_pattern.match(value):
        raise ValidationError(_('Invalid phone number format'))

def validate_positive_number(value):
    """
    Validasi angka positif.
    """
    if value < 0:
        raise ValidationError(_('Value must be positive'))

def validate_non_empty_string(value):
    """
    Validasi string yang tidak boleh kosong.
    """
    if not value.strip():
        raise ValidationError(_('This field cannot be empty'))

def validate_url(value):
    """
    Validasi format URL yang benar.
    """
    url_pattern = re.compile(
        r'^(https?:\/\/)?'  # http:// or https://
        r'((([a-zA-Z0-9]{1,}\.)+[a-zA-Z]{2,})|'  # domain...
        r'(([0-9]{1,3}\.){3}[0-9]{1,3}))'  # ...or ip
        r'(:[0-9]{1,5})?'  # optional port
        r'(\/[a-zA-Z0-9\._\-~]*)*\/?$'  # resource path
    )
    if not url_pattern.match(value):
        raise ValidationError(_('Invalid URL format'))
