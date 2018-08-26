from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bank/<int:model_no>',views.bank,name='bank'),
    path('getBankDataURL',views.getBankData,name='getBankData')
]
