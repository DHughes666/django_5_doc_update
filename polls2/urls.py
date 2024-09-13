from django.urls import path

from . import views

app_name = "polls2"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls2/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls2/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="votes"),
]