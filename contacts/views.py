from django.shortcuts import render


def contact_screen_view(request):
    context={}
    return render(request, 'contacts/contact.html', context)
