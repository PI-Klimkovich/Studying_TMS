from sqlalchemy import Column, Integer, String, Float, ForeignKey, select
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

# Строка подключения (DSN)
dsn = "sqlite:///tasks_lesson_15.db"

# Точка входа в БД.
engine = create_engine(dsn, echo=True)

# Класс для сессий, которые использует `engine`
session = sessionmaker(bind=engine, autoflush=False)


# Декларативная основа для будущих классов
class Base(DeclarativeBase):
    pass


# Декларативное описание таблиц
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(200), unique=True, nullable=False)

    # Внутренние связи для SQLAlchemy
    orders = relationship("Order", back_populates="user")

    def __str__(self):
        return f"User: {self.username}"


class Seller(Base):
    __tablename__ = "sellers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64), unique=True, nullable=False)
    phone = Column(String(64), nullable=False)

    # Внутренние связи для SQLAlchemy
    products = relationship("Product", back_populates="seller")

#     def __str__(self):
#         return f"Seller: {self.company}"


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    cost = Column(Float, nullable=False)
    count = Column(Integer, nullable=False)
    seller_id = Column(Integer, ForeignKey("sellers.id"))

    # Далее внутренние связи для SQLAlchemy
    orders = relationship("Order", back_populates="product")
    seller = relationship("Seller", back_populates="products")


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    count = Column(Integer, nullable=False)

    # Далее внутренние связи для SQLAlchemy
    product = relationship(Product, back_populates="orders")
    user = relationship(User, back_populates="orders")


def create_tables():
    # Создание таблиц, унаследованных от`Base`
    Base.metadata.create_all(engine)


def drop_tables():
    # Удаление таблиц, унаследованных от Base`
    Base.metadata.drop_all(engine)


def add_users(connection):
    # Добавим в таблицу запись через подключение
    connection.add(User(username="igor", password="<PASSWORD>", email="igor@mail.com"))
    connection.add(User(username="user123", password="<PASSWORD>", email="user123@mail.com"))
    connection.add(User(username="user111", password="<PASSWORD>", email="user111@mail.com"))
    connection.add(User(username="user999", password="<PASSWORD>", email="user999@mail.com"))
    # Подтверждаем добавление!
    connection.commit()


def add_sellers(connection):
    connection.add(Seller(company="company1", phone='+375293336688'))
    connection.add(Seller(company="company2", phone='+375334445566'))
    connection.add(Seller(company="company3", phone='+375443338899'))
    connection.add(Seller(company="company4", phone='+375256667788'))
    connection.commit()


def add_products(connection):
    connection.add(Product(name="tv", cost=111, count=20, seller_id=1))
    connection.add(Product(name="ps5", cost=222, count=10, seller_id=2))
    connection.add(Product(name="pc", cost=333, count=25, seller_id=3))
    connection.add(Product(name="monitor", cost=444, count=5, seller_id=4))
    connection.commit()


def create_order(connection, user: User, product: Product):
    order = Order(user_id=user.id, product_id=product.id, count=2)
    connection.add(order)
    connection.commit()


def show_user_orders_opt(connection, username: str):
    # Первый SQL запрос

    # SELECT users.username, products.name FROM users
    # JOIN orders ON users.id = orders.user_id
    # JOIN products ON products.id = orders.product_id
    # WHERE users.username = ?
    query = (
        select(User.username, Product.name)
        .join(User.orders)
        .join(Order.product)
        .where(User.username == username)
    )

    res = connection.execute(query)

    for line in res:
        print("-" * 20, line)


drop_tables()
create_tables()

with session() as conn:
    add_users(conn)  # Добавили пользователей

    add_sellers(conn)  # Добавили поставщиков

    add_products(conn)  # Добавили товары

    # Отобразить всех пользователей!

    # Создаем запрос
    query = select(User)  # select * from users;

    users = conn.execute(query).scalars()  # Выполняем запрос!
    # Через метод `scalars()` получаем перечень объектов `User`
    # users это тип `ScalarResult[User]` - перечень (итератор).

    for user in users:
        print(user.username, user.email)

    query = select(User).where(User.username == "igor")

    # Так как пользователь только 1 с таким username, то можно сделать `one()`
    user = conn.execute(query).scalars().one()

    query = select(Product).where(Product.name == "tv")
    product = conn.execute(query).scalars().one()

    create_order(conn, user, product)

    print("=" * 20)
    print("START show_user_orders_opt")
    show_user_orders_opt(conn, "igor")
