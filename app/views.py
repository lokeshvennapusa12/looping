from django.shortcuts import render

def looping(request):

    d={'name':'Lokesh'}


    return render(request,'looping.html',d)
    