from django.contrib import admin
from .models import SolarDataUpload, District, SolarYearData


@admin.register(SolarDataUpload)
class SolarDataUploadAdmin(admin.ModelAdmin):
	list_display = ("original_filename", "year_label", "uploaded_by", "uploaded_at")
	search_fields = ("original_filename", "year_label", "uploaded_by__username")


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
	list_display = ("code", "name", "updated_at")
	search_fields = ("code", "name")
	ordering = ("name",)


@admin.register(SolarYearData)
class SolarYearDataAdmin(admin.ModelAdmin):
	list_display = (
		"district",
		"year_label",
		"target",
		"booking",
		"installed",
		"rejected",
		"updated_at",
	)
	list_filter = ("year_label",)
	search_fields = ("district__code", "district__name", "year_label")
	autocomplete_fields = ("district",)
	ordering = ("year_label", "district__name")
