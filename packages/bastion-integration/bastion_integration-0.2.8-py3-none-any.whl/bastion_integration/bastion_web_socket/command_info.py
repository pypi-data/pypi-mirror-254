from datetime import datetime

from bastion_integration.base_info.bastion_dto import HandShakeConfig
from bastion_integration.bastion_web_socket.bastion_web_socket_dto import PassDto
from bastion_integration.bastion_web_socket.request_types import RequestName, REQUEST_COMMAND


class WebSocketCommand:

    def login(self, login: str, password: str):
        return {"request_name": RequestName.LOGIN.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.Operators.LoginRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "authorizationParams": {
                        "$type": "ESprom.Taurus.Roles.NetCenter.Operators"
                                 ".UserPasswordAuthorizationParams, "
                                 "ESprom.Taurus.NetCenter.Common",
                        "user": login,
                        "password": password
                    },
                    "id": 0,
                }}

    def net_center_status(self):
        return {"request_name": RequestName.NET_CENTER_STATUS.name,
                "$type": "ESprom.Taurus.Protocol.RequestCommand, ESprom.Taurus.Platform",
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.NetCenterInitStateRequest, "
                             "ESprom.Taurus.NetCenter.Common"}}

    def handshake(self, dto: HandShakeConfig):
        return {"request_name": RequestName.HANDSHAKE.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.HandshakeRequest, ESprom.Taurus.NetCenter.Common",
                    "roleType": dto.role_type,
                    "hostName": dto.host_name,
                    "socketId": dto.socket_id,
                    "id": 0
                }}

    def get_operator_info(self, operator_id):
        return {"request_name": RequestName.GET_OPERATOR_INFO.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.Operators.OperatorRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "operatorId": operator_id,
                    "id": 0
                }}

    def get_all_organization_and_departments(self):
        return {"request_name": RequestName.GET_ORGANIZATIONS_AND_DEPARTMENTS.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.Persons"
                             ".OrganizationStructureListRequest, "
                             "ESprom.Taurus.NetCenter.Common.Persons",
                    "id": 0}}

    def create_organization(self, organization_name: str):
        return {"request_name": RequestName.CREATE_ORGANIZATION.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.UpdateDataRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "updateDescription": {
                        "$type": "System.Collections.Generic.List`1[["
                                 "ESprom.Taurus.Roles.NetCenter.UpdateOperation, "
                                 "ESprom.Taurus.NetCenter.Common]],mscorlib",
                        "$values": [
                            {
                                "$type": "ESprom.Taurus.Roles.NetCenter.Add`1[["
                                         "ESprom.Taurus.Roles.NetCenter.Persons"
                                         ".OrganizationNode,"
                                         "ESprom.Taurus.NetCenter.Common.Persons]], "
                                         "ESprom.Taurus.NetCenter.Common",
                                "target": {
                                    "name": organization_name,
                                    "parentId": 0,
                                    "type": 0
                                }
                            }
                        ]
                    },
                    "id": 0
                }}

    def update_organization(self, organization_id: int, new_name: str):
        return {"request_name": RequestName.UPDATE_ORGANIZATION.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.UpdateDataRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "updateDescription": {
                        "$type": "System.Collections.Generic.List`1[["
                                 "ESprom.Taurus.Roles.NetCenter.UpdateOperation, "
                                 "ESprom.Taurus.NetCenter.Common]],mscorlib",
                        "$values": [
                            {
                                "$type": "ESprom.Taurus.Roles.NetCenter.Update`1[["
                                         "ESprom.Taurus.Roles.NetCenter.Persons"
                                         ".OrganizationNode,"
                                         "ESprom.Taurus.NetCenter.Common.Persons]], "
                                         "ESprom.Taurus.NetCenter.Common",
                                "target": {
                                    "id": organization_id,
                                    "name": new_name,
                                    "parentId": 0,
                                    "type": 0
                                }
                            }
                        ]
                    },
                    "id": 0
                }}

    def delete_organization(self, organization_id: int):
        return {"request_name": RequestName.DELETE_ORGANIZATION.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.UpdateDataRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "updateDescription": {
                        "$type": "System.Collections.Generic.List`1[["
                                 "ESprom.Taurus.Roles.NetCenter.UpdateOperation, "
                                 "ESprom.Taurus.NetCenter.Common]],mscorlib",
                        "$values": [
                            {
                                "$type": "ESprom.Taurus.Roles.NetCenter.Delete`1[["
                                         "ESprom.Taurus.Roles.NetCenter.Persons"
                                         ".OrganizationNode,"
                                         "ESprom.Taurus.NetCenter.Common.Persons]], "
                                         "ESprom.Taurus.NetCenter.Common",
                                "target": {
                                    "id": organization_id
                                }
                            }
                        ]
                    },
                    "id": 0
                }}

    def create_department(self, department_name: str, organization_id: int):
        return {"request_name": RequestName.CREATE_DEPARTMENT.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.UpdateDataRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "updateDescription": {
                        "$type": "System.Collections.Generic.List`1[["
                                 "ESprom.Taurus.Roles.NetCenter.UpdateOperation, "
                                 "ESprom.Taurus.NetCenter.Common]],mscorlib",
                        "$values": [
                            {
                                "$type": "ESprom.Taurus.Roles.NetCenter.Add`1[["
                                         "ESprom.Taurus.Roles.NetCenter.Persons"
                                         ".OrganizationNode,"
                                         "ESprom.Taurus.NetCenter.Common.Persons]], "
                                         "ESprom.Taurus.NetCenter.Common",
                                "target": {
                                    "name": department_name,
                                    "parentId": organization_id,
                                    "type": 1
                                }
                            }
                        ]
                    },
                    "id": 0
                }}

    def update_department(self, department_id: int, new_name: str, parent_id: int):
        return {"request_name": RequestName.UPDATE_DEPARTMENT.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.UpdateDataRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "updateDescription": {
                        "$type": "System.Collections.Generic.List`1[["
                                 "ESprom.Taurus.Roles.NetCenter.UpdateOperation, "
                                 "ESprom.Taurus.NetCenter.Common]],mscorlib",
                        "$values": [
                            {
                                "$type": "ESprom.Taurus.Roles.NetCenter.Update`1[["
                                         "ESprom.Taurus.Roles.NetCenter.Persons"
                                         ".OrganizationNode,"
                                         "ESprom.Taurus.NetCenter.Common.Persons]], "
                                         "ESprom.Taurus.NetCenter.Common",
                                "target": {
                                    "id": department_id,
                                    "name": new_name,
                                    "parentId": parent_id,
                                    "type": 1
                                }
                            }
                        ]
                    },
                    "id": 0
                }}

    def delete_department(self, department_id: int):
        return {"request_name": RequestName.DELETE_DEPARTMENT.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.UpdateDataRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "updateDescription": {
                        "$type": "System.Collections.Generic.List`1[["
                                 "ESprom.Taurus.Roles.NetCenter.UpdateOperation, "
                                 "ESprom.Taurus.NetCenter.Common]],mscorlib",
                        "$values": [
                            {
                                "$type": "ESprom.Taurus.Roles.NetCenter.Delete`1[["
                                         "ESprom.Taurus.Roles.NetCenter.Persons"
                                         ".OrganizationNode,"
                                         "ESprom.Taurus.NetCenter.Common.Persons]], "
                                         "ESprom.Taurus.NetCenter.Common",
                                "target": {
                                    "id": department_id
                                }
                            }
                        ]
                    },
                    "id": 0
                }}

    def create_pass(self, dto: PassDto.Create):
        return {"request_name": RequestName.CREATE_PASS.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.UpdateDataRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "updateDescription": {
                        "$type": "System.Collections.Generic.List`1[["
                                 "ESprom.Taurus.Roles.NetCenter.UpdateOperation, "
                                 "ESprom.Taurus.NetCenter.Common]],mscorlib",
                        "$values": [
                            {
                                "$type": "ESprom.Taurus.Roles.NetCenter.Add`1[["
                                         "ESprom.Taurus.Roles.NetCenter.Persons.Pass,"
                                         "ESprom.Taurus.NetCenter.Common.Persons]], "
                                         "ESprom.Taurus.NetCenter.Common",
                                "target": dto.dict(exclude_none=True)
                            }
                        ]
                    },
                    "id": 0
                }}

    def create_card(self, card_code: str):
        return {"request_name": RequestName.CREATE_CARD.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.UpdateDataRequest, "
                             "ESprom.Taurus.NetCenter.Common",
                    "updateDescription": {
                        "$type": "System.Collections.Generic.List`1[["
                                 "ESprom.Taurus.Roles.NetCenter.UpdateOperation, "
                                 "ESprom.Taurus.NetCenter.Common]],mscorlib",
                        "$values": [
                            {
                                "$type": "ESprom.Taurus.Roles.NetCenter.Add`1[["
                                         "ESprom.Taurus.Roles.NetCenter.Persons.Card,"
                                         "ESprom.Taurus.NetCenter.Common.Persons]], "
                                         "ESprom.Taurus.NetCenter.Common",
                                "target": {
                                    "fullCardCode": int(card_code, 16),
                                    "createDate": datetime.now().astimezone().strftime(
                                        "%Y-%m-%dT%H:%M:%S.%f+04:00")
                                }
                            }
                        ]
                    },
                    "id": 0
                }}

    def issue_pass(self, pass_id: int, card_id: int):
        return {"request_name": RequestName.ISSUE_PASS.name,
                "$type": "ESprom.Taurus.Protocol.RequestCommand, ESprom.Taurus.Platform",
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.Persons.IssuePassRequest, "
                             "ESprom.Taurus.NetCenter.Common.Persons",
                    "passId": pass_id,
                    "cardId": card_id,
                    "id": 0
                }}

    def set_pin_code(self, pass_id: int, pin_code: str):
        return {"request_name": RequestName.SET_PIN_CODE.name,
                "$type": REQUEST_COMMAND,
                "request": {
                    "$type": "ESprom.Taurus.Roles.NetCenter.UpdateDataRequest, ESprom.Taurus.NetCenter.Common",
                    "updateDescription": {
                        "$type": "System.Collections.Generic.List`1[[ESprom.Taurus.Roles.NetCenter.UpdateOperation, "
                                 "ESprom.Taurus.NetCenter.Common]],mscorlib",
                        "$values": [
                            {
                                "$type": "ESprom.Taurus.Roles.NetCenter.Add`1[["
                                         "ESprom.Taurus.Roles.NetCenter.Persons.PinCode,"
                                         "ESprom.Taurus.NetCenter.Common.Persons]], ESprom.Taurus.NetCenter.Common",
                                "target": {
                                    "passId": pass_id,
                                    "code": pin_code
                                }
                            }
                        ]
                    },
                    "id": 0
                }}
