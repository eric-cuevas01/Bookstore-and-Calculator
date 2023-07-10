import ArrayList
import ArrayQueue
import Book
import DLList
import RandomQueue
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import MaxQueue
import time
from ChainedHashTable import ChainedHashTable


class BookStore:
    """
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart.
    """

    def __init__(self):
        self.getIndices = None
        self.catalog = DLList.DLList()
        self.bookCatalog = None
        self.shoppingCart = SLLQueue.SLLQueue()
        self.bookIndices = ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        """
        loadCatalog: Read the file fileName and creates the array list with all books.
        book records are separated by  ^. The order is key,
        title, group, rank (number of copies sold) and similar books
        """
        self.bookCatalog = ArrayList.ArrayList()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

        with open(fileName, encoding="utf8") as f:
            start_time = time.time()
            for line in f:
                key, title, group, rank, similar = line.split("^")
                book = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(book)
                # self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
                # search tree
                # self.bookIndices.add(key, self.bookCatalog.size() - 1)
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        """
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input:
            i: positive integer
        """
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        """
        addBookByIndex: Inserts into the playlist the song of the list at index i
        input:
            i: positive integer
        """
        # Validating the index. Otherwise, it  crashes
        if 0 <= i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByPrefix(self, prefix):
        """
        addBookByPrefix: Adds the first matched book containing prefix in the title, when
        the book titles are sorted in alphabetical order. Returns the title of the book that
        was added to the cart, if the prefix was matched, None otherwise.
        """
        book = self.sortedTitleIndices.searchSmallestGreaterThanOrEqual(prefix)
        if book.k[0:len(prefix)] == prefix:
            if len(prefix) > 0:
                self.shoppingCart.add(self.bookCatalog.get(book.v))
                print("Added first matched title: " + book.k)
            else:
                print('Error: Prefix was not found.')
        else:
            print('Error: Prefix was not found.')

    def addBookByKey(self, key):
        """
        addBookByKey: Adds the book with the given key to the shopping cart
        input:
            key: A string representing the book key
        """
        start_time = time.time()
        if self.bookIndices.find(key) is not None:
            self.shoppingCart.add(self.bookCatalog.get(self.bookIndices.find(key)))
            print(f"Added title: {self.bookCatalog.get(self.bookIndices.find(key)).title}")
        else:
            print("Book not found...")
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt: int):
        """
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
        """
        start_time = time.time()
        found = 0
        for book in self.bookCatalog:
            if infix in book.title:
                print(book)
                found += 1
                if found >= cnt:
                    break
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        """
        removeFromShoppingCart: remove one book from the shopping cart
        """
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        """
        getCartBestSeller: prints the title of the book that is the bestseller amongst the rest of the books in the cart
        """
        if self.shoppingCart.size() > 0:
            print('getCartBestSeller returned')
            print(f"The best-seller in the shopping cart is {self.shoppingCart.max().title}")
        else:
            print("The shopping cart is empty.")

    def getCatalogBookByKey(self, key):
        for book in self.bookCatalog:
            if book.key == key:
                return book
        return None

    def bestsellers_with(self, infix, structure, n=0):
        if n == '':
            n = 0
        n = int(n)
        if infix == '':
            print('Invalid infix.')
        elif n < 0:
            print('Invalid number of titles.')
        else:
            abc = time.time()
            if True:  # if structure == '1':
                BS = BinarySearchTree.BinarySearchTree()
                for goo in self.bookCatalog:
                    if infix in goo.title:
                        BS.add(goo.rank, goo)
                yes = BS.in_order()
                yes.reverse()
                for yoot, yeet in enumerate(yes):
                    if yoot >= n > 0:
                        break
                    print(yeet.v)
            elif structure == '2':
                BS = BinaryHeap.BinaryHeap()
                for goo in self.bookCatalog:
                    if infix in goo.title:
                        goo.rank *= -1
                        BS.add(goo)
                for _ in range(BS.size()):
                    if _ >= n > 0:
                        break
                    yo = BS.remove()
                    yo.rank *= -1
                    print(yo)
            else:
                print('Invalid data structure.')
            y123 = time.time() - abc
            print(
                f'Displayed bestsellers_with({infix}, {structure}, {n}) in {y123} seconds')

    def sort_catalog(self, s):
        """
        sort_catalog: Sorts the ArrayList instance self.bookCatalog using the sorting algorithm determined by parameter s
        input:
            s: An integer determining the sorting algorithm to use:
                1 for merge-sort
                2 for quick-sort with first element as pivot
                3 for quick-sort with a randomly chosen element as pivot
        output:
            True if s is a valid integer, False otherwise
        """
        if s == 1:
            # merge-sort
            start_time = time.time()
            self.bookCatalog = self.merge_sort(self.bookCatalog)
            elapsed_time = time.time() - start_time
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
            return True
        elif s == 2:
            # quick-sort with first element as pivot
            start_time = time.time()
            self.quick_sort(self.bookCatalog, 0, self.bookCatalog.size() - 1, pivot_choice=1)
            elapsed_time = time.time() - start_time
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
            return True
        elif s == 3:
            # quick-sort with a randomly chosen element as pivot
            start_time = time.time()
            self.quick_sort(self.bookCatalog, 0, self.bookCatalog.size() - 1, pivot_choice=2)
            elapsed_time = time.time() - start_time
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
            return True
        else:
            # invalid input
            return False

    def display_catalog(self, n):
        """
        display_catalog: Displays the first n books of the book catalog
        input:
            n: The number of books to display
        """
        if n > self.bookCatalog.size():
            # display all books
            n = self.bookCatalog.size()
        for i in range(n):
            book = self.bookCatalog.get(i)
            print(f"Title: {book.title}")
            print(f"Group: {book.group}")
            print(f"Rank: {book.rank}")
            print(f"Similar: {book.similar}")
            print("-----")
