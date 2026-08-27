from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def game_home(request):
    return HttpResponse("Welcome to the guesser game! Try to guess the number I'm thinking of!") #this is the home page of the guesser game. It will display a welcome message to the user.