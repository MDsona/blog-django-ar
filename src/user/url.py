from django.urls import path                    # -14c
from . import views                            

urlpatterns = [                                        
    path('register/', views.register, name= 'register_url'),            # -14c
]