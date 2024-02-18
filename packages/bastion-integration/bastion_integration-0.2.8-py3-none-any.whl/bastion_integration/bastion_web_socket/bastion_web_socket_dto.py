from datetime import datetime

from pydantic import BaseModel


class PersonalInfo(BaseModel):
    personId: int = None
    birthPlace: str
    birthDate: str
    documentNumber: str
    documentSeries: str
    # documentIssueOrgan: int
    documentIssueDate: str
    phone: str
    address: str


# class BastionOperatorInfo(BaseModel):
#     login: str
#     password: str
#
#
# class BastionServerConfig(BaseModel):
#     host: str
#     port: int
#     certificate: str = None
#
#
# class HandShakeConfig(BaseModel):
#     role_type: str
#     host_name: str
#     socket_id: int

#
# class BastionWebSocketConfig(BaseModel):
#     server_config: BastionServerConfig
#     operator_info: BastionOperatorInfo
#     enable_integration: bool = False
#     handshake: HandShakeConfig

#
# class HandShakeDto(BaseModel):
#     role_type: str  # Bastion
#     host_name: str  # EEJKEEHOME
#     socket_id: int  # 100


class BastionWebSocketPersonDto:
    class Create(BaseModel):
        name: str  # "Тестов"
        firstName: str  # "Тест"
        secondName: str  # "123987"

        tableNo: str = ""  # "123987"
        comments: str = ""  # "Без комментариев"
        organizationNodeId: int = None  # 2
        positionId: int = None  # 141

        addField1: str = ""  # "Значение дополнительного поля 1",
        addField2: str = ""  # ""
        addField3: str = ""  # ""
        addField4: str = ""  # ""
        addField5: str = ""  # ""
        addField6: str = ""  # ""
        addField7: str = ""  # ""
        addField8: str = ""  # ""
        addField9: str = ""  # ""
        addField10: str = ""  # ""
        addField11: str = ""  # ""
        addField12: str = ""  # ""
        addField13: str = ""  # ""
        addField14: str = ""  # ""
        addField15: str = ""  # ""
        addField16: str = ""  # ""
        addField17: str = ""  # ""
        addField18: str = ""  # ""
        addField19: str = ""  # ""
        addField20: str = ""  # ""
        createDate: str = datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S.%f+04:00")

        personal_info: PersonalInfo | None

    class Get(BaseModel):
        name: str = None
        firstName: str = None
        secondName: str = None
        orgNodeId: str = None
        tableNumber: str = None
        birthDate: str = None

    class Update(BaseModel):
        id: int
        name: str = None  # "Тестов"
        firstName: str = None  # "Тест"
        secondName: str = None  # "123987"
        tableNo: str = None  # "123987"
        comments: str = None  # "Без комментариев"
        organizationNodeId: int = None  # 2
        positionId: int = None  # 141

        addField1: str = None  # "Значение дополнительного поля 1",
        addField2: str = None  # ""
        addField3: str = None  # ""
        addField4: str = None  # ""
        addField5: str = None  # ""
        addField6: str = None  # ""
        addField7: str = None  # ""
        addField8: str = None  # ""
        addField9: str = None  # ""
        addField10: str = None  # ""
        addField11: str = None  # ""
        addField12: str = None  # ""
        addField13: str = None  # ""
        addField14: str = None  # ""
        addField15: str = None  # ""
        addField16: str = None  # ""
        addField17: str = None  # ""
        addField18: str = None  # ""
        addField19: str = None  # ""
        addField20: str = None  # ""
        createDate: str = None

        personal_info: PersonalInfo | None


class OrganizationDto:
    class Create(BaseModel):
        id: int = None
        name: str
        parentId: int = 0
        type: int = 0

    class Update(BaseModel):
        id: int
        name: str
        parentId: int = 0
        type: int = 0

    class Delete(BaseModel):
        id: int
        # name: str
        # parentId: int = 0
        # type: # int = 0


class DepartmentDto:
    class Create(BaseModel):
        name: str
        parentId: int
        type: int = 1

    class Update(BaseModel):
        id: int
        name: str
        parentId: int = None
        type: int = 1


class PassDto:
    class Create(BaseModel):
        passCategoryId: int
        accessLevelId: int
        personId: int
        priority: int
        createDate: str = datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S.%f+04:00")


