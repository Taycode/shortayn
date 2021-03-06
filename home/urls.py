from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('api/', include('home.api.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('<str:short_code>/delete', views.delete_link, name='delete_link'),
    path('<str:short_code>/', views.redirect_user, name='redirect'),
]
