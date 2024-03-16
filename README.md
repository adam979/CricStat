# CricStat

CricStat is a Python project designed to analyze and visualize cricket match data stored in CSV files. It provides tools to preprocess the data, generate various graphs, and gain insights into the performance of teams and players.

## Features

- Read CSV files containing cricket match data.
- Preprocess the data by converting overs to balls and handling missing values.
- Plot score progression over deliveries for each innings.
- Calculate and plot run rate over time for each innings.
- Customize the appearance of plots for better visualization.
- Store data of each match in separate CSV files.

## File Structure

- **match.py**: Contains the `Match` class, which provides methods for reading CSV files, preprocessing data, and generating graphs.
- **plotting_utils.py**: Includes utility functions to customize the appearance of plots.
- **data/**: Directory to store CSV files containing cricket match data.
- **main.py**: The main script to execute the project. It imports the `Match` class from `match.py` and demonstrates how to use it.

## Usage

1. **Installation**: Clone the repository to your local machine.

    ```bash
    git clone https://github.com/your_username/CricStat.git

2. **Data Preparation**: Place your CSV files containing cricket match data in the `data/` directory.

## Adding New Plotting Functions
When creating a new plotting function in match.py, follow these steps:

1. Define the function in match.py to generate the desired plot.
2. If styling is needed, create a corresponding function in plotting_utils.py to customize the appearance of the plot.
3. Import the necessary functions from plotting_utils.py into match.py.
4. Call the styling function from plotting_utils.py within the new plotting function in match.py
