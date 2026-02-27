from collections import defaultdict

def calculate_descriptive_metrics(data):
    district_data = defaultdict(list)

    # Group by district
    for row in data:
        district_data[row["district"]].append(row)

    results = []

    for district, records in district_data.items():
        total_eff = 0
        total_target_rate = 0
        total_rejection = 0
        count = 0

        for r in records:
            if r["booking"] > 0:
                eff = r["installed"] / r["booking"]
                rejection = r["rejected"] / r["booking"]
            else:
                eff = 0
                rejection = 0

            if r["target"] > 0:
                target_rate = r["installed"] / r["target"]
            else:
                target_rate = 0

            total_eff += eff
            total_target_rate += target_rate
            total_rejection += rejection
            count += 1

        avg_eff = total_eff / count if count else 0
        avg_target_rate = total_target_rate / count if count else 0
        avg_rejection = total_rejection / count if count else 0

        # Combined Score
        score = (0.4 * avg_eff) + (0.4 * avg_target_rate) + (0.2 * (1 - avg_rejection))

        # Classification
        if score >= 0.75:
            category = "High"
        elif score >= 0.55:
            category = "Moderate"
        else:
            category = "Low"

        results.append({
            "district": district,
            "avg_efficiency": round(avg_eff, 3),
            "avg_target_rate": round(avg_target_rate, 3),
            "avg_rejection": round(avg_rejection, 3),
            "score": round(score, 3),
            "category": category
        })

    # Sort by score descending
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results
