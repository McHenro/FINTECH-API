from .views import RegisterAPI, LoginAPI
from django.urls import path
from knox import views as knox_views
from .import api
app_name ='speedapp'


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/deposit/', api.DepositCreateAPI.as_view(), name='deposit'),
    path('api/withdraw/', api.WithdrawCreateAPI.as_view(), name='withdraw'),
       
]