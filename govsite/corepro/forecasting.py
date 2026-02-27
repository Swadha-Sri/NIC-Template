from collections import defaultdict
import numpy as np

def calculate_district_forecast(data):
    district_data = defaultdict(list)

    for row in data:
        if row["installed"] > 0:
            district_data[row["district"]].append(row)

    forecast_results = []

    for district, records in district_data.items():

        if len(records) < 2:
            continue

        records = sorted(records, key=lambda x: x["year"])

        years_index = list(range(1, len(records) + 1))
        installed_values = [r["installed"] for r in records]

        slope, intercept = np.polyfit(years_index, installed_values, 1)

        next_year_index = len(records) + 1
        predicted_next = int(intercept + slope * next_year_index)

        growth = (slope / installed_values[-1] * 100) if installed_values[-1] > 0 else 0

        risk = "Stable"
        if slope < 0:
            risk = "High Risk"
        elif slope > 50:
            risk = "High Growth"

        forecast_results.append({
            "district": district,
            "latest_year": records[-1]["year"],
            "growth_rate": round(growth, 2),
            "predicted_next_year_installed": max(predicted_next, 0),
            "risk_level": risk
        })

    forecast_results = sorted(forecast_results, key=lambda x: x["predicted_next_year_installed"], reverse=True)

    return forecast_results
