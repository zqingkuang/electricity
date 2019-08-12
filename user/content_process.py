from .models import User
from django.shortcuts import redirect


def get_user(request):
    u_id = request.session.get("u_id")
    if u_id:
        u = User.objects.get(id=u_id)
        return {"u": u}
    else:
        return {}


def login_decorator(views):
    """登录状态判断装饰器"""

    def login_views(request, *args, **kwargs):
        u_id = request.session.get("u_id")
        if u_id:
            return views(request, *args, **kwargs)
        else:
            return redirect('login')

    return login_views
