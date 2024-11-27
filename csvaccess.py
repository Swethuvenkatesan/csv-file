import csv
import os

def read_csv_file(filename):
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")

        # Open and read the CSV file
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            
            # Read and print header row
            header = next(reader, None)
            print(f"Header: {header}")

            # Process each row
            for row in reader:
                if len(row) >= 3:  # Ensure sufficient columns exist
                    name, age, company = row[0], row[1], row[2]
                    print(f"Name: {name}, Age: {age}, comapny: {company}")
                else:
                    print(f"Skipping incomplete row: {row}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print(f"Error: Permission denied for the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function with the specified file
read_csv_file('data.csv') 