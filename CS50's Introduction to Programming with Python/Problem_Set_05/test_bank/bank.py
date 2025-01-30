def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    clean = greeting.strip().lower()
    if clean.startswith("hello") == True:
        return "$0"
    elif clean[0] == "h":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
