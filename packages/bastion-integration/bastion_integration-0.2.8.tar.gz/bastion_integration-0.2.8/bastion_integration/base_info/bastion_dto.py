from pydantic import BaseModel


class BastionServerConfig(BaseModel):
    host: str
    port: int
    certificate: str = None
    https: bool = False


class BastionOperatorInfo(BaseModel):
    login: str
    password: str


class HandShakeConfig(BaseModel):
    role_type: str
    host_name: str
    socket_id: int


class BastionConfigDto(BaseModel):
    server_config: BastionServerConfig
    operator_info: BastionOperatorInfo
    handshake: HandShakeConfig | None = None


class BastionDepartmentDto:
    class Create(BaseModel):
        department_name: str
        organization_name: str

    class Update(BaseModel):
        old_name: str
        new_name: str
        organization_name: str = None


class PersonDto:
    class Create(BaseModel):
        rfid: str | None = None
        last_name: str
        first_name: str
        middle_name: str
        organization_name: str
        department_name: str
        job_title: str
        date_of_birth: str
        doc_issue_organ: str
        doc_issue_date: str | None = None
        doc_series: str
        doc_number: str
        birth_place: str
        address: str | None = None
        phone: str

        visit_start_date: str | None = None
        visit_end_date: str | None = None
        comments: str | None = None

        access_level_id: int | None = None
        pass_category: str

