# urls.py

from django.urls import path
from . import views
from .views import back_or_default

urlpatterns = [
    path('Scan-Result', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    path('keyword-scan/', views.keyword_scan, name='keyword_scan'),
    path('user-files/', views.user_files, name='user_files'),
    path('delete-file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('file-details/<int:file_id>/', views.file_details, name='file_details'),
    path('back/', back_or_default, name='back'),
    path('senti/', views.user_upload, name='user_upload'),
    path('delete-uploaded-file/<int:file_id>/', views.delete_uploaded_file, name='delete_uploaded_file'),
    path('', views.test, name='test'),
    path('AboutUs/', views.AboutUs, name="AboutUs"),
]
