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