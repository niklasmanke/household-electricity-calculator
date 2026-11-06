
# Household Electricity Consumption Calculator

A Python application to calculate, analyze, and visualize household electricity consumption.

## Features

- Add and remove electrical appliances
- Calculate electricity consumption in kWh
- Estimate electricity costs
- Calculate each appliance's share of total consumption
- Identify appliances with the highest and lowest consumption
- Save and load appliance data using CSV files
- Visualize consumption using Matplotlib

## Technologies

- Python
- CSV
- Matplotlib
- pytest


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/niklasmanke/household-electricity-calculator.git
```

### 2. Navigate to the project directory

```bash
cd household-electricity-calculator
```

### 3. Install the required packages

Make sure Python is installed, then run:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python stromverbrauchsrechner.py
```

The application allows users to add appliances, calculate their electricity consumption, and visualize the results.

A CSV file is created automatically when appliance data is saved for the first time.


## Usage

Run the application:

```bash
python stromverbrauchsrechner.py
```

## Testing

Run automated tests:

```bash
python -m pytest -v
```
