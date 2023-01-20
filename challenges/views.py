from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn for at least 20 minutes every day!",
    "april": "Run for at least 20 minutes every day!",
    "may": "Do something you never done before every day!",
    "june": "Do push-ups for at least 20 minutes every day!",
    "july": "Drink 2l of water every day!",
    "august": "Swim for at least 20 minutes every day!",
    "september": "Read a book for at least 20 minutes every day!",
    "october": "Come up with a new hobby and do it every day!",
    "november": "Save at least 300$ for the entire month!",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request=request, template_name="challenges/challenge.html", context={
            "text": challenge_text,
            "month": month
        })
    except Exception:
        raise Http404()
