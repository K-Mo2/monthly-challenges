from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
# Create your views here.
monthly_challenges = {
    'januray':'Eat no meat for the entire month!',
    'february':'Walk for at least 20 minutes everyday!',
    'march':'Walk for at least 20 minutes everyday!',
    'april':'Run for 30 minutes everyday',
    'may':'Eat vegetables for 30 days',
}

class indexView(View):


    def get(self,request):
   
        months = list(monthly_challenges.keys())

        return render(request, 'challenges/index.html', {
            "months":months
        })

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
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month":month,
        })

    except:
        return HttpResponseNotFound("This month is not supported!")
