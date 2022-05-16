from django.urls import path
from .views import (PersonalPage, InputWeight,
ChangeUserDetails, CustomLoginView, RegisterPage, Group,
CreateUserDetails, EditWeightRecord, DeleteWeightInput)

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('account/', PersonalPage.as_view(), name='account'),
    path('update-weight/', InputWeight.as_view(), name='update-weight'),
    path('delete-weight/<int:pk>/', DeleteWeightInput.as_view(), name='delete-weight'),
    path('edit-update-weight/<int:pk>/', EditWeightRecord.as_view(), name='edit-update-weight'),
    path('update-details/<int:pk>/', ChangeUserDetails.as_view(), name='update-details'),
    path('new-details/', CreateUserDetails.as_view(), name='new-details'),


    path('', Group.as_view(), name='group'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
]
