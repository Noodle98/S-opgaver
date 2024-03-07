from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract
import plusbus_data as pbd
import plusbus_sql as pbsql


def booked_rejse(rejse):
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Bookinger).where(pbd.Bookinger.rejse_id == rejse.id))
        pladser = 0

        for record in records:
            pladser += pbsql.get_record(pbd.Bookinger, record.id).pladser
    return pladser


def capacity_available(rejse, new_booking):
    # Is the already booked pladser plus the new bookinger pladser less than the resjer's pladskapacitet
    booked = booked_rejse(rejse)
    print(booked)
    print(new_booking.pladser)
    return rejse.pladskapacitet >= (booked + int(new_booking.pladser))
