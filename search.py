import tkinter as tk
from bnd import *

# GLOBAL VARIABLES HERE
firstSectionNum = 0
secondSectionNum = 0
genresNum = 0
showButton = True
genres = ["Philosophy & Psychology", "Technology", "Religion", "Social Sciences", "Languages", "Science", "Literature", "Arts & Recreation", "History & Geography", "General Knowledge"]

def Main_search_page(content):
    global firstSectionNum
    global genresNum
    global genres
    global secondSectionNum

    firstSectionNum = 0
    secondSectionNum = 0
    genresNum = 0

    search_page = tk.Frame(content)
    search_page.place(x=0, y=0, width=1720, height=1080)
    entry = tk.Entry(search_page, width=75)
    entry.place(x=300, y=300)
    search_page.tkraise()

    def enterSearch():
        input = entry.get()
        print(searchBooks("Title", input))

    def booksOutput(genre, sectionName , num):
        """ Fetch and return books for the given genre and section. """
        global firstSectionNum, secondSectionNum
        
        # Determine the section to fetch from
        if sectionName == "firstSectionNum":
            sectionIndex = firstSectionNum
        else:
            sectionIndex = secondSectionNum

        # Get books
        sectionIndex -= num
        books = showGenreBooks(genre, sectionIndex, sectionIndex + 3)

        # If there are no books, return early
        if not books:
            return None
        sectionIndex += 3
        # Increment the section number if books exist
        if sectionName == "firstSectionNum":
            firstSectionNum = sectionIndex
        else:
            secondSectionNum = sectionIndex
        print("PRESSED")
        return books

    def firstSection(genre, num, sectionName, nextButton, prevButton, x, y):
        """ Controls the Next and Prev navigation of books within a genre. """
        global firstSectionNum, secondSectionNum

        # Determine which section number to adjust
        if sectionName == "firstSectionNum":
            sectionVar = firstSectionNum
        else:
            sectionVar = secondSectionNum

        # Prevent negative index (going back too far)
        if sectionVar - num < 0:
            prevButton.place_forget()
            return
        else: 
            prevButton.place(x=x, y=y)
        try:
            print(sectionVar)
            # Fetch books
            books = booksOutput(genre, sectionName, num)
            print(books)
            if books == 3:
                # Ensure the Next button remains visible if more books exist
                if not nextButton.winfo_ismapped():
                    nextButton.place(x=x, y=y)
            else:
                nextButton.place_forget()  # No more books, hide Next button

            # Hide 'Prev' if at the first section
            if sectionVar == 0:
                prevButton.place_forget()
            else:
                if not prevButton.winfo_ismapped():
                    prevButton.place(x=x, y=y)

        except IndexError:
            prevButton.place_forget()  # Hide Prev button on error

    def genresButton(num, button, altButton, x, y, prevButton):
        """ Controls genre navigation and resets book section numbers. """
        global genresNum, firstSectionNum, secondSectionNum

        firstSectionNum = 0
        secondSectionNum = 0

        # Prevent negative index (going back too far)
        if genresNum - num < 0:
            button.place_forget()
            return

        try:
            genresNum -= num

            # Fetch books from two genres
            firstGenres = booksOutput(genres[genresNum], "firstSectionNum", 0)
            secondGenres = booksOutput(genres[genresNum + 1], "secondSectionNum", 0)

            # Print genres and books for debugging
            print(genres[genresNum], firstGenres, 0)
            print(genres[genresNum + 1], secondGenres, 0)

            # Increment genresNum to move forward
            genresNum += 2

            # Hide Prev button if at the first genre
            prevButton.place_forget()

            # Ensure the Next button remains visible if more genres exist
            if not altButton.winfo_ismapped():
                altButton.place(x=x, y=y)

        except IndexError:
            button.place_forget()

    # UI Components
    label1_text = tk.StringVar()
    label2_text = tk.StringVar()

    label1 = tk.Label(search_page, textvariable=label1_text)
    label1.place(x=425, y=250)
    label2 = tk.Label(search_page, textvariable=label2_text)
    label2.place(x=300, y=300)

    # Book Navigation Buttons
    firstNextButton = tk.Button(
        search_page, text="Next", 
        command=lambda: firstSection(genres[genresNum - 2], 0, "firstSectionNum", firstNextButton, firstPrevButton, 400, 400)
    )
    firstNextButton.place(x=500, y=400)

    firstPrevButton = tk.Button(
        search_page, text="Prev", 
        command=lambda: firstSection(genres[genresNum - 2], 6, "firstSectionNum", firstPrevButton, firstNextButton, 500, 400)
    )
    firstPrevButton.place(x=400, y=400)

    # Genre Navigation Buttons
    genreNextButton = tk.Button(
        search_page, text="Next Genre", 
        command=lambda: genresButton(0, genreNextButton, genrePrevButton, 400, 500, firstPrevButton)
    )
    genreNextButton.place(x=500, y=500)

    genrePrevButton = tk.Button(
        search_page, text="Prev Genre", 
        command=lambda: genresButton(4, genrePrevButton, genreNextButton, 500, 500, firstPrevButton)
    )
    genrePrevButton.place(x=400, y=500)

    # Initialize first genre view
    genresButton(0, genreNextButton, genrePrevButton, 400, 500, firstPrevButton)
