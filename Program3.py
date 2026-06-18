def library_search(Id):
    library = {
        11: "Home coming",
        22: "Far away from Home",
        33: "No Way Home",
        44: "Brand New Day",
        55: "Dark of Night"
    }

    if Id in library:
        print("Your book is -", library[Id])
    else:
        print("The book is not found")

library_search(33)