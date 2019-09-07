from django.shortcuts import render

def newVisitor(request):
    context = {'title': 'VMS | New Visitor'}
    return render(request, 'user/add_visitor.html', context)
