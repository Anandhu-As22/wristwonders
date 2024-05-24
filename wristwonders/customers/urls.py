from django.urls import path
from customers import views


urlpatterns =[
    path('',views.Home_page,name ='home' ),
    path('user-login/',views.user_login,name='user-login'),
    path('user-signup/',views.user_signup,name='user-signup')
    
]
