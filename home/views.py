from django.shortcuts import render
from accounts.models import Account



def home_screen_view(request):

    accounts = Account.objects.all()
    context = {
         'accounts': accounts,
    }

    return render(request, 'home/index.html', context)