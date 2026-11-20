Skin Tone Analysis CSV Project

A beginner Python project that reads and cleans a CSV export of skin tone analysis requests, then summarizes selected results with NumPy.

## What the program does

- Reads CSV rows using Python's built-in `csv.DictReader`.
- Trims extra spaces from values and skips completely blank rows.
- Skips missing or invalid numeric values when calculating statistics.
- Reports the most frequently predicted undertone, mean undertone confidence, mean and median match confidence, and mean pixels analyzed.

These are summaries of the values recorded by the analysis system. They do not measure prediction accuracy: the feedback columns (`feedbackData.userConfirmed`, `feedbackData.userFeedback`, and `feedbackData.actualShadeUsed`) are empty in the provided dataset.

## Requirements

- Python 3
- NumPy

Install NumPy from a terminal:

```bash
python -m pip install numpy
```

## Set up the CSV path

The program expects the downloaded CSV file to be available locally. Open `main.py` and update `filepath` to the location of your file. For example:

```python
filepath = r"C:\Users\your-name\Downloads\lumina_beauty.analysis_requests.csv"
```

Keep the `r` before the quoted Windows path so backslashes are read correctly. The dataset is not included in this repository; download it from its source and check its license before using it.

## Run

From the project folder, run:

```bash
python main.py
```

The summary values will be printed in the terminal.

## Statistics reported

1. Most frequent predicted undertone and its record count
2. Mean undertone confidence
3. Mean match confidence
4. Median match confidence
5. Mean number of pixels analyzed

## Data privacy

Do not upload the raw CSV to a public repository without checking that you have permission to share it. The dataset contains session identifiers and user-agent information. Keep the dataset local or remove identifying fields before sharing it.
