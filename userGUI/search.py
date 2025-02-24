import tkinter as tk
from bnd import *
import customtkinter as ctk  # type: ignore
from PIL import Image, ImageTk  # type: ignore
import io


# GLOBAL VARIABLES HERE
firstSectionNum = 0
secondSectionNum = 0
genresNum = 0
showButton = True
book_buttons = []
genre_labels = []
genres = ["Philosophy & Psychology", "Technology", "Religion", "Social Sciences", "Languages", "Science", "Literature", "Arts & Recreation", "History & Geography", "General Knowledge"]

def load_image(filename, size=(50, 50)):
    try:
        with open(filename, "rb") as file:
            image_bytes = file.read()
        pil_image = Image.open(io.BytesIO(image_bytes))
        return ctk.CTkImage(pil_image, size=size)
    except Exception as e:
        print(f"Error loading image {filename}: {e}")
        return None

def Main_search_page(content):
    global firstSectionNum
    global genresNum
    global genres
    global secondSectionNum

    firstSectionNum = 0
    secondSectionNum = 0
    genresNum = 0

    # Load images with full path
    def booksOutput(genre, sectionName , num):
        """ Fetch and return books for the given genre and section. """
        global firstSectionNum, secondSectionNum
        
        # Determine the section to fetch from
        if sectionName == "firstSectionNum":
            sectionIndex = firstSectionNum
        elif sectionName == "secondSectionNum":
            sectionIndex = secondSectionNum

        # Get books
        sectionIndex -= num
        books = showGenreBooks(genre, sectionIndex, sectionIndex + 3)

        # If there are no books, return early
        sectionIndex += 3
        # Increment the section number if books exist
        if sectionName == "firstSectionNum":
            firstSectionNum = sectionIndex
        elif sectionName == "secondSectionNum":
            secondSectionNum = sectionIndex
        print("PRESSED")
        return books
    def genresButton(num, next, prev, next_x, next_y, prev_x, prev_y, anchorNext, anchorPrev, firstPrevButton, secondPrevButton):
        """ Controls genre navigation and resets book section numbers. """
        global genresNum, firstSectionNum, secondSectionNum
        firstSectionNum = 0
        secondSectionNum = 0
        genresNum -= num

        # Remove previous book buttons
        for button in book_buttons:
            button.destroy()
        book_buttons.clear()  # Reset list
        
        # Fetch books from two genres
        firstGenres = booksOutput(genres[genresNum], "firstSectionNum", 0)
        secondGenres = booksOutput(genres[genresNum + 1], "secondSectionNum", 0)
        # Print genres and books for debugging
        showBooks(secondGenres, 0.775)
        showBooks(firstGenres, 0.30)
        # Increment genresNum to move forward
        genresNum += 2

        # Hide Prev button if at the first genre
        firstPrevButton.place_forget()
        secondPrevButton.place_forget()
        # Prevent negative index (going back too far)
        if genresNum <= 2:
            prev.place_forget()
        else:
            prev.place(relx = prev_x, rely = prev_y, anchor = anchorPrev)
        # Prevent index going forward too far
        if genresNum >= len(genres):
            next.place_forget()
        else:
            next.place(relx=next_x, rely=next_y, anchor= anchorNext)
        print(genresNum)
    
    def firstSection(genre, num, sectionName, nextButton, prevButton, x, y, anchor):
        """ Controls the Next and Prev navigation of books within a genre. """
        global firstSectionNum, secondSectionNum
        print("INITIATED")
        # Determine which section number to adjust
        if sectionName == "firstSectionNum":
            sectionVar = firstSectionNum
            print(sectionName)
        elif sectionName == "secondSectionNum":
            sectionVar = secondSectionNum
            print(sectionName)

        # Prevent negative index (going back too far)
        if sectionVar - num < 0:
            prevButton.place_forget()
            return
        else: 
            prevButton.place(relx=x, rely=y, anchor= anchor)
        try:
            print(sectionVar)
            # Fetch books
            books = booksOutput(genre, sectionName, num)
            showBooks(books)
            if books == 3:
                # Ensure the Next button remains visible if more books exist
                if not nextButton.winfo_ismapped():
                    nextButton.place(relx=x, rely=y, anchor= anchor)
            else:
                nextButton.place_forget()  # No more books, hide Next button

            # Hide 'Prev' if at the first section
            if sectionVar == 0:
                prevButton.place_forget()
            else:
                if not prevButton.winfo_ismapped():
                    prevButton.place(relx=x, rely=y, anchor= anchor)

        except IndexError:
            prevButton.place_forget()  # Hide Prev button on error
    search_image = load_image("search_icon.png", size=(50, 50))
    next_image = load_image("next.png", size=(40, 40))
    back_image = load_image("back.png", size=(40, 40))
    # Create search page frame
    search_page = tk.Frame(content)
    search_page.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Create a border for the search bar
    search_border = ctk.CTkFrame(search_page, width=800, height=85, fg_color='white', corner_radius=15)
    search_border.place(relx=0.5, rely=0.1, anchor='center')

    # Create the search bar entry inside the border
    search_bar = ctk.CTkEntry(search_border, width=750, height=70, corner_radius=30, bg_color='white', fg_color='white',
                              text_color="black", placeholder_text="Search bar", font=("Arial", 20))
    search_bar.place(relx=0.5, rely=0.5, anchor="center")

    # Create the search button inside the search bar
    search_button = ctk.CTkButton(search_bar, text='', image=search_image, width=75, fg_color='white')
    search_button.place(relx=0.98, rely=0.5, anchor='e')

    # Frame for all books (already exists)
    books = ctk.CTkFrame(content, width=1400, height=650, fg_color="white", 
                      corner_radius=20, border_width=15, border_color="DeepSkyBlue3")
    books.place(relx=0.5, rely=0.55, anchor="center")

# Divider Line
    divider = ctk.CTkFrame(books, width=1000, height=2, fg_color="grey")
    divider.place(relx=0.5, rely=0.5, anchor="center")

# Navigation Buttons
    top_next_book = ctk.CTkButton(books, text='', image=next_image, bg_color="white", width=50, fg_color="white", command= lambda: firstSection(genres[genresNum - 2], 0, "firstSectionNum", top_next_book, top_back_book, 0.13, 0.25, 'w'))
    top_next_book.place(relx=0.87, rely=0.25, anchor='e')

    top_back_book = ctk.CTkButton(books, text='', image=back_image, bg_color="white", width=50, fg_color="white", command = lambda: firstSection(genres[genresNum - 2], 6, "firstSectionNum", top_next_book, top_back_book, 0.87, 0.25, 'e'))
    top_back_book.place(relx=0.13, rely=0.25, anchor='w')

    bot_next_book = ctk.CTkButton(books, text='', image=next_image, bg_color="white", width=50, fg_color="white", command=lambda: firstSection(genres[genresNum - 1], 0, "secondSectionNum", bot_next_book, bot_back_book, 0.13, 0.75, 'w'))
    bot_next_book.place(relx=0.87, rely=0.75, anchor='e')

    bot_back_book = ctk.CTkButton(books, text='', image=back_image, bg_color="white", width=50, fg_color="white", command=lambda: firstSection(genres[genresNum - 1], 6, "secondSectionNum", bot_next_book, bot_back_book, 0.87, 0.75, 'e'))
    bot_back_book.place(relx=0.13, rely=0.75, anchor='w')

    genre_next_button = ctk.CTkButton(books, text='', image=next_image, bg_color="white", width=50, fg_color="white", command = lambda: genresButton(0, genre_next_button, genre_back_button, 0.97, 0.05, 0.93, 0.05, "ne", "ne", top_back_book, bot_back_book))
    genre_next_button.place(relx=0.97, rely=0.05, anchor='ne')

    genre_back_button = ctk.CTkButton(books, text='', image=next_image, bg_color="white", width=50, fg_color="white", command = lambda: genresButton(4, genre_next_button, genre_back_button, 0.97, 0.05, 0.93, 0.05, "ne", "ne", top_back_book, bot_back_book))
    genre_back_button.place(relx=0.93, rely=0.05, anchor='ne')
# Books (placed where they were inside `top_books` and `bot_books`)
    def showBooks(bookArray, y):
            # Keep track of book buttons and labels globally
        global book_buttons, genre_labels

    # Remove previous genre labels
        for label in genre_labels:
            label.destroy()
        genre_labels.clear()  # Reset list
        positions = [(0.2, y), (0.5, y), (0.8, y)]  # Positions for top books
        top_label = ctk.CTkLabel(books, text=genres[genresNum], font=("Arial", 28, "bold"), text_color="grey")
        top_label.place(relx=0.05, rely=0.060, anchor="w")
        bot_label = ctk.CTkLabel(books, text=genres[genresNum + 1], font=("Arial", 28, "bold"), text_color="grey")
        bot_label.place(relx=0.05, rely=0.53, anchor="w")
        genre_labels.extend([top_label, bot_label])
        for i, (blob, title) in enumerate(bookArray):
            try:
                # Load image from binary data
                image = Image.open(io.BytesIO(blob)).resize((136, 205))
                ctk_image = ctk.CTkImage(light_image=image, size=(136, 205))
            except Exception as e:
                print(f"Error loading image {i}: {e}")
                continue
            
            # Create book button
            book_button = ctk.CTkButton(
                books, text=title, image=ctk_image, compound="top", 
                fg_color="white", hover_color="lightblue", text_color="midnightblue", 
                font=("Arial", 25, "bold")
            )
            
            # Place button using predefined positions
            book_button.place(relx=positions[i][0], rely=positions[i][1], anchor="center")
            book_button.image = ctk_image  # Keep reference to prevent garbage collection
            
            book_buttons.append(book_button)
    genresButton(0, genre_next_button, genre_back_button, 0.97, 0.05, 0.93, 0.05, "ne", "ne", top_back_book, bot_back_book)
    ### LOGICCCCCCCCC ############
