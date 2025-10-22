from customtkinter import *

def draw_books(master, books):
    """
    Draws book frames on the master CTkFrame using grid layout.
    Each row can contain at most 4 book frames.

    Args:
        master (CTkFrame): The parent frame where books will be displayed.
        books (list[CTkFrame]): A list of CTkFrame objects representing books.
    """
    # Clear any existing widgets inside master
    for widget in master.winfo_children():
        widget.grid_forget()

    max_per_row = 4

    for index, book in enumerate(books):
        row = index // max_per_row
        col = index % max_per_row

        # Place book in grid
        book.grid(row=row, column=col, padx=10, pady=10) #sticky="nsew")

    # Make grid cells expand equally
    # total_rows = (len(books) + max_per_row - 1) // max_per_row
    # for r in range(total_rows):
    #     master.rowconfigure(r, weight=1)
    # for c in range(max_per_row):
    #     master.columnconfigure(c, weight=1)

if __name__ == "__main__":
    app = CTk()
    app.geometry("800x600")

    main_frame = CTkFrame(app)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Example: creating dummy book frames
    books = []
    for i in range(10):
        frame = CTkFrame(main_frame, width=150, height=200, corner_radius=10)
        CTkLabel(frame, text=f"Book {i+1}").pack(pady=10)
        books.append(frame)

    # Draw them
    draw_books(main_frame, books)

    app.mainloop()



