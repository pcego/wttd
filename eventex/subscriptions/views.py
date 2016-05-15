from django.shortcuts import render


def subscribe(request):
    return render(request, 'subscription_form.html')