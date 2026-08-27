import random
from django.shortcuts import render

def game_home(request):
    # 1. SETUP: Check if a secret number already exists in the user's session backpack.
    if 'secret_number' not in request.session:
        # If not, generate one and put it in the backpack!
        request.session['secret_number'] = random.randint(1, 100)
    
    # We will use this variable to send feedback to the HTML
    feedback_message = ""

    # 2. GAME LOGIC: Did the user submit a guess?
    if request.method == 'POST':
        # Grab the guess from the form (it comes in as a string, so we convert to int)
        guess = int(request.POST.get('user_guess'))
        
        # Retrieve the secret number from the session backpack
        secret = request.session['secret_number']
        
        # Compare them!
        if guess < secret:
            feedback_message = "Too low! Try again."
        elif guess > secret:
            feedback_message = "Too high! Try again."
        else:
            feedback_message = f"Congratulations! {secret} was correct!"
            # Game over! Delete the secret number so a new one is generated next time.
            del request.session['secret_number']

    # 3. SEND TO HTML: Pack up the message into our context dictionary
        context = {
        'message': feedback_message
    }
    
    # Pass the context to the template
    return render(request, 'guesser_home.html', context)