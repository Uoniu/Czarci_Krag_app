from django.conf.urls import url
from django.urls import path, include
from App import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
# guest
    path('guest/home/', views.index, name='home'),
    path('', views.index, name='home'),
    path('guest/login/', views.login, name='login'),
    path('guest/prices/', views.prices, name='prices'),
    path('guest/gallery/', views.gallery, name='gallery'),
    path('guest/about/', views.about, name='about'),
    path('guest/contact/', views.contact, name='contact'),

# admin
    path('power/home/', views.admin_home, name='admin_home'),
    path('power/admin/', admin.site.urls, name='admin_control'),
# manager
    path('manager/home/', views.manager_home, name='manager_home'),

# user
    path('user/home/', views.user_home, name='user_home'),
    path('user/data/', views.user_data, name='user_data'),
    path('user/program/', views.user_program, name='user_program'),
    path('user/reserve/', views.user_reserve, name='user_reserve'),

# worker
    path('worker/home/', views.worker_home, name='worker_home'),

# shared
    path('logout/', views.logout, name='logout')
    # path('prices/', views.prices, name='prices')

]

urlpatterns += staticfiles_urlpatterns()

