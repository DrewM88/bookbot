
def getContentsFromFile(path):
    with open(path) as f:
        return f.read()

def countWords(text):
    words = text.split()
    wordCount = 0
    for word in words:
        wordCount += 1
    return wordCount

def countLetters(text):
    lower_text = text.lower()
    letterCounts = {}

    for char in lower_text:
        if char in letterCounts:
            letterCounts[char] += 1
        else:
            letterCounts[char] = 1

    return letterCounts


def sort_on(dict):
    return dict["number"]

def printReport(wordCount, charDict, path):

    charList = []

    for char in charDict:
        if char.isalpha():
            charList.append({"letter": char, "number": charDict[char]})

    charList.sort(reverse=True, key=sort_on)

    
    print(f"--- Begin report of {path} ---")
    print(f"{wordCount} words found in the document")

    for character in charList:
        print(f"The '{character['letter']}' character was found {character['number']} times")

    print('--- End report ---')


def main():
    path = "books/frankenstein.txt"
    book_text = getContentsFromFile(path)
    # print(book_text)
    word_count = countWords(book_text)
    char_dictionary = countLetters(book_text)

    printReport(word_count, char_dictionary, path)

main()