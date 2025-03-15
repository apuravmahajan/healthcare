
from django.urls import path
from .views import Doctor_View

urlpatterns = [
    
    path('', Doctor_View.as_view(), name="doctor"),
    path('<int:id>/', Doctor_View.as_view(), name="edit")
]
