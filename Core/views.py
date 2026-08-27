from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Welcome to myGames where you find your favorite Python Games!") #this is the home page of the website. It will display a welcome message to the user.
def home(request):
    return render(request, 'home.html', context_data) #this is the home page of the website. It will display a welcome message to the user.

# We are creating a dictionary of data to send to the HTML
context_data = {
    'platform_name': 'My Awesome Games',
    'creator': 'Bemos',
    'games_count': 0 
}