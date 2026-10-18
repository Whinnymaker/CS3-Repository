class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author
        
    def display_info(self):
        print(f'Title: {self.__title}')
        print(f'Author: {self.__author}')

class Book(Publication):
    def __init__(title, author, number_pages):
        self.__title = title
        self.__author = author
        self.number_pages = number_pages
        
    def get_number_of_pages(self):
        return self.number_pages

    def set_number_of_pages(self, title):
        if number_pages <= 0:
            print("The number of pages must be positive.")
    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.get_number_of_pages()}")
        

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        self.title = title
        self.author = author
        self.issue_number = issue_number
        
    def get_issue_number(self):
        return self.issue_number
        
    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("The number of pages must be positive.")
            
    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.get_issue_number()}")
        


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()


print("\nMagazine Information:")
mag1.display_info()
