from django.core.exceptions import ObjectDoesNotExist
# from django.db.models import Q

from .models import UsersDetails


def is_authenticate(username, password):
    """
    Authenticate the user
    1. on the basis of email + password
    :param username: required(email/username)
    :param password: required
    :return: if success user object, otherwise pass
    """
    try:
        user = UsersDetails.objects.get(email__exact=username, active=True)
        print (user)
        if user.check_password(password):
            return user
    except ObjectDoesNotExist:
        pass

