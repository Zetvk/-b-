from db import db

# Определяем класс items, который наследуется от db.Model
class items(db.Model):
    # Определяем атрибуты, соответствующие столбцам таблицы
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class OrderModel(db.Model):

    # Определяем атрибуты, соответствующие столбцам таблицы
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mail = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)


    # Определяем конструктор класса
    def __init__(self, title, image, description, price):
        # Присваиваем значения атрибутам
        self.title = title
        self.image = image
        self.description = description
        self.price = price

    def __repr__(self):
        # Возвращаем название, автора и издателя книги
        return f"<Book: {self.title} by {self.image} published by {self.description}d {self.price}>"
    

    # Определяем конструктор класса
    def __init__(self, mail, name, phone, address):
        # Присваиваем значения атрибутам
        self.mail = mail
        self.name = name
        self.phone = phone
        self.address = address

    def __repr__(self):
        # Возвращаем информацию о заказе
        return f"<Order: {self.id} by {self.name} at {self.mail}>"