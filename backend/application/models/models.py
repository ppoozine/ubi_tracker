import sqlalchemy
from ..database import metadata

UserInfoBaseModel = sqlalchemy.Table(
    "user_info_base",
    metadata,
    sqlalchemy.Column("pk", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("idnumber", sqlalchemy.Text),
    sqlalchemy.Column("username", sqlalchemy.Text),
    sqlalchemy.Column("sex", sqlalchemy.Text),
    sqlalchemy.Column("addr", sqlalchemy.Text),
    sqlalchemy.Column("email", sqlalchemy.Text),
    sqlalchemy.Column("phone", sqlalchemy.Text),
    sqlalchemy.Column("user_id", sqlalchemy.Text)
)

CarInfoBaseModel = sqlalchemy.Table(
    "car_info_base",
    metadata,
    sqlalchemy.Column("pk", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Text),
    sqlalchemy.Column("tracker_id", sqlalchemy.Text),
    sqlalchemy.Column("car_plate", sqlalchemy.Text),
    sqlalchemy.Column("create_date", sqlalchemy.DATE),
    sqlalchemy.Column("active", sqlalchemy.BOOLEAN)
)

CarPlateModel = sqlalchemy.Table(
    "car_plate_info",
    metadata,
    sqlalchemy.Column("pk", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("car_plate", sqlalchemy.Text),
    sqlalchemy.Column("start_date", sqlalchemy.DATE),
    sqlalchemy.Column("end_date", sqlalchemy.DATE)
)

def car_segment_table(table_name):
    CarSegmentModel = sqlalchemy.Table(
        table_name,
        metadata,
        sqlalchemy.Column("tracker_id", sqlalchemy.Text),
        sqlalchemy.Column("trip_date", sqlalchemy.Text),
        sqlalchemy.Column("trip_id", sqlalchemy.Integer),
        sqlalchemy.Column("seq_no", sqlalchemy.Integer),
        sqlalchemy.Column("longitude", sqlalchemy.Float),
        sqlalchemy.Column("latitude", sqlalchemy.Float),
        extend_existing=True
    )
    return CarSegmentModel