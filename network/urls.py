from django.urls import path

from network import views


urlpatterns = [

    path('list/', views.CompanyView.as_view(), name='company_list'),

]