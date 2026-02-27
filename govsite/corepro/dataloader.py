from .models import SolarYearData


def load_solar_data_from_db():
    records = (
        SolarYearData.objects.select_related("district")
        .all()
        .order_by("year_label", "district__name")
    )

    structured_data = []
    for record in records:
        structured_data.append(
            {
                "Distcode": record.district.code,
                "district": record.district.name,
                "year": record.year_label,
                "target": int(record.target or 0),
                "booking": int(record.booking or 0),
                "installed": int(record.installed or 0),
                "rejected": int(record.rejected or 0),
            }
        )

    return structured_data

def load_solar_excel():
    return load_solar_data_from_db()
