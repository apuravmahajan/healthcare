from django.urls import path
from .views import Mapping_View

urlpatterns=[
    path('', Mapping_View.as_view(), name="mapping"),
    path('<int:id>/', Mapping_View.as_view(), name="edit"),
    path('<int:pid>/<int:did>/', Mapping_View.as_view(), name="delete"),
]