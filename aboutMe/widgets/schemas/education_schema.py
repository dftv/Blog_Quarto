from datetime import date

from pydantic import BaseModel


class EducationSchema(BaseModel):
    degree: str
    institution: str
    startDate: date
    endDate: date = date.today()
    present: bool = False
