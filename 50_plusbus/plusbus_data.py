from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date
from dateutil import parser
from tkinter import messagebox
Base = declarative_base()

class Kunder(Base):
    __tablename__ = "kunder"
    id = Column(Integer, primary_key=True)
    efternavn = Column(String)
    kontakt = Column(String)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Kunder({self.id}    {self.efternavn}    {self.kontakt})"

    def convert_to_tuple(self):  # Convert Kunder to tuple
        return self.id, self.efternavn, self.kontakt

    def valid(self):
        try:
            value = int(self.id)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Kunder
        kunder = Kunder(id=tuple_[0], efternavn=tuple_[1], kontakt=tuple_[2])
        return kunder


class Rejser(Base):
    __tablename__ = "rejser"
    id = Column(Integer, primary_key=True)
    rute = Column(String)
    dato = Column(Date)
    pladskapacitet = Column(Integer)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Rejser({self.id}    {self.rute}    {self.dato}     {self.pladskapacitet})"

    def convert_to_tuple(self):  # Convert Rejser to tuple
        return self.id, self.rute, self.dato, self.pladskapacitet
    def valid(self):
        try:
            value = int(self.id)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Rejser
        rejser = Rejser(id=tuple_[0], rute=tuple_[1], dato=tuple_[2], pladskapacitet=tuple_[3])
        return rejser


class Bookinger(Base):
    __tablename__ = "bookinger"
    id = Column(Integer, primary_key=True)
    kunde_id = Column(Integer, ForeignKey("kunder.id"), nullable=False)
    rejse_id = Column(Integer, ForeignKey("rejser.id"), nullable=False)
    pladser = Column(Integer)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Bookinger({self.id=:4}    {self.kunde_id=:}    {self.rejse_id=:}     {self.pladser=:5})"

    def convert_to_tuple(self):  # Convert Bookinger to tuple
        return self.id, self.kunde_id, self.rejse_id, self.pladser
    def valid(self):
        try:
            value = int(self.id)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Bookinger
        bookinger = Rejser(id=tuple_[0], kunde_id=tuple_[1], rejse_id=tuple_[2], pladser=tuple_[3])
        return bookinger