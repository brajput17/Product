from django.urls import path
from . import views

urlpatterns = [
      path('signup',views.Registration.as_view(),name="signup"),
      path('',views.Logins.as_view(),name="login"),
      path('logout',views.logouts,name="logout"),
      path('dashboard',views.dashboard,name="dashboard"),
      path('delete',views.delete,name='delete'),
      path('update',views.update,name='update'),
       path('add_product',views.add_product,name='add_product'),

    
]
