import tkinter as tk
from bnd import *
import customtkinter as ctk  # type: ignore
from PIL import Image, ImageTk  # type: ignore
import io
from Book_profile import *
from keyboard import *

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

def Main_search_page(content, root):
    for widget in content.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
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
        books = showGenreBooks(genre, sectionIndex, 3)

        # If there are no books, return early
        sectionIndex += 3
        # Increment the section number if books exist
        if sectionName == "firstSectionNum":
            firstSectionNum = sectionIndex
        elif sectionName == "secondSectionNum":
            secondSectionNum = sectionIndex
        return books
    def genresButton(num, next, prev, next_x, next_y, prev_x, prev_y, anchorNext, anchorPrev, firstPrevButton, secondPrevButton, firstNextButton, secondNextButton):
        """ Controls genre navigation and resets book section numbers. """
        global genresNum, firstSectionNum, secondSectionNum
        firstSectionNum = 0
        secondSectionNum = 0
        genresNum -= num

        # Remove previous book buttons 
        for button, y, title, unavailable in book_buttons:
            button.destroy()
            title.destroy()
            if unavailable:
                unavailable.destroy()
        book_buttons.clear()  # Reset list

        # Increment genresNum to move forward
        genresNum += 2
        firstGenres = booksOutput(genres[genresNum], "firstSectionNum", 0)
        secondGenres = booksOutput(genres[genresNum + 1], "secondSectionNum", 0)
        # Print genres and books for debugging
        showBooks(secondGenres, 0.730, True)
        showBooks(firstGenres, 0.25, True)
        # Hide Prev button if at the first genre
        firstPrevButton.place_forget()
        secondPrevButton.place_forget()
        # Prevent negative index (going back too far)
        if genresNum <= 0:
            prev.place_forget()
        else:
            prev.place(relx = prev_x, rely = prev_y, anchor = anchorPrev)
        # Prevent index going forward too far
        if (genresNum + 2) >= len(genres):
            next.place_forget()
        else:
            next.place(relx=next_x, rely=next_y, anchor= anchorNext)
        if len(firstGenres) == 3:
            firstNextButton.place(relx=0.87, rely=0.25, anchor='w')
        else:
            firstNextButton.place_forget()
        if len(secondGenres) == 3:
            secondNextButton.place(relx=0.87, rely=0.75, anchor='w')
        else:
            secondNextButton.place_forget()
    def firstSection(genre, num, sectionName, nextButton, prevButton, back_x, back_y, next_x, next_y, anchor):
        """ Controls the Next and Prev navigation of books within a genre. """
        global firstSectionNum, secondSectionNum, book_buttons
        # Determine which section number to adjust
        if sectionName == "firstSectionNum":
            sectionVar = firstSectionNum
            rely_value = 0.25
        elif sectionName == "secondSectionNum":
            sectionVar = secondSectionNum
            rely_value = 0.730
        for button, y_val, title, unavailable in book_buttons:  # Iterate over a copy to avoid modification issues
            if y_val == rely_value:
                button.destroy()
                title.destroy()
                if unavailable:
                    unavailable.destroy()
            # Hide 'Prev' if at the first section
        if sectionVar - num <= 0:
            nextButton.place(relx=next_x, rely=next_y, anchor= 'w')
            prevButton.place_forget()
        else:
            print("pwede pa")
            prevButton.place(relx=back_x, rely=back_y, anchor= 'e')
        try:
            # Fetch books
            books = booksOutput(genre, sectionName, num)
            if sectionName == "firstSectionNum":
                showBooks(books, 0.25, True)
            elif sectionName == "secondSectionNum":
                showBooks(books, 0.730, True)
            if len(books) == 3:
                nextButton.place(relx=next_x, rely=next_y,anchor= 'w')
            else:
                nextButton.place_forget() # No more books, hide Next button
        except IndexError:
            prevButton.place_forget()  # Hide Prev button on error
    
    search_image = load_image("search_icon.png", size=(50, 50))
    next_image = load_image("next.png", size=(40, 40))
    back_image = load_image("back.png", size=(40, 40))
    # Create search page frame
    search_page = tk.Frame(content)
    search_page.place(relx=0, rely=0, relwidth=1, relheight=1)
    ww = search_page.winfo_screenwidth()
    wh = search_page.winfo_screenheight()
    time_border = ctk.CTkFrame(search_page, width=(0.08 * ww), height=(0.067 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    time_border.place(relx=0.89, rely=0.05)

    date_border = ctk.CTkFrame(search_page, width=(0.13 * ww), height=(0.069 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    date_border.place(relx=0.03, rely=0.05)

    def update_date():
        ph_timezone = pytz.timezone("Asia/Manila")
        current_time = datetime.now(ph_timezone)
        formatted_date = current_time.strftime("%B %d, %Y")
        formatted_time = current_time.strftime("%I:%M %p")
        date_label.configure(text=formatted_date)
        time_label.configure(text=formatted_time)
        search_page.after(1000, update_date)

    date_label = ctk.CTkLabel(date_border, font=("Arial", 24, 'bold'), text_color="Black")
    date_label.place(relx=0.5, rely=0.5, anchor = "center")

    time_label = ctk.CTkLabel(time_border, font=("Arial", 24, 'bold'), text_color="Black")
    time_label.place(relx=0.5, rely=0.5, anchor = "center")
    update_date()
    # Create a border for the search bar
    search_border = ctk.CTkFrame(search_page, width=800, height=85, fg_color='white', corner_radius=15)
    search_border.place(relx=0.5, rely=0.1, anchor='center')

    # Create the search bar entry inside the border
    search_bar = ctk.CTkEntry(search_border, width=750, height=70, corner_radius=30, bg_color='white', fg_color='white',
                              text_color="black", placeholder_text="Search bar", font=("Arial", 20))
    search_bar.place(relx=0.5, rely=0.5, anchor="center")
    search_bar.bind("<Button-1>", lambda event: open_keyboard(root, search_bar, event))
    # Frame for all books (already exists)
    books = ctk.CTkFrame(content, width=(0.8 * ww), height=650, fg_color="white", 
                      corner_radius=20, border_width=5, border_color="#5088FC")
    books.place(relx=0.5, rely=0.55, anchor="center")

    # Divider Line
    divider = ctk.CTkFrame(books, width=1000, height=2, fg_color="grey")
    divider.place(relx=0.5, rely=0.5, anchor="center")

# Navigation Buttons
    top_next_book = ctk.CTkButton(books, text='', image=next_image, bg_color="white", width=50, fg_color="white", command= lambda: firstSection(genres[genresNum], 0, "firstSectionNum", top_next_book, top_back_book, 0.13, 0.25, 0.87, 0.25, 'w'))
    top_next_book.place(relx=0.87, rely=0.25, anchor='w')

    top_back_book = ctk.CTkButton(books, text='', image=back_image, bg_color="white", width=50, fg_color="white", command = lambda: firstSection(genres[genresNum], 6, "firstSectionNum", top_next_book, top_back_book, 0.13, 0.25, 0.87, 0.25, 'e'))

    bot_next_book = ctk.CTkButton(books, text='', image=next_image, bg_color="white", width=50, fg_color="white", command=lambda: firstSection(genres[genresNum + 1], 0, "secondSectionNum", bot_next_book, bot_back_book, 0.13, 0.75, 0.87, 0.75, 'w'))
    bot_next_book.place(relx=0.87, rely=0.75, anchor='w')

    bot_back_book = ctk.CTkButton(books, text='', image=back_image, bg_color="white", width=50, fg_color="white", command=lambda: firstSection(genres[genresNum + 1], 6, "secondSectionNum", bot_next_book, bot_back_book, 0.13, 0.75, 0.87, 0.75, 'e'))

    genre_next_button = ctk.CTkButton(books, text='', image=next_image, bg_color="white", width=50, fg_color="white", command = lambda: genresButton(0, genre_next_button, genre_back_button, 0.97, 0.05, 0.93, 0.05, "ne", "ne", top_back_book, bot_back_book, top_next_book, bot_next_book))
    genre_next_button.place(relx=0.97, rely=0.05, anchor='ne')

    genre_back_button = ctk.CTkButton(books, text='', image= back_image, bg_color="white", width=50, fg_color="white", command = lambda: genresButton(4, genre_next_button, genre_back_button, 0.97, 0.05, 0.93, 0.05, "ne", "ne", top_back_book, bot_back_book, top_next_book, bot_next_book))
# Books (placed where they were inside `top_books` and `bot_books`)
    def showBooks(bookArray, y, forGenre):
            # Keep track of book buttons and labels globally
        global book_buttons, genre_labels

    # Remove previous genre labels
        for label in genre_labels:
            label.destroy()
        genre_labels.clear()  # Reset list
        positions = [(0.2, y), (0.5, y), (0.8, y)] # Positions for top books
        if forGenre:
            top_label = ctk.CTkLabel(books, text=genres[genresNum], font=("Arial", 28, "bold"), text_color="grey")
            top_label.place(relx=0.05, rely=0.060, anchor="w")
            bot_label = ctk.CTkLabel(books, text=genres[genresNum + 1], font=("Arial", 28, "bold"), text_color="grey")
            bot_label.place(relx=0.05, rely=0.53, anchor="w")
            genre_labels.extend([top_label, bot_label])
        for i, (id, blob, title, availability) in enumerate(bookArray):
            try:
                # Load image from binary data
                image = Image.open(io.BytesIO(blob)).resize((136, 205))
                ctk_image = ctk.CTkImage(light_image=image, size=(136, 205))
            except Exception as e:
                print(f"Error loading image {i}: {e}")
                continue
            
            # Create book button
            book_button = ctk.CTkButton(
                books, image=ctk_image, compound="top", text= "",
                fg_color="white", hover_color="lightblue", command = lambda id=id: book_profile(content, id)
            )
            titleLabel = ctk.CTkLabel(books, text=title, font=("Poppins", 12.5, "bold"), text_color="black", wraplength=300)
            titleLabel.place(relx=positions[i][0], rely=(positions[i][1])+0.185, anchor="center")
            if availability == 0:
                unavailableBox = ctk.CTkFrame(books, width=150, height=20, fg_color="#8c1c2d", corner_radius= 50)
                unavailableBox.place(relx=positions[i][0], rely=(positions[i][1])+0.225, anchor="center")
                unavailableText = ctk.CTkLabel(unavailableBox, text="Currently Unavailable", font=("Poppins", 12.5, "bold"), text_color="white", wraplength=300, height= 10)
                unavailableText.place(relx=0.5, rely=0.5, anchor="center")
            # Place button using predefined positions
            book_button.place(relx=positions[i][0], rely=(positions[i][1]), anchor="center")
            book_button.image = ctk_image  # Keep reference to prevent garbage collection
            book_buttons.append((book_button, y, titleLabel, unavailableBox))
            # Fetch books from two genres
    firstGenres = booksOutput(genres[genresNum], "firstSectionNum", 0)
    secondGenres = booksOutput(genres[genresNum + 1], "secondSectionNum", 0)
    # Print genres and books for debugging
    showBooks(secondGenres, 0.730, True)
    showBooks(firstGenres, 0.25, True)

    ### SA MAY LITERAL NA SEARCH NAMAN ############
    def searchTitle(searchedItem, num):
        for widget in books.winfo_children():
            widget.destroy()

        searchNum = num  # Unused in current code, can be removed if unnecessary
        bookArray = searchBooks("Title", searchedItem, 6, searchNum)
        print(" ######, ",(searchNum + 6), searchNum )

    # Show first 3 books (if available)
        print("length of the books Searched: ", len(bookArray))
        showBooks(bookArray[0: 3], 0.25, False)
        if len(bookArray) > 3:
            print("extending")
            showBooks(bookArray[3: 6], 0.730, False)
        if len(bookArray) >= 6:
            search_next_button = ctk.CTkButton(books, text='', image=next_image, bg_color="white", width=50, fg_color="white", command= lambda: searchTitle(searchedItem, (searchNum + 6)))
            search_next_button.place(relx=0.97, rely=0.05, anchor='ne')
        if searchNum >= 6:
            search_back_button = ctk.CTkButton(books, text='', image= back_image, bg_color="white", width=50, fg_color="white", command= lambda: searchTitle(searchedItem, (searchNum - 6)))
            search_back_button.place(relx=0.93, rely=0.05, anchor='ne')
    def enterSearch():
        close()
        input = search_bar.get()
        searchTitle(input, 0)
    search_button = ctk.CTkButton(search_bar, text='', image=search_image, width=75, fg_color='white', command=enterSearch)
    search_button.place(relx=0.98, rely=0.5, anchor='e')