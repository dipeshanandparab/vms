from django.shortcuts import render


def homePage(request):
    context = {'title':'VMS | Home '}
    return render(request, 'visitors_management/homePage.html', context)