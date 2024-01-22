from flask import Flask, render_template, request


from db import db


from items import items, OrderModel


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Books.db'

    db.init_app(app)

    @app.route('/')
    def index():
        
        return render_template('index.html')

    @app.route('/catalog')
    def catalog():
        try:
            
            items_list = items.query.all()

            return render_template('catalog.html', items=items_list)
        except Exception as e:
          
            print(f"Error retrieving items: {e}")
           
            return render_template('error.html', message='Произошла ошибка при получении данных из базы данных.')

    @app.route('/order', methods=['GET', 'POST'])
    def order():
       
        if request.method == 'GET':
            return render_template('order.html')
        elif request.method == 'POST':
            # Получаем значения полей почты, имени, телефона и адреса из формы
            mail = request.form.get('mail')
            name = request.form.get('name')
            phone = request.form.get('phone')
            address = request.form.get('address')
            # Проверяем, что все поля заполнены
            if mail and name and phone and address:
                # Создаем объект модели OrderModel с полученными данными
                new_order = OrderModel(mail=mail, name=name, phone=phone, address=address)
                # Создаем контекст приложения
                with app.app_context():
                    # Создаем сессию для работы с базой данных
                    session = db.sessionmaker(bind=db.engine)()
                    # Добавляем объект модели OrderModel в сессию
                    session.add(new_order)
                    # Сохраняем изменения в базе данных
                    session.commit()
                    # Закрываем сессию
                    session.close()
                    # Рендерим страницу success.html с сообщением об успешном оформлении заказа
                    return render_template('success.html', message='Ваш заказ успешно оформлен!')
            else:
                # Рендерим страницу error.html с сообщением об ошибке
                return render_template('error.html', message='Пожалуйста, заполните все поля формы.')

    # Создаем контекст приложения
      # Создаем контекст приложения
    with app.app_context():
        # Создаем таблицы в базе данных
        db.create_all()
        # Создаем сессию для работы с базой данных
        session = db.sessionmaker(bind=db.engine)()
        # Проверяем, есть ли уже записи в таблице items
        if items.query.count() == 0:
            # Создаем объекты модели, которые соответствуют данным, которые хотим добавить в таблицу items
            new_item1 = items(title='Ведьмак', image='static/img.jpg', description='В мире, где существуют магия и чудовища, Геральт из Ривии - один из последних ведьмаков, профессиональных убийц нечисти.', price=2400)
            new_item2 = items(title='Властелин колец', image='static/img (1).jpg', description='В древние времена эльфийский кузнец Саурон создал Кольцо Всевластия, в которое вложил свою силу и злобу. Также но давало  власть над другими ...', price=1500)
            new_item3 = items(title='Песнь льда и пламени', image='static/img (2).jpg', description='В мире, где длительность сезонов не подчиняется законам природы, народы Вестероса и Эссоса оказываются втянуты в жестокую игру престолов.', price=4444)

            # Добавляем объекты модели в сессию
            session.add_all([new_item1, new_item2, new_item3])

            # Сохраняем изменения в базе данных
            session.commit()

        # Закрываем сессию
        session.close()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)