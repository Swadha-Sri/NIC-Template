from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.forms import LoginCaptchaForm
import csv
import json

# Create your views here.
def index(request):
    return render(request, 'public/index.html', {
        "captcha_form": LoginCaptchaForm()
    })

def inner(request):
    return render(request, 'public/inner.html')

def sitemap(request):
    return render(request, 'public/site-map.html')

def contactus(request):
    return render(request, 'public/contactus.html')

@login_required(login_url='login')
def dashboard(request):
    def _load_solar_data():
        csv_path = settings.BASE_DIR / 'corepro' / 'data' / 'solar-data-combined.csv'
        rows = []
        try:
            with open(csv_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    district = (row.get('District') or '').strip()
                    if not district:
                        continue
                    rows.append(row)
        except FileNotFoundError:
            return {
                "rows": [],
                "total_target": 0,
                "total_booking": 0,
                "total_installed": 0,
                "total_rejected": 0,
                "year_installed": {"2023-2024": 0, "2024-2025": 0, "2025-2026": 0},
            }

        def to_int(value):
            try:
                return int(str(value).strip() or 0)
            except ValueError:
                return 0

        total_target = sum(to_int(r.get('total_curr_target')) for r in rows)
        total_booking = sum(to_int(r.get('total_curr_Booking')) for r in rows)
        total_installed = sum(to_int(r.get('total_curr_installed')) for r in rows)
        total_rejected = sum(to_int(r.get('total_curr_Rejected')) for r in rows)

        year_installed = {
            "2023-2024": sum(to_int(r.get('2023-2024_installed')) for r in rows),
            "2024-2025": sum(to_int(r.get('2024-2025_installed')) for r in rows),
            "2025-2026": sum(to_int(r.get('2025-2026_installed')) for r in rows),
        }

        return {
            "rows": rows,
            "total_target": total_target,
            "total_booking": total_booking,
            "total_installed": total_installed,
            "total_rejected": total_rejected,
            "year_installed": year_installed,
        }

    solar_data = _load_solar_data()

    def to_int(value):
        try:
            return int(str(value).strip() or 0)
        except ValueError:
            return 0

    top_districts = sorted(
        solar_data["rows"],
        key=lambda r: to_int(r.get('total_curr_installed')),
        reverse=True
    )[:10]

    top_labels = [r.get('District') for r in top_districts]
    top_installed = [to_int(r.get('total_curr_installed')) for r in top_districts]
    top_target = [to_int(r.get('total_curr_target')) for r in top_districts]

    total_target = solar_data["total_target"]
    total_installed = solar_data["total_installed"]
    total_booking = solar_data["total_booking"]
    total_rejected = solar_data["total_rejected"]
    remaining_target = max(total_target - total_installed, 0)

    install_rate = (total_installed / total_target * 100) if total_target else 0
    reject_rate = (total_rejected / total_booking * 100) if total_booking else 0

    context = {
        "solar_total_target": f"{total_target:,}",
        "solar_total_booking": f"{total_booking:,}",
        "solar_total_installed": f"{total_installed:,}",
        "solar_reject_rate": f"{reject_rate:.1f}%",
        "solar_install_rate": f"{install_rate:.1f}%",
        "solar_year_labels": json.dumps(list(solar_data["year_installed"].keys())),
        "solar_year_installed": json.dumps(list(solar_data["year_installed"].values())),
        "solar_top_labels": json.dumps(top_labels),
        "solar_top_installed": json.dumps(top_installed),
        "solar_top_target": json.dumps(top_target),
        "solar_total_installed_value": total_installed,
        "solar_remaining_target": remaining_target,
    }

    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def buttons(request):
    return render(request, 'dashboard/buttons.html')

@login_required(login_url='login')
def cards(request):
    return render(request, 'dashboard/cards.html')

@login_required(login_url='login')
def table(request):
    return render(request, 'dashboard/table.html')

@login_required(login_url='login')
def typography(request):
    return render(request, 'dashboard/typography.html')

@login_required(login_url='login')
def icons(request):
    return render(request, 'dashboard/icons.html')

@login_required(login_url='login')
def forms(request):
    return render(request, 'dashboard/forms.html')

@login_required(login_url='login')
def areachart(request):
    return render(request, 'dashboard/charts/areachart.html')

@login_required(login_url='login')
def scatterchart(request):
    return render(request, 'dashboard/charts/scatterchart.html')

@login_required(login_url='login')
def polarareachart(request):
    return render(request, 'dashboard/charts/polarareachart.html')

@login_required(login_url='login')
def linechart(request):
    return render(request, 'dashboard/charts/linechart.html')

@login_required(login_url='login')
def barchart(request):
    return render(request, 'dashboard/charts/barchart.html')

@login_required(login_url='login')
def doughnut_piechart(request):
    return render(request, 'dashboard/charts/doughnut_piechart.html')