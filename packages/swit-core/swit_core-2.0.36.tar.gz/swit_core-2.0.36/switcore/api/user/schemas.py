from pydantic import BaseModel


class SwitUser(BaseModel):
    cmp_id: str
    color: str | None
    department: str | None
    id: str
    language: str
    name: str
    photo: str | None
    status: int | None
    status_msg: str | None
    tel: str | None
    timezone: str | None
    user_email: str | None
