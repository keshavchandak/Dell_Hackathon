from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bank/<int:model_no>',views.bank,name='bank'),
    path('getBankDataURL',views.getBankData,name='getBankDataURL'),
    path('thankyou',views.thankyou,name='thankyou'),
    path('security',views.securitypage,name='security'),
    path('getSecurityURL',views.getSecurityData,name='getSecurityURL'),
    path('register',views.register,name='register')
]
