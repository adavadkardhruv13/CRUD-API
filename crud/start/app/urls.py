from django.urls import path
from.views import cropListView, cropDetailView

urlpatterns = [
    path('api/crop', cropListView),
    path('api/crop/<int:pk>', cropDetailView)
]
