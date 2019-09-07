from django.shortcuts import render
# from .models import Company
# from django.http import Http404
from .models import Visitor

def visitorsList(request):
    visitors_list = Visitor.objects.all()
    context = {
        'visitors_list': visitors_list,
        'title':'VMS | Visitors List'
    }
    return render(request, 'visitor/visitors_list.html', context)

def visitorsDetail(request, id):
    visitors_detail = Visitor.objects.get(pk=id)
    print(f'Details:',visitors_detail)
    context = {'visitors_detail': visitors_detail, 'title':'VMS | Visitor Details'}
    return render(request, 'visitor/visitors_detail.html', context)

