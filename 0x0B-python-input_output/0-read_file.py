def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    # Use the with statement to open the file in read mode
    with open(filename, "r", encoding="utf-8") as f:
        # Loop through each line in the file
        for line in f:
            # Print the line to stdout, end="" prevents adding a new line
            print(line, end="")
