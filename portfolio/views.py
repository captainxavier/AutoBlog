from django.shortcuts import render


def portfolio_screen_view(request):
    context = {}   
    return render(request, 'portfolio/portfolio.html', context)

