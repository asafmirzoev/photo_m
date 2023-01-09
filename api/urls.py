from django.urls import path

from .views import ImageView, PersonView


urlpatterns = [
    path('images/', ImageView.as_view()),
    path('images/<uuid:image_id>/', ImageView.as_view()),
    path('persons/', PersonView.as_view())
]