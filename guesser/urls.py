from django.urls import path
from . import views  # The dot means "import views from this current folder"

urlpatterns = [
    # We will leave the path empty for now, so it will be the "home" of this game
    path('', views.game_home, name='guesser_home'), 
]