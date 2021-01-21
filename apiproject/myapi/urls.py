from django.urls import path
from . import views

urlpatterns = [
    path('', views.accountList, name="accounts"),
    path('create', views.createAccount, name="create"),
    path('detail/<str:pk>', views.accountDetail, name="detail"),
    path('update/<str:pk>/deposit/<int:value>', views.depositMoney, name="deposit"),
    path('update/<str:pk>/debit/<int:value>', views.debitMoney, name="debit"),
    path('delete/<str:pk>', views.deleteAccount, name="delete")
]