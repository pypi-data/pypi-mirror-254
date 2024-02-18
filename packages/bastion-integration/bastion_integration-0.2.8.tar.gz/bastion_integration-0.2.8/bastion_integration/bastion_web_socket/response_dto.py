from pydantic import BaseModel

from bastion_integration.bastion_web_socket.bastion_web_socket_dto import PersonalInfo


class OrganizationResponseDto(BaseModel):
    id: int | None
    name: str
    parent_id: int
    type: int


class DepartmentResponseDto(BaseModel):
    id: int | None
    name: str
    parent_id: int
    type: int


class PersonResponseDto(BaseModel):
    id: int | None = None
    name: str | None = None
    firstName: str | None = None
    secondName: str | None = None
    tableNo: str | None = None
    comments: str | None = None
    createDate: str | None = None

    birthPlace: str | None = None
    birthDate: str | None = None
    documentNumber: str | None = None
    documentSeries: str | None = None
    documentIssueDate: str | None = None
    phone: str | None = None
    address: str | None = None

