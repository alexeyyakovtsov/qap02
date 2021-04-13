import json

class Book:
    """
    Class for work with books in json file
    """

    def read_book_file(self):
        with open('homework_7/book.json', 'r') as book_file:
            return json.loads(book_file.read())

    def add_book(self, name, author, pages, isbn):
        with open('homework_7/book.json', 'a') as file:
            data = dict(zip(('name', 'author', 'pages', 'isbn'), (
                name, author, pages, isbn
            )))
            json.dump(data, file, indent=2)
            #file.write('\n')
        file.close()

class User(Book):
    """
    Class for booking books for user.    
    """

    def booking(self, book_number):
        f = self.read_book_file()

        for book in f:
            if book == book_number and f[book_number]['isbn'] == True:
                print('Книга уже забронирована')
            elif book == book_number and f[int(book_number)]['isbn'] == False:
                with open('homework_7/book.json', 'r') as r_file:
                    json_data = json.load(r_file)
                    print(json_data)

                with open('homework_7/book.json', 'w') as w_file:
                    json_data = book[book_number]['isbn'] = True
                    json.dumps(json_data)
                w_file.close()
                print('Вы забронировали книгу')

a = User()
a.booking(1)