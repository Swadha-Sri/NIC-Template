import re
from pathlib import Path
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


def solar_upload_path(instance, filename):
	return f"solar_uploads/{filename}"


class SolarDataUpload(models.Model):
	FILE_NAME_PATTERN = re.compile(r"^SolarPumpData_\d{4}-\d{2}\.xlsx$")

	file = models.FileField(upload_to=solar_upload_path)
	original_filename = models.CharField(max_length=255)
	year_label = models.CharField(max_length=7)
	uploaded_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name="solar_data_uploads",
	)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-uploaded_at"]

	def __str__(self):
		return self.original_filename

	@classmethod
	def validate_filename(cls, filename):
		if not cls.FILE_NAME_PATTERN.match(filename):
			raise ValidationError(
				"File name must follow this format: SolarPumpData_YYYY-YY.xlsx"
			)

	@staticmethod
	def extract_year_label(filename):
		match = re.search(r"(\d{4}-\d{2})", filename)
		return match.group(1) if match else ""

	def clean(self):
		filename = self.original_filename or Path(self.file.name).name
		self.validate_filename(filename)
		self.year_label = self.extract_year_label(filename)

	def save(self, *args, **kwargs):
		if self.file and not self.original_filename:
			self.original_filename = Path(self.file.name).name
		self.full_clean()
		super().save(*args, **kwargs)


class District(models.Model):
	code = models.CharField(max_length=20, unique=True)
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["name", "code"]

	def __str__(self):
		return f"{self.name} ({self.code})"


class SolarYearData(models.Model):
	district = models.ForeignKey(
		District,
		on_delete=models.CASCADE,
		related_name="solar_year_data",
	)
	year_label = models.CharField(max_length=7)
	target = models.PositiveIntegerField(default=0)
	booking = models.PositiveIntegerField(default=0)
	installed = models.PositiveIntegerField(default=0)
	rejected = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["year_label", "district__name"]
		constraints = [
			models.UniqueConstraint(
				fields=["district", "year_label"],
				name="unique_district_year_solar_data",
			)
		]

	def __str__(self):
		return f"{self.district.name} - {self.year_label}"
