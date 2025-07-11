from django.shortcuts import render

def page_name(request):
    return render(request, 'LoginPage/MainTemp.html')

# def second(request):
#     return render(request, 'proj_name/second.html')