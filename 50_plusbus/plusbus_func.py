from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract
import plusbus_data as pbd
import plusbus_sql as pbsql


def booked_rejse(rejser):
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Bookinger).where(pbd.Bookinger.rejse_id == rejser.id))
        pladser = 0

        #for record in records



def capacity_available(rejser, id, new_booking):
    booked = booked_rejse(rejser, id)
