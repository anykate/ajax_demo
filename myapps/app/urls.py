from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.AjaxHandlerView.as_view(), name='ajax_handler'),
]
