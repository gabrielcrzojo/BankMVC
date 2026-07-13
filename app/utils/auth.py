from bottle import request, redirect
from app.models.usuario import UsuarioModel
import functools

def get_current_user():
    user_id = request.get_cookie('session_id', secret='bmvc-secret')
    if user_id:
        return UsuarioModel.get_by_id(user_id)
    return None

def requires_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = get_current_user()
        if not user:
            redirect('/login')
        return func(*args, **kwargs)
    return wrapper
