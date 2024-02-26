from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from datetime import date
from plusbus_data import Kunder, Rejser, Bookinger, Base

# add the following 7 lines to make foreign key constraints work  https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#sqlite-foreign-keys
from sqlalchemy.engine import Engine as engine
from sqlalchemy import event


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Database = 'sqlite:///plusbus.db'  # first part: database type, second part: file path

def create_test_data():  # Optional. Used to test database functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Kunder(efternavn="Hansen", kontakt="ehansen@gmail.com"))
        new_items.append(Kunder(efternavn="Lund", kontakt="uulund@gmail.com"))
        new_items.append(Kunder(efternavn="Rasmussen", kontakt="+4572189485"))
        new_items.append(Rejser(rute="Roskilde - Vordingborg", dato= date(day=5, month=7, year=2024), pladskapacitet=25))
        new_items.append(Rejser(rute="Høje-Taastrup - Jönköping", dato= date(day=4, month=8, year=2024), pladskapacitet=25))
        new_items.append(Rejser(rute="Aarhus - Berlin", dato= date(day=20, month=6, year=2024), pladskapacitet=30))
        new_items.append(Bookinger(kunde_id=0, rejse_id=0, pladser=4))
        new_items.append(Bookinger(kunde_id=1, rejse_id=1, pladser=2))
        new_items.append(Bookinger(kunde_id=2, rejse_id=2, pladser=4))
        session.add_all(new_items)
        session.commit()


def select_all(classparam):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))  # very useful for converting into our data class
        result = []
        for record in records:
            # print(record)
            result.append(record)
    return result


def get_record(classparam, record_id):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return the record in classparams table with a certain id
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()  # very useful for converting into our data class
    return record


def create_record(record):
    with Session(engine) as session: # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
        # create a record in the database
        record.id = None
        session.add(record)
        session.commit() # makes changes permanent in database


# region kunder
def update_kunder(kunder):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the kunder table
    with Session(engine) as session:
        session.execute(update(Kunder).where(Kunder.id == kunder.id).values(efternavn=kunder.efternavn, kontakt=kunder.kontakt))
        session.commit()  # makes changes permanent in database


def delete_hard_kunder(kunder):
    # delete a record in the kunder table
    with Session(engine) as session:
        session.execute(delete(Kunder).where(Kunder.id == kunder.id))
        session.commit()  # makes changes permanent in database


def delete_soft_kunder(kunder):
    # soft delete a record in the kunder table by setting its kontakt to -1 (see also method "valid" in the kunder class)
    with Session(engine) as session:
        session.execute(update(Kunder).where(Kunder.id == kunder.id).values(id=-1, efternavn=kunder.efternavn, kontakt=kunder.kontakt))
        session.commit()  # makes changes permanent in database
# endregion kunder


# region rejser
def update_rejser(rejser):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the rejser table
    with Session(engine) as session:
        session.execute(update(Rejser).where(Rejser.id == rejser.id).values(rute=rejser.rute, dato=rejser.dato, pladskapacitet=rejser.pladskapacitet))
        session.commit()  # makes changes permanent in database


def delete_hard_kunder(rejser):
    # delete a record in the rejser table
    with Session(engine) as session:
        session.execute(delete(Rejser).where(Rejser.id == rejser.id))
        session.commit()  # makes changes permanent in database


def delete_soft_kunder(rejser):
    # soft delete a record in the rejser table by setting its pladskapacitet to -1 (see also method "valid" in the kunder class)
    with Session(engine) as session:
        session.execute(update(Rejser).where(Rejser.rute == rejser.rute).values(id=-1, dato=rejser.dato, pladskapacitet=rejser.pladskapacitet))
        session.commit()  # makes changes permanent in database
# endregion rejser


# region bookinger
def update_bookinger(bookinger):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the bookinger table
    with Session(engine) as session:
        session.execute(update(Bookinger).where(Bookinger.id == bookinger.id).values(kunde_id=bookinger.kunde_id, rejse_id=bookinger.rejse_id, pladser=bookinger.pladser))#, date=bookinger.date))
        session.commit()  # makes changes permanent in database


def delete_hard_bookinger(bookinger):
    # delete a record in the bookinger table
    with Session(engine) as session:
        session.execute(delete(Bookinger).where(Bookinger.id == bookinger.id))
        session.commit()  # makes changes permanent in database


def delete_soft_bookinger(bookinger):
    # soft delete a record in the bookinger table by setting its weight to -1 (see also method "valid" in the kunder class)
    with Session(engine) as session:
        session.execute(update(Bookinger).where(Bookinger.id == bookinger.id).values(kunde_id=bookinger.kunde_id, rejse_id=bookinger.rejse_id, pladser=bookinger.pladser))#, date=bookinger.date, ))
        session.commit()  # makes changes permanent in database
# endregion bookinger

if __name__ == "__main__":  # Executed when invoked directly
# The next 2 lines are needed _after_ data classes / sql tables were defined
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    # create_test_data()
    # print(select_all(Kunder))
    # print(get_record_kunder(Kunder, 2))
else:  # Executed when imported
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)

create_test_data()