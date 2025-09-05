#Grace Hechavarria
#09/05/2025

def main():
    user_input = input("Enter a string: ")
    chars = [c for c in user_input if c != ' ']
    sorted_chars = sorted(chars)
    print(''.join(sorted_chars))  # Output characters alphabetically on the same line

if __name__ == "__main__":
    main()