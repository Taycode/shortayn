from django.urls import path
from home.api import views

urlpatterns = [
    path('link/', views.link_list),
    path('link/<str:short_code>/', views.link_details),
    path('login/', views.login_view)
]