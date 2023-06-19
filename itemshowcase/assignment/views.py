from django.shortcuts import render

# Create your views here.
def loadHomePage(request):
    return render(request, "assignment/index.html")

def loadAboutPage(request):
    return render(request, "assignment/about.html")

def loadServicePage(request):
    return render(request, "assignment/services.html")

def loadContactPage(request):
    """
    This is the contact page
    """

    return render(request, "assignment/contact.html")
