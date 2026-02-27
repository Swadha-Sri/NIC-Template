from django.urls import path
from .views import index, inner, sitemap, contactus, dashboard, buttons, cards, table, typography, icons, forms, areachart, barchart, scatterchart, polarareachart, linechart, doughnut_piechart, predictive_dashboard, descriptive_dashboard, anamap_dashboard, advanced_ana_dashboard, download_solar_pump_data, view_uploaded_file_data, download_uploaded_file, delete_uploaded_file

urlpatterns = [
    path('', index, name='index'),
    path('inner/', inner, name='inner'),
    path('contactus/', contactus, name='contactus'),
    path('sitemap/', sitemap, name='sitemap'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/download-solar-pump-data/', download_solar_pump_data, name='download_solar_pump_data'),
    path('dashboard/uploads/<int:upload_id>/view/', view_uploaded_file_data, name='view_uploaded_file_data'),
    path('dashboard/uploads/<int:upload_id>/download/', download_uploaded_file, name='download_uploaded_file'),
    path('dashboard/uploads/<int:upload_id>/delete/', delete_uploaded_file, name='delete_uploaded_file'),
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
    path('dashboard/predictive/', predictive_dashboard, name='predictive_dashboard'),
    path('dashboard/descriptive/', descriptive_dashboard, name='descriptive_dashboard'),
    path('dashboard/anamap/', anamap_dashboard, name='anamap_dashboard'),
    path('dashboard/advanced-ana/', advanced_ana_dashboard, name='advanced_ana_dashboard'),

]
