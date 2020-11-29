from django.conf.urls import url
from django.urls import path
from App import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # =========================================================== guest
    # path('guest/', views.guest_home, name='home'),
    # =========================================================== user
    path('my/logout/', views.logout, name='logout'),
    path('my/bookings/', views.user_bookings, name='user_reservations'),
    path('my/points/', views.user_points, name='user_points'),
    path('my/profile/', views.user_profile, name='user_profile'),
    # =========================================================== manager
    path('manage/boots/', views.all_boots, name='all_boots'),
    path('manage/reservations/', views.all_reservations, name='all_reservations'),
    path('manage/notifications/', views.notifications, name='notifications'),

    # =========================================================== admin
    path('power/users/', views.all_users, name='all_users'),
    path('power/points/', views.all_programs, name='all_programs'),

    # =========================================================== shared
    path('', views.guest_home, name='home'),
    path('prices/', views.prices, name='prices'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('faq/', views.faq, name='faq'),
]

urlpatterns += staticfiles_urlpatterns()

