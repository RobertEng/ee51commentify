# -*- coding: utf-8 -*-

# EE51 Commentify a block of text such that it has a semicolon at the
# beginning of the line and is no longer than 80 characters.

import re

def commentify():
    LINE_LENGTH = 80
    DELIMITER = '; '
    EFFECTIVE_LINE_LENGTH = LINE_LENGTH - len(DELIMITER) - 1

    fin = open('commentify_input.txt', 'r')
    open("commentify_output.txt", 'w').close()
    fout = open('commentify_output.txt', 'a')
    
    for line in fin:
        while len(line) >= EFFECTIVE_LINE_LENGTH:
            stop_index = EFFECTIVE_LINE_LENGTH
            while line[stop_index] != ' ' and stop_index > 0:
                stop_index -= 1

            # If there were no spaces in the line, just cut the line at the end
            if stop_index == 0:
                stop_index = EFFECTIVE_LINE_LENGTH

            outline = DELIMITER + line[:stop_index] + "\n"
            fout.write(outline)

            line = line[stop_index + 1:]

        # Print the rest of the line
        fout.write(DELIMITER + line)
        
def commentify2():
    LINE_LENGTH = 80
    DELIMITER = '; '
    EFFECTIVE_LINE_LENGTH = LINE_LENGTH - len(DELIMITER) - 1
    
    CATEGORIES = ["Description", "Operation", "Arguments", "Return Values", "Local Variables", "Shared Variables", "Global Variables", "Inputs", "Outputs", "Registers Used", "Stack Depth", "Error Handling", "Algorithms", "Data Structures", "Limitations", "Known Bugs", "Special Notes", "Author", "Last Modified"]
    MAX_CAT_LENGTH = len(max(CATEGORIES, key=len))
    
    LIST_CATEGORIES = ["Arguments", "Return Values", "Local Variables", "Shared Variables", "Global Variables"]
    LIST_VAR_LENGTH = 11

    fin = open('commentify_input.txt', 'r')
    open("commentify_output.txt", 'w').close()
    fout = open('commentify_output.txt', 'a')
    

    for line in fin:
        # Find if this line is a category
        for c in CATEGORIES:
            match = re.match(c.lower() + ":[ \t]*", line.lower())
            if match:
                # Add space after every category so it matches to the same indentation
                spaced_cat = match.group(0).strip() + ' ' * (MAX_CAT_LENGTH - len(c) + 1)
                line = spaced_cat + line[len(match.group(0)):]
                
                if c in LIST_CATEGORIES:
                    # Line up the list that comes after this category
                    elem = line[len(spaced_cat):]

                    # Find a match with something like
                    # str(ES:SI)  - blah blah blah
                    match = re.match("((\S)*)([ \t]*-[ \t]*)(.*)", elem)
                    # match = re.match("((\S)*)([ \t]*-[ \t]*)", elem)
                    if match:
                        e = match.group(1) + ' ' * (LIST_VAR_LENGTH - len(match.group(1)))
                        elem = e + '- ' + match.group(4)
                        line = spaced_cat + elem + "\n"

                # We found the category and have done all we need to do. Let's get out of here
                break

        while len(line) >= EFFECTIVE_LINE_LENGTH:
            stop_index = EFFECTIVE_LINE_LENGTH
            while line[stop_index] != ' ' and stop_index > 0:
                stop_index -= 1

            # If there were no spaces in the line, just cut the line at the end
            if stop_index == 0:
                stop_index = EFFECTIVE_LINE_LENGTH

            outline = DELIMITER + line[:stop_index] + "\n"
            fout.write(outline)

            line = line[stop_index + 1:]

        # Print the rest of the line
        fout.write(DELIMITER + line)

if __name__ == '__main__':
    commentify2()




