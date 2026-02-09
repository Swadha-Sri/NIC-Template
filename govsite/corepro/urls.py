from django.urls import path
from .views import index, inner, sitemap, contactus, dashboard, buttons, cards, table, typography, icons, forms, areachart, barchart, scatterchart, polarareachart, linechart, doughnut_piechart

urlpatterns = [
    path('', index, name='index'),
    path('inner/', inner, name='inner'),
    path('contactus/', contactus, name='contactus'),
    path('sitemap/', sitemap, name='sitemap'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/buttons/', buttons, name='buttons'),
    path('dashboard/cards/', cards, name='cards'),
    path('dashboard/table/', table, name='table'),
    path('dashboard/typography/', typography, name='typography'),
    path('dashboard/icons/', icons, name='icons'),
    path('dashboard/forms/', forms, name='forms'),
    path('dashboard/charts/areachart/', areachart, name='areachart'),
    path('dashboard/charts/barchart/', barchart, name='barchart'),
    path('dashboard/charts/scatterchart/', scatterchart, name='scatterchart'),
    path('dashboard/charts/polarareachart/', polarareachart, name='polarareachart'),
    path('dashboard/charts/linechart/', linechart, name='linechart'),
    path('dashboard/charts/doughnut_piechart/', doughnut_piechart, name='doughnut_piechart'),

]
