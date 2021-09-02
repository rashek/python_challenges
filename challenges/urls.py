from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    # path("january", views.january),
    path("", views.index),
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenges, name="monthly_changes")
]
