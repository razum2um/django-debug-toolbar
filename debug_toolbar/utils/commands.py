import os, binascii
from django.contrib.auth import authenticate, logout, login

def get_test_user(purpose):
    """
    Gets a test user by changing his pass by a random one

    Always set purpose since it could be more subclasses/1to1 to User,
    and we cannot purge them without cleaning all related objects,
    neither is good derivating from the same User
    """
    from django.contrib.auth.models import User
    passwd = binascii.b2a_base64(os.urandom(6)) # reliable enough?
    user, is_created = User.objects.get_or_create(username='test_user_for_%s' % purpose)
    user.set_password(passwd)
    user.save()
    user = authenticate(username=user.username, password=passwd)
    return user

def force_login_admin(request):
    """
    Creates an admin, set him radom pass, login as him
    """
    try:
        # as contrib doesn't return anything
        user = get_test_user(purpose='admin')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        login(request, user) 
        return True
    except:
        return False

def force_logout(request):
    """
    Simple. Force logout ;)
    """
    try:
        logout(request)
        return True
    except:
        return False

