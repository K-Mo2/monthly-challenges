from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    'januray':'Eat no meat for the entire month!',
    'february':'Walk for at least 20 minutes everyday!',
    'march':'Walk for at least 20 minutes everyday!',
    'april':'Run for 30 minutes everyday',
    'may':'Eat vegetables for 30 days',
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalize_months = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li> <a href='{month_path}'>{capitalize_months}</a></li>"
        
    response_data = f"<ol>{list_items}</ol>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(monthly_challenges) or month < 1:
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]    

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)

    except:
        return HttpResponseNotFound("This month is not supported!")
