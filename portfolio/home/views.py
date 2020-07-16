from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Hello")
    context = {'name': 'Joy', 'course': 'Django'}
    return render(request, 'home.html',context)
    
def about(request):
    # return HttpResponse("Hello about")
    return render(request, 'about.html')
def projects(request):
    # return HttpResponse("Hello projects")
    return render(request, 'projects.html')
def contact(request):
    # return HttpResponse("Hello contact")
    return render(request, 'contact.html')