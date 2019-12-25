from django.urls import path                    # -2c
from . import views                             # -2c

urlpatterns = [                                        
    path('', views.home, name= 'home_url'),            # -2c
    path('about/', views.about, name= 'about_url'),     # -4b
]

