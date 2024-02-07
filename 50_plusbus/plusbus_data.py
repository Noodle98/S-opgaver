from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date
from dateutil import parser
from tkinter import messagebox
Base = declarative_base()

class Kunder(Base):
    __tablename__ = "kunder"
    efternavn = Column(String, primary_key=True)
    kontakt = Column(String)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Kunder({self.efternavn=:4}    {self.kontakt=:5})"

    def convert_to_tuple(self):  # Convert Kunder to tuple
        return self.efternavn, self.kontakt
    def valid(self):
        try:
            value = self.kontakt
            if value == "-":
                return False
        except ValueError:
            return False
        return value

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Kunder
        kunder = Kunder(efternavn=tuple_[0], kontakt=tuple_[1])
        return kunder


class Rejser(Base):
    __tablename__ = "rejser"
    rute = Column(String, primary_key=True)
    dato = Column(Date)
    pladskapacitet = Column(Integer)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Rejser({self.rute=:4}    {self.dato=:5}     {self.pladskapacitet=:6})"

    def convert_to_tuple(self):  # Convert Rejser to tuple
        return self.rute, self.dato, self.pladskapacitet
    def valid(self):
        try:
            value = int(self.pladskapacitet)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Rejser
        rejser = Rejser(rute=tuple_[0], dato=tuple_[1], pladskapacitet=tuple_[2])
        return rejser


class Bookinger(Base):
    __tablename__ = "bookinger"
    kunde_id = Column(Integer, primary_key=True)
    rejse_id = Column(Integer)
    pladser = Column(Integer)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Bookinger({self.kunde_id=:4}    {self.rejse_id=:5}     {self.pladser=:6})"

    def convert_to_tuple(self):  # Convert Bookinger to tuple
        return self.kunde_id, self.rejse_id, self.pladser
    def valid(self):
        try:
            value = int(self.kunde_id)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Bookinger
        bookinger = Rejser(kunde_id=tuple_[0], rejse_id=tuple_[1], pladser=tuple_[2])
        return bookinger