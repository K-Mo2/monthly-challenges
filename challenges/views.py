from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
monthly_challenges = {
    'januray':'Eat no meat for the entire month!',
    'february':'Walk for at least 20 minutes everyday!',
    'march':'Walk for at least 20 minutes everyday!',
    'april':'Run for 30 minutes everyday',
    'may':'Eat vegetables for 30 days',
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(monthly_challenges) or month < 1:
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]    

    return HttpResponseRedirect('/challenges/' + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)

    except:
        return HttpResponseNotFound("This month is not supported!")
