from django.urls import path                    # -14c
from . import views                            
from django.contrib.auth.views import LoginView, LogoutView             # -16a

urlpatterns = [                                        
    path('register/', views.register, name = 'register_url'),        # -14c  , views.function
    path('login/', LoginView.as_view(template_name='user/login.html'), name = 'login_url'), # -16a  , class 16b template_name
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name = 'logout_url'),  # -16d
]