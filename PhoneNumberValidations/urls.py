from django.urls import path
from .views import PhoneNumberList, PhoneNumberDetail, PhoneNumberFilter

urlpatterns = [
    path('PhoneNumberValidations/phonenumbers/', PhoneNumberList.as_view(), name='phonenumbers-list'),
    path('PhoneNumberValidations/phonenumbers/<int:pk>/', PhoneNumberDetail.as_view(), name='phonenumbers-detail'),
    path('PhoneNumberValidations/phonenumbers/filter/<str:country>/<int:state>/', PhoneNumberFilter.as_view(), name='phonenumbers-filter'),
]
