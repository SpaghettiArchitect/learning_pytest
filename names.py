from name_funtion import get_formatted_name


def main() -> None:
    """The main program.
    Asks for a first and last name to create a neatly formatted name.
    """
    print("Enter 'q' at any time to quit.")
    while True:
        first = input("\nPlease give me a first name: ")
        if first == "q":
            break
        last = input("Please give me a last name: ")
        if last == "q":
            break

        formatted_name = get_formatted_name(first, last)
        print(f"\tNeatly formatted name: {formatted_name}.")


if __name__ == "__main__":
    main()
