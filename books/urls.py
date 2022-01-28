# created by sagar kakade


from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # account Urls
    path('', views.login, name="login"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # for forget password
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="account/reset_password.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="account/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name="account/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="account/password_reset_done.html"), name='password_reset_complete'),
    path('change_password/', auth_views.PasswordChangeView.as_view(
        template_name="account/change_password.html"), name='change_password'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="account/password_change_done.html"), name='password_change_done'),

    # profile
    path('profile/', views.profile, name="profile"),
    path('requestProfile/', views.requestProfile, name="requestProfile"),

    path('home/', views.homepage, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about-us/', views.about, name="about-us"),
    path('search/', views.search, name="search"),
    path('addbook/', views.addbook, name="addbook"),
    path('signup/', views.SignUp, name="signup"),

    path('allBooks/', views.allBooks, name="allBooks"),
    #     path('requestProfile/followers_count',
    #          views.followers_count, name="followers_count"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
