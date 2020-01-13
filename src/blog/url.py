from django.urls import path                    # -2c
from . import views                             # -2c
from .views import PostCreateView               # -27b

urlpatterns = [                                        
    path('', views.home, name= 'home_url'),            # -2c
    path('about/', views.about, name= 'about_url'),     # -4b
    path('detail/<int:post_id>/', views.post_detail, name= 'detail_url'),     # -7c
    path('new_post/', PostCreateView.as_view(), name= 'new_post_url'),        # -27b
]

