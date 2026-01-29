from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'public/index.html')

def inner(request):
    return render(request, 'public/inner.html')

def sitemap(request):
    return render(request, 'public/site-map.html')

def contactus(request):
    return render(request, 'public/contactus.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def buttons(request):
    return render(request, 'dashboard/buttons.html')

def cards(request):
    return render(request, 'dashboard/cards.html')

def table(request):
    return render(request, 'dashboard/table.html')

def typography(request):
    return render(request, 'dashboard/typography.html')

def icons(request):
    return render(request, 'dashboard/icons.html')

def forms(request):
    return render(request, 'dashboard/forms.html')

def areachart(request):
    return render(request, 'dashboard/charts/areachart.html')

def scatterchart(request):
    return render(request, 'dashboard/charts/scatterchart.html')

def polarareachart(request):
    return render(request, 'dashboard/charts/polarareachart.html')

def linechart(request):
    return render(request, 'dashboard/charts/linechart.html')

def doughtnut_piechart(request):
    return render(request, 'dashboard/charts/doughtnut_piechart.html')