from typing import List

from pydantic import BaseModel


class TimeIntervalDto(BaseModel):
    timeStart: str  # указывается в форматах «HH:MM:SS» либо «HH:MM»
    timeEnd: str  # указывается в форматах «HH:MM:SS» либо «HH:MM»
    inSaturday: int = 0  # 1/0 – Разрешение/запрет прохода
    inSunday: int = 0  # 1/0 – Разрешение/запрет прохода
    inHolidays: int = 0  # 1/0 – Разрешение/запрет прохода


class BastionIKSPersonDto(BaseModel):
    name: str
    firstName: str
    secondName: str | None = ""

    tableNo: str | None = ""
    personCat: str | None = ""
    org: str
    dep: str
    post: str | None = ""
    comments: str | None = ""
    docIssueOrgan: str | None = ""
    docSer: str | None = ""
    docNo: str | None = ""
    docIssueDate: str | None = ""
    birthDate: str | None = ""
    birthPlace: str | None = ""
    address: str | None = ""
    phone: str | None = ""
    foto: str | None = ""
    addField1: str | None = ""
    addField2: str | None = ""
    addField3: str | None = ""
    addField4: str | None = ""
    addField5: str | None = ""
    addField6: str | None = ""
    addField7: str | None = ""
    addField8: str | None = ""
    addField9: str | None = ""
    addField10: str | None = ""
    addField11: str | None = ""
    addField12: str | None = ""
    addField13: str | None = ""
    addField14: str | None = ""
    addField15: str | None = ""
    addField16: str | None = ""
    addField17: str | None = ""
    addField18: str | None = ""
    addField19: str | None = ""
    addField20: str | None = ""
    createDate: str | None = ""


class PersonBriefDto(BaseModel):
    Name: str
    FirstName: str = ""
    SecondName: str = ""
    BirthDate: str = ""


class EntryPoint(BaseModel):
    servID: str
    subDeviceNo: int
    subDeviceName: str


class AccessLevel(BaseModel):
    servID: str
    id: int
    name: str


class AccessPoint(BaseModel):
    servID: str
    subDeviceNo: int
    subDeviceName: str


class PassInDto(BaseModel):
    cardCode: str = ""
    personData: BastionIKSPersonDto | str
    passType: str = ""
    dateFrom: str = ""
    dateTo: str = ""
    cardStatus: int
    timeInterval: TimeIntervalDto | str = ""
    entryPoints: List[EntryPoint] | str = []
    accessLevels: List[AccessLevel] | str = []
    passCat: str
    createDate: str
    issueDate: str = ""
    pincode: int | str = ""
