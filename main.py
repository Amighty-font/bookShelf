import bookFinder
import bookInfo
from BookShelf import BookShelf

to_read = BookShelf()
completed = BookShelf()
command = ""
running = True


def display_menu():
    print("Select from: ")
    print("a -> add to shelf")
    print("r -> remove from shelf")
    print("v -> view shelf")
    print("l -> lookup book")
    print("q -> quit")


def addToShelf():
    bk = findBook()
    print("What bookshelf would you like to add to? ")
    add_command = input("To-Read or Completed? (t/c) ")
    if add_command == "t":
        to_read.add_book(bk)
    elif add_command == "c":
        completed.add_book(bk)
    else:
        print("ruh-roh")


def removeFromShelf():
    print("What bookshelf would you like to remove from? ")
    remove_command = input("To-Read or Completed? (t/c) ")
    remove_title = input("Input the title of the book to remove: ")
    remove_author = input("Input the author of the book to remove: ")
    if remove_command == "t":
        to_read.remove_book(remove_title, remove_author)
    elif remove_command == "c":
        completed.remove_book(remove_title, remove_author)
    else:
        print("ruh-roh")


def viewShelf():
    print("To-Read: ")
    to_read.print_shelf()
    print("")
    print("Completed: ")
    completed.print_shelf()
    print("")


def findBook():
    val = input("Book Name: ")
    found_book = bookInfo.getInfo(val)
    print(found_book.get_author())
    ans = input("Is this the correct author? (y/n) ")
    while ans != "y":
        inp = input("State correct author: ")
        check = found_book.get_title() + " " + inp
        found_book = bookInfo.getInfo(check)
        print(found_book.get_author())
        ans = input("IS this the correct author? (y/n) ")
    return found_book


def lookUp():
    bk = findBook()
    print(bk.get_title())
    print(bk.get_author())
    print("Book Rating of: " + bk.get_rating() + " with " + bk.get_num_ratings())


def process_command(given_command):
    if given_command == "a":
        addToShelf()
    elif given_command == "r":
        removeFromShelf()
    elif given_command == "v":
        viewShelf()
    elif given_command == "l":
        lookUp()
    else:
        print("ruh-roh")


while running:
    display_menu()
    command = input("What would you like to do? ")
    if command == "q":
        break
    process_command(command)
