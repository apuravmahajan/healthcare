
from django.urls import path
from .views import Patient_View

urlpatterns = [
    
    path('', Patient_View.as_view(), name="patient"),
    path('<int:id>/', Patient_View.as_view(), name="edit")
]
