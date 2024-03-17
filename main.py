from match import Match

def main():
    # Instantiate Match object with the CSV file path
    csv_file_path = "path/to/your/csv_file.csv"
    match = Match(csv_file_path)
    
    # Read CSV file and preprocess data
    match.read_csv()
    match.preprocess_data()
    
    # Generate graphs
    match.generate_graphs()

if __name__ == "__main__":
    main()
