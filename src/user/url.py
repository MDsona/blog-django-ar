from django.urls import path                    # -14c
from . import views                            
from django.contrib.auth.views import LoginView, LogoutView          # -16a

urlpatterns = [                                        
    path('register/', views.register, name = 'register_url'),        # -14c  , views.function
    # 17c path('login/', LoginView.as_view(template_name='user/login.html'), name = 'login_url'), # -16a  , class 16b template_name
    path('login/', views.login_user, name = 'login_url'),            # -17c
    # 17g path('logout/', LogoutView.as_view(template_name='user/logout.html'), name = 'logout_url'),  # -16d
    path('logout/', views.logout_user, name = 'logout_url'),         # -17g
    path('profile/', views.profile, name = 'profile_url'),           # -18b
]