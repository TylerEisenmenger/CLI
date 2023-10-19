import sys

# Command line arguments are passed into Python as a list of strings in sys.argv
def main():
    # Check if there are command line arguments
    # There will always be one: the script name
    if len(sys.argv) > 1:
        length = 0
        for arg in sys.argv[1:]:
            length += len(arg)
        print("You entered", len(sys.argv) - 1, "command line arguments.")
        print("The average number of characters per argument is", length / (len(sys.argv) - 1), ".")
    else:
        print("No command line arguments were given.")

if __name__ == "__main__":
    main()





