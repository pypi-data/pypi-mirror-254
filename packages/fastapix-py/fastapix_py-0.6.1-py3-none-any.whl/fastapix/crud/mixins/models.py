from typing_extensions import Optional

from sqlalchemy import func

from fastapix.crud import Field, SQLModel
from fastapix.crud.mixins._typing import DATETIME


class PkMixin(SQLModel):
    id: int = Field(default=None, title="ID", primary_key=True, nullable=False, create=False, update=False)


class CreateTimeMixin(SQLModel):
    create_time: DATETIME = Field(default_factory=DATETIME.now, title="Create Time", create=False, update=False)


class UpdateTimeMixin(SQLModel):
    update_time: Optional[DATETIME] = Field(
        default_factory=DATETIME.now,
        title="Update Time",
        sa_column_kwargs={"onupdate": func.localtimestamp()},
        create=False,
        update=False
    )


class DeleteTimeMixin(SQLModel):
    delete_time: Optional[DATETIME] = Field(None, title="Delete Time", create=False)


class CUDTimeMixin(CreateTimeMixin, UpdateTimeMixin, DeleteTimeMixin):
    pass
