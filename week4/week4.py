def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\nOriginal Content Read Successfully.")
        
        modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"Modified content written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# User interaction
def main():
    print("📁 File Read & Write Challenge + 🧪 Error Handling Lab")
    input_filename = input("Enter the name of the file to read from: ")
    output_filename = input("Enter the name of the file to write to: ")

    read_and_modify_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
