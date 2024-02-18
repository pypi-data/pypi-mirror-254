import datetime
from enum import Enum
from pathlib import Path

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta as rd
from pydantic import BaseModel, ConfigDict, Field, field_validator

MAX_JUSTICE_AGE = 70  # 1987 Constitution
JUSTICE_FILE = Path(__file__).parent / "sc.yaml"


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "unspecified"


class Suffix(str, Enum):
    jr = "Jr."
    sr = "Sr."
    third = "III"
    fourth = "IV"
    fifth = "V"
    sixth = "VI"


class Justice(BaseModel):
    """
    # Justice

    Field | Type | Description
    --:|:--|:--
    id |int | Unique identifier of the Justice based on appointment roster
    full_name |str | First + last + suffix
    first_name |str | -
    last_name |str | -
    suffix |str | e.g. Jr., Sr., III, etc.
    nick_name |str | -
    gender |str | -
    alias |str | Other names
    start_term |str | Time justice appointed
    end_term |str | Time justice
    chief_date |str | Date appointed as Chief Justice (optional)
    birth_date |str | Date of birth
    retire_date |str | Based on the Birth Date, if it exists, it is the maximum term of service allowed by law.
    inactive_date |str | Which date is earliest inactive date of the Justice, the retire date is set automatically but it is not guaranteed to to be the actual inactive date. So the inactive date is either that specified in the `end_term` or the `retire_date`, whichever is earlier.

    The list of justices from the sc.yaml file are parsed through this model prior to being inserted
    into the database.
    """  # noqa: E501

    model_config = ConfigDict(use_enum_values=True)
    id: int = Field(
        ...,
        title="Justice ID Identifier",
        description=(
            "Starting from 1, the integer represents the order of appointment"
            " to the Supreme Court."
        ),
        ge=1,
        lt=1000,
    )
    full_name: str | None = Field(None)
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    suffix: Suffix | None = Field(None, max_length=4)
    gender: Gender = Field(...)
    alias: str | None = Field(
        None,
        title="Alias",
        description="Means of matching ponente and voting strings to the justice id.",
    )
    start_term: datetime.date | None = Field(
        None,
        title="Start Term",
        description="Date of appointment.",
    )
    end_term: datetime.date | None = Field(
        None,
        title="End Term",
        description="Date of termination.",
    )
    chief_date: datetime.date | None = Field(
        None,
        title="Date Appointed As Chief Justice",
        description=(
            "When appointed, the extension title of the justice changes from"
            " 'J.' to 'C.J'. for cases that are decided after the date of"
            " appointment but before the date of retirement."
        ),
    )
    birth_date: datetime.date | None = Field(
        None,
        title="Date of Birth",
        description=(
            "The Birth Date is used to determine the retirement age of the"
            " justice. Under the 1987 constitution, this is"
            f" {MAX_JUSTICE_AGE}. There are missing dates: see Jose Generoso"
            " 41, Grant Trent 14, Fisher 19, Moir 20."
        ),
    )
    retire_date: datetime.date | None = Field(
        None,
        title="Mandatory Retirement Date",
        description=(
            "Based on the Birth Date, if it exists, it is the maximum term of"
            " service allowed by law."
        ),
    )
    inactive_date: datetime.date | None = Field(
        None,
        title="Date",
        description=(
            "Which date is earliest inactive date of the Justice, the retire"
            " date is set automatically but it is not guaranteed to to be the"
            " actual inactive date. So the inactive date is either that"
            " specified in the `end_term` or the `retire_date`, whichever is"
            " earlier."
        ),
    )

    @field_validator("retire_date")
    def retire_date_70_years(cls, v, values):
        if v and values["birth_date"]:
            if values["birth_date"] + rd(years=MAX_JUSTICE_AGE) != v:
                raise ValueError("Must be 70 years from birth date.")
        return v

    @classmethod
    def from_data(cls, data: dict):
        def extract_date(text: str | None) -> datetime.date | None:
            return parse(text).date() if text else None

        # Not all justices have/need aliases; default needed
        alias = data.pop("Alias", None)
        if not alias:
            if surname := data.get("last_name"):
                if suffix := data.get("suffix"):
                    alias = f"{surname} {suffix}".lower()

        retire_date = None
        if dob := extract_date(data.pop("Born")):
            retire_date = dob + rd(years=MAX_JUSTICE_AGE)

        # retire_date = latest date allowed; but if end_date present, use this
        inactive_date = retire_date
        if end_date := extract_date(data.pop("End of term")):
            inactive_date = end_date or retire_date

        return cls(
            id=data.pop("#"),
            full_name=data["full_name"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            suffix=Suffix(data["suffix"]),
            gender=Gender(data["gender"]),
            alias=alias,
            birth_date=dob,
            start_term=extract_date(data.pop("Start of term")),
            end_term=end_date,
            chief_date=extract_date(data.pop("Appointed chief")),
            retire_date=retire_date,
            inactive_date=inactive_date,
        )
