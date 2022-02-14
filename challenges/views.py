from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def monthly_challenges(request, month):
    challenge_text=None
    if month == 'january':
        challenge_text='Eat no meat for the entire month!'
    
    elif month == 'february':
        challenge_text='Walk for at least 20 minutes everyday!'
    
    elif month == 'march':
        challenge_text='Learn Django for at least 20 minutes everyday!'
    
    else:
        return HttpResponseNotFound("This month is not supprted!")
    
    return HttpResponse(challenge_text)
