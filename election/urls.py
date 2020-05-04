from django.urls import path
from .views import index, vote

urlpatterns = [
    path('', index.as_view()),
    path('vote',
         vote.as_view())
]
