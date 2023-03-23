import re


def main():
    file_directory = file_checker()
    print(matches_counter(file_directory))


def file_checker():
    while True:
        file_directory = input("File Directory: ").strip()
        try:
            open(file_directory)
            return file_directory
        except FileNotFoundError:
            print(f"'{file_directory}' is Invalid directory name or file might not exist")


def matches_counter(file_directory):
    word_matches, character_matches = [], []
    with open(file_directory) as file:
        for line in file:
            word_matches.extend(re.findall(r"\b[a-zA-Z]+\b", line)) 
            character_matches.extend(re.findall(r"[^\s\n]", line))
    return f"Word count: {len(word_matches)}\nCharacter count: {len(character_matches)}"


if __name__ == "__main__":
    main()