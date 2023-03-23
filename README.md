# Word-counter

This Python program defines three functions:** main()**, **file_checker()**, and **matches_counter()**.

The program begins by importing the regular expression module, re.

The **main()** function serves as the program's entry point. It calls **file_checker()** to get a valid file directory from the user, then passes that directory to **matches_counter()** and prints the function's returned value.

The **file_checker()** function prompts the user for a file directory and attempts to open the file at that location. If the file does not exist or the directory is invalid, the function prints an error message and continues prompting the user for a valid directory.

The **matches_counter()** function takes a file directory as an argument and returns a string with the count of words and characters in the file. The function opens the file and reads its contents line by line, using regular expressions to find word and character matches. It then returns a string formatted with the counts of the word and character matches.

Overall, this program prompts the user for a file directory, reads the contents of the file at that location, and returns the number of words and characters in the file.

It is important to note that the regular expressions used in this program are limited to English alphabet letters only. If the file contains non-English characters, the word and character counts may not be accurate.
