import challenges
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges_list = {
    "january": "Eat meat and fat for entire month!",
    "february": "Walk for at least 20 minute every day!",
    "march": "Learn Django for rest of the day when u don't have other job to do!",
    "april": "Eat meat and fat for entire month!",
    "may": "Walk for at least 20 minute every day!",
    "june": "Learn Django for rest of the day when u don't have other job to do!",
    "july": "Eat meat and fat for entire month!",
    "august": "Walk for at least 20 minute every day!",
    "september": "Learn Django for rest of the day when u don't have other job to do!",
    "october": "Eat meat and fat for entire month!",
    "november": "Walk for at least 20 minute every day!",
    "december": "Learn Django for rest of the day when u don't have other job to do!",
}
# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges_list.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_changes", args=[month])
        list_items += f"<li><a href=\"{month_path}\"> {capitalized_month}</a></li>"

    response_data = f"<ul> {list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_number(requst, month):
    # months= list(monthly_challenges_list.keys())
    months = list(monthly_challenges_list.keys())
    redirect_month = months[month]
    redirect_path = reverse("monthly_changes", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        # challenges_text = monthly_challenges_list[month]

        # does the same think like the following 2 line
        return render(request, "challenges/challenge.html")
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")

    # if month == "january":
    #     challenges_text = "Eat meat and fat for entire month!"
    # elif month == "february":
    #     challenges_text = "Walk for at least 20 minute every day!"
    # elif month == "march":
    #     challenges_text = "Learn Django for rest of the day when u don't have other job to do!"
        # return HttpResponse(challenges_text)
    # else:
        # return HttpResponseNotFound("This month is not supported!")


# def january(request):
#     return HttpResponse("Eat meat and fat for entire month!")


# def fabruary(request):
#     return HttpResponse("Walk for at least 20 minute every day!")
