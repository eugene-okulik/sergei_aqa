class Book:
    page_material = "бумага"
    text = "в наличии"

    def __init__(self, book_name, author, page_count, isbn, book_is_reserved=True):
        self.book_name = book_name
        self.author = author
        self.page_count = page_count
        self.ISBN = isbn
        self.book_is_reserved = book_is_reserved


class SchoolBook(Book):

    def __init__(self, book_name, author, page_count, isbn, subject, school_class, exercises, book_is_reserved=True):
        super().__init__(book_name, author, page_count, isbn, book_is_reserved)
        self.subject = subject
        self.school_class = school_class
        self.exercises = exercises


first_book = Book('Тени забытого времени', 'Александр Волков', 384, 9785123456789)
second_book = Book('Восхождение к мечте', 'Елена Романова', 256, 9785987654321, False)
third_book = Book('Код свободы', 'Виктор Зорин', 420, 9785234567890)
fourth_book = Book('Потерянные голоса', 'Мария Смирнова', 312, 9785876543210)
fifth_book = Book('Миры будущего', 'Игорь Андреев', 512, 9785192837465)
sixth_book = SchoolBook('Тайны физики: Учебник для юных исследователей', ' Анна Иванова', 320,
                        9785123459990, 'Физика', 9, True)
seventh_book = SchoolBook('Математические горизонты: Пособие для старшеклассников', 'Сергей Петров',
                          280, 9785543218887, 'Математика', 11, True, False)

print(f"Материал: {first_book.page_material}, Наличие текста: {first_book.text}, Название: {first_book.book_name}, "
      f"Автор: {first_book.author}, Количество страниц: {first_book.page_count}, "
      f"ISBN: {first_book.ISBN}" + (", Зарезервирована" if first_book.book_is_reserved else ""))

print(f"Материал: {second_book.page_material}, Наличие текста: {second_book.text}, Название: {second_book.book_name}, "
      f"Автор: {second_book.author}, Количество страниц: {second_book.page_count}, "
      f"ISBN: {second_book.ISBN}" + (", Зарезервирована" if second_book.book_is_reserved else ""))

print(f"Материал: {third_book.page_material}, Наличие текста: {third_book.text}, Название: {third_book.book_name}, "
      f"Автор: {third_book.author}, Количество страниц: {third_book.page_count}, "
      f"ISBN: {third_book.ISBN}" + (", Зарезервирована" if third_book.book_is_reserved else ""))

print(f"Материал: {fourth_book.page_material}, Наличие текста: {fourth_book.text}, Название: {fourth_book.book_name}, "
      f"Автор: {fourth_book.author}, Количество страниц: {fourth_book.page_count}, "
      f"ISBN: {fourth_book.ISBN}" + (", Зарезервирована" if fourth_book.book_is_reserved else ""))

print(f"Материал: {fifth_book.page_material}, Наличие текста: {fifth_book.text}, Название: {fifth_book.book_name}, "
      f"Автор: {fifth_book.author}, Количество страниц: {fifth_book.page_count}, "
      f"ISBN: {fifth_book.ISBN}" + (", Зарезервирована" if fifth_book.book_is_reserved else ""))

print(f"Материал: {sixth_book.page_material}, Наличие текста: {sixth_book.text}, Название: {sixth_book.book_name}, "
      f"Автор: {sixth_book.author}, Количество страниц: {sixth_book.page_count}, ISBN: {sixth_book.ISBN}, "
      f"Предмет: {sixth_book.subject}, Класс: {sixth_book.school_class}"
      f"{', Зарезервирована' if sixth_book.book_is_reserved else ''}")

print(
    f"Материал: {seventh_book.page_material}, Наличие текста: {seventh_book.text}, Название: {seventh_book.book_name}, "
    f"Автор: {seventh_book.author}, Количество страниц: {seventh_book.page_count}, ISBN: {seventh_book.ISBN}, "
    f"Предмет: {seventh_book.subject}, Класс: {seventh_book.school_class}"
    f"{', Зарезервирована' if seventh_book.book_is_reserved else ''} "
)
