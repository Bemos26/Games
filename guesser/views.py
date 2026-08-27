import random
from django.shortcuts import render

def game_home(request):
    # 1. SETUP (Runs every time)
    if 'secret_number' not in request.session:
        request.session['secret_number'] = random.randint(1, 100)
        request.session['attempts_left'] = 5
        
    feedback_message = ""

    # 2. GAME LOGIC (ONLY runs when they hit submit)
    if request.method == 'POST':
        # guess is created here!
        guess = int(request.POST.get('user_guess'))
        secret = request.session['secret_number']
        
        request.session['attempts_left'] -= 1
        
        # This MUST be indented inside the POST block!
        if guess == secret:
            feedback_message = f"Congratulations! {secret} was correct!"
            del request.session['secret_number']
            del request.session['attempts_left']
        else:
            if request.session['attempts_left'] <= 0:
                feedback_message = f"Game Over! The number was {secret}."
                del request.session['secret_number']
                del request.session['attempts_left']
            else:
                if guess < secret:
                    feedback_message = "Too low! Try again."
                else:
                    feedback_message = "Too high! Try again."

    # 3. CONTEXT (Runs every time, pushed all the way to the left)
    context = {
        'message': feedback_message,
        'attempts_left': request.session.get('attempts_left', 0)
    }
    return render(request, 'guesser_home.html', context)