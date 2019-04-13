from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('shorten', views.shorten, name='shorten'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('shorten/<str:short_code>/', views.redirect_user, name='redirect'),

]