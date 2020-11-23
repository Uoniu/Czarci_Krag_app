from django.conf.urls import url
from django.urls import path
from App import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # =========================================================== guest
    path('guest/', views.guest_home, name='home'),
    # =========================================================== shared
    path('logout/', views.logout, name='logout'),
    path('my_bookings/', views.user_bookings, name='user_bookings'),
    path('my_points/', views.user_points, name='user_points'),
    # =========================================================== shared
    path('', views.guest_home, name='home'),
    path('prices/', views.prices, name='prices'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.prices, name='contact'),
    path('login/', views.login, name='login')

]

urlpatterns += staticfiles_urlpatterns()

