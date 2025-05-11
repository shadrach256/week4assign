def file_processor():
    # Get input filename with error handling
    while True:
        input_filename = input("Enter the name of the file to read: ")
        try:
            with open(input_filename, 'r') as file:
                content = file.read()
            break
        except FileNotFoundError:
            print(f"Error: File '{input_filename}' not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied when trying to read '{input_filename}'. Please try another file.")
        except IOError as e:
            print(f"Error: Unable to read file '{input_filename}'. {str(e)}")

    # Process the content (convert to uppercase in this example)
    modified_content = content.upper()

    # Get output filename with validation
    while True:
        output_filename = input("Enter the name of the output file: ")
        if output_filename.strip() == "":
            print("Error: Output filename cannot be empty.")
            continue
        if output_filename == input_filename:
            print("Error: Output file cannot be the same as input file.")
            continue
        
        try:
            with open(output_filename, 'x') as file:  # 'x' mode fails if file exists
                file.write(modified_content)
            print(f"Success! Modified content written to '{output_filename}'")
            break
        except FileExistsError:
            print(f"Error: File '{output_filename}' already exists. Please choose a different name.")
        except PermissionError:
            print(f"Error: Permission denied when trying to write to '{output_filename}'.")
        except IOError as e:
            print(f"Error: Unable to write to file '{output_filename}'. {str(e)}")

if __name__ == "__main__":
    print("=== File Processing Program ===")
    print("This program will read a file, modify its content,")
    print("and write the modified version to a new file.\n")
    
    file_processor()