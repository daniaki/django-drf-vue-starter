def username(request):
    """
    Return the username of the currently logged in user if appropriate.
    """
    uname = None
    if request.user:
        uname = request.user.username
    return {'USERNAME': uname}


def user_is_authenticated(request):
    """
    Adds a bool to Django's context specifying if the current user is
    authenticated.
    """
    is_auth = False
    if request.user:
        is_auth = bool(request.user.is_authenticated)
    return {'IS_AUTHENTICATED': is_auth}
