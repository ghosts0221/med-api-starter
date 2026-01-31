from pydantic import BaseModel, Field


class PatientCreate(BaseModel):
    patient_code: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, le=130)
    sex: str = Field(..., min_length=1, max_length=10)


class PatientUpdate(BaseModel):
    age: int | None = Field(default=None, ge=0, le=130)
    sex: str | None = Field(default=None, min_length=1, max_length=10)


from pydantic import BaseModel, Field, ConfigDict

class PatientOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    patient_code: str
    age: int
    sex: str
