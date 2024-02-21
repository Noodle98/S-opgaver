from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract
import plusbus_data as pbd
import plusbus_sql as pbsql


#def booked_rute(rejser, date_):
    # returns the already booked route on Rejse at a certain date
    #with Session(pbsql.engine) as session:
        #records = session.scalars(select(pbd.Bookinger).where(pb.Bookinger.rejse_id == rejser.id).where(extract('day', pbd.Bookinger.dato))
