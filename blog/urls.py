from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('zazu', login_required(TemplateView.as_view(template_name="index.html", extra_context={'text':"Here's the text of the Web page.", }), login_url='/admin/login/'), name='zazu'),
]
