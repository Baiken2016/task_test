from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date

Base = declarative_base()


class OwnerData(Base):
    """
    Модель таблицы владельцев автомобиля в базе данных

    Столбцы:
        owner_id (int): уникальный идентификатор владельца (является первичным ключом)
        owner_name (str): ФИО владельца
        registration_address (str): адрес регистрации местожительства владельца
        actual_address (str): адрес проживания владельца
    """

    __tablename__ = 'owner_data'
    __tableargs__ = {
        'comment': 'Владельцы автомобиля'
    }

    owner_id = Column(Integer, primary_key=True)
    owner_name = Column(String, nullable=False, comment='ФИО владельца')
    registration_address = Column(String, nullable=False, comment='Адрес регистрации местожительства владельца')
    actual_address = Column(String, comment='Адрес проживания владельца')


class CarModels(Base):
    """
    Модель таблицы моделей и телеметрических данных автомобиля в базе данных

    Столбцы:
        car_id (int): уникальный идектификатор автомобиля (является первичным ключом)
        car_model (str): название и модель автомобиля
        car_height (float): высота автомобиля
        car_width (float): ширина автомобиля
        car_length (float): длина автомобиля
        car_speed (float): максимальная скорость автомобиля (км/час)
        date_of_creation (date): дата выпуска автомобиля (формат даты: YYYY-MM-DD)
    """

    __tablename__ = 'car_models_data'
    __tableargs__ = {
        'comment': 'Модели автомобиля'
    }

    car_id = Column(Integer, primary_key=True)
    car_model = Column(String, nullable=False, comment='Название модели автомобиля')
    car_height = Column(Float, nullable=False, comment='высота автомобиля')
    car_width = Column(Float, nullable=False, comment='ширина автомобиля')
    car_length = Column(Float, nullable=False, comment='длина автомобиля')
    car_speed = Column(Float, nullable=False, comment='максимальная скорость автомобиля (км/час)')
    date_of_creation = Column(Date, nullable=False, comment='дата выпуска автомобиля (формат даты: YYYY-MM-DD)')


class TechPassport(Base):
    """
    Модель таблицы тех. паспортов автомобиля в базе данных

    Столбцы:
        passport_id (int): уникальный идентификатор пасспорта (является первичным ключом)
        registration_id (str): гос. номер автомобиля (пример: 123AAA01)
        car_id (int): идентификатор модели автомобиля (является внешним ключом столба car_id, таблицы CarModels)
        date_of_issue (date): дата выпуска пасспорта (формат даты: YYYY-MM-DD)
        car_color (str): цвет автомобиля
        owner_id (int): идентификатор владельца автомобиля
                        (является внешним ключом столба owner_id, таблицы OwnerData)
    """

    __tablename__ = 'tech_passport_data'
    __tableargs__ = {
        'comment': 'Тех. пасспорта автомобиля'
    }

    passport_id = Column(Integer, primary_key=True)
    registration_id = Column(String, nullable=False, comment='гос. номер автомобиля (пример: 123AAA01)')
    car_id = Column(Integer, ForeignKey(CarModels.car_id),
                    comment="ID модели автомобиля (является внешним ключом столба car_id, таблицы CarModels)")
    date_of_issue = Column(Date, nullable=False, comment='дата выпуска пасспорта (формат даты: YYYY-MM-DD)')
    car_color = Column(String, nullable=False, comment='цвет автомобиля')
    owner_id = Column(Integer, ForeignKey(OwnerData.owner_id),
                      comment='ID владельца автомобиля (является внешним ключом столба owner_id, таблицы OwnerData)')
