import csv
from collections import Counter

import numpy as np


filepath = r"C:\Users\biswa\Downloads\lumina_beauty.analysis_requests.csv"


def read_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def clean_data(rows):
    cleaned_rows = []

    for row in rows:
        cleaned_row = {}

        for column, value in row.items():
            if isinstance(value, str):
                value = value.strip()

            cleaned_row[column] = value

        # Keep the row if at least one cell has a value
        if any(cleaned_row.values()):
            cleaned_rows.append(cleaned_row)

    return cleaned_rows


def get_numeric_values(rows, column_name):
    values = []

    for row in rows:
        try:
            value = float(row[column_name])

            # Ignore invalid values such as NaN or infinity
            if np.isfinite(value):
                values.append(value)
        except (ValueError, KeyError, TypeError):
            pass  # Skip missing or invalid values

    return np.array(values)


data = read_csv(filepath)
data = clean_data(data)

# 1. Most frequently predicted undertone
undertones = []

for row in data:
    tone = row["detectedSkinData.undertone"]
    if tone:
        undertones.append(tone)

if undertones:
    most_common_tone, tone_count = Counter(undertones).most_common(1)[0]
    print("Most frequent predicted undertone:", most_common_tone)
    print("Number of records with this undertone:", tone_count)

# 2. Mean undertone confidence
undertone_confidence = get_numeric_values(
    data, "detectedSkinData.undertoneConfidence"
)
if len(undertone_confidence) > 0:
    print("Mean undertone confidence:", round(np.mean(undertone_confidence), 2))

# 3. Mean match confidence
match_confidence = get_numeric_values(data, "matchResult.matchConfidence")
if len(match_confidence) > 0:
    print("Mean match confidence:", round(np.mean(match_confidence), 2))

# 4. Median match confidence
if len(match_confidence) > 0:
    print("Median match confidence:", round(np.median(match_confidence), 2))

# 5. Mean number of pixels analyzed
pixels_analyzed = get_numeric_values(data, "analysisMetrics.pixelsAnalyzed")
if len(pixels_analyzed) > 0:
    print("Mean pixels analyzed:", round(np.mean(pixels_analyzed), 2))



   