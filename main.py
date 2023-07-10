import Calculator
import BookStore
import DLList


def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    # variables = {}  # dictionary to store variable-value pairs

    while option != '0':
        print("""
        1 Check mathematical expression
        2 Store variable values
        3 Print expression with values
        4 Evaluate expression
        0 Return to main menu
        """)
        option = input()

        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")

        elif option == "2":
            indic = True
            while indic:
                variable = input("Enter a variable: ")
                value = input("Enter its value: ")
                calculator.set_variable(variable, float(value))
                # variables[variable] = value
                answer = input("Enter another variable? Y/N: ")
                if answer.upper() == "N":
                    indic = False

        elif option == "3":
            expression = input("Introduce the mathematical expression: ")
            if not calculator.matched_expression(expression):
                print("Invalid expression")
                continue
            calculator.print_expression(expression)

        elif option == "4":
            expression = input("Enter the expression: ")
            try:
                result = calculator.evaluate(expression)
                print(f"Result: {result}")
            except ValueError:
                print("Result: Error - Not all variable values are defined.")


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        10 Sort the catalog
        11 Display the first n books of catalog
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)
        elif option == "6":
            print(bookStore.getCartBestSeller())
        elif option == "7":
            key = input("Enter book key: ")
            temp = bookStore.addBookByKey(key)
            if temp is not None:
                print(f"Added title: {temp}")
            else:
                print("Book not found.")
        elif option == "8":
            prefix = input("Enter a prefix: ")
            temp = bookStore.addBookByPrefix(prefix)
            if temp is not None:
                print(f"Added first matched title: {temp}")
            else:
                print("Error: Prefix was not found.")
        elif option == "9":
            infix = input("Enter infix: ")
            structure = int(input("Enter structure (1 or 2): "))
            max_titles = int(input("Enter max number of titles: "))
            bookStore.bestsellers_with(infix, structure, max_titles)
        elif option == '10':
            bookStore.sort_catalog(
                input('Choose an algorithm:\n\t1 - Merge Sort\n\t2 - Quick Sort (first element pivot)'
                      '\n\t3 - Quick Sort (random element pivot)\nYour selection: '))
        elif option == '11':
            bookStore.display_catalog(input('Enter the number of books to display: '))
        ''' 
        Add the menu options when needed
        '''


def menu_palindrome_test():
    option = ""
    while option != '0':
        print("""
        Enter a word/phrase to test if it's a palindrome:
        0 Return to main menu
        """)
        option = input()
        if option != '0':
            word = option.lower()
            if word == word[::-1]:
                print("Result: Palindrome")
                return "Palindrome"
            else:
                print("Result: Not a palindrome")
                return "Not a palindrome"


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)
        option = input()

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            menu_palindrome_test()


if __name__ == "__main__":
    main()
