from datetime import datetime
from typing import Annotated
from uuid import uuid4

from sqlalchemy import UUID, DateTime, Integer, text
from sqlalchemy.orm import mapped_column

db_utc_now = text("TIMEZONE('utc', now())")

integer_pk = Annotated[int, mapped_column(Integer, primary_key=True)]

uuid_pk = Annotated[
    uuid4,
    mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4),
]

created_at_ct = Annotated[datetime, mapped_column(DateTime, server_default=db_utc_now)]
updated_at_ct = Annotated[
    datetime,
    mapped_column(DateTime, server_default=db_utc_now, onupdate=db_utc_now),
]
