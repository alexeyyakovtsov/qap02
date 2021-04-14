import json

class Book:
    """
    Class for work with books in json file
    """
    def read_book_file(self):
        with open('homework_7/book.json', 'r') as book_file:
            return json.loads(book_file.read())

    def add_book(self, id, name, author, pages, isbn, flag):
        f = self.read_book_file()
        with open('homework_7/book.json', 'w') as file:
            data = {
                id: {
                    "name": name,
                    "author": author,
                    "pages": pages,
                    "idbn": isbn,
                    "flag": flag
                }
            }
            f[id] = data[id]
            json.dump(f, file, indent=4)
        file.close()


class User(Book):
    """
    Class for booking books for user.    
    """
    def booking(self, book_number):
        f = self.read_book_file()

        for book in f:
            if book == book_number and f[book_number]['flag'] == True:
                print('Книга уже забронирована')
            elif book == book_number and f[book_number]['flag'] == False:
                with open('homework_7/book.json', 'w') as w_file:
                    f[book_number]["flag"] = True
                    json.dump(f, w_file, indent=4)
                w_file.close()
                print('Вы забронировали книгу')


a = User()
a.booking(input('Введите номер книги: '))
a.add_book(int(input('Ведите id книги: ')), input('Введите название книги: '), input('Введите автора книги: ')
, input('Введите количество страниц: '), input('Введите ISBN: '), bool(input('Введите флаг (True or False): ')))
