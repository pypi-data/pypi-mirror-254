import asyncio
import json
import time
from typing import List

import websockets
import yaml
from loguru import logger

from bastion_integration.base_info.bastion_dto import PersonDto, BastionConfigDto, HandShakeConfig
from bastion_integration.base_info.custom_error_handler import BastionIntegrationError
from bastion_integration.bastion_web_socket.bastion_web_socket_dto import PassDto, PersonalInfo, \
    BastionWebSocketPersonDto
from bastion_integration.bastion_web_socket.command_info import WebSocketCommand
from bastion_integration.bastion_web_socket.request_types import RequestName, REQUEST_COMMAND
from bastion_integration.bastion_web_socket.response_dto import OrganizationResponseDto, DepartmentResponseDto, \
    PersonResponseDto


class CoreWebSocket:
    send_messages = True
    bastion_socket = None
    count = 0

    sleep_time = 2
    log_response = False
    log_request = False

    def __init__(self, config: BastionConfigDto):
        self.config = config
        self.send_messages = True
        self.log_response = False
        self.log_request = False
        self.request_info = {}
        self.response_info = [{
        }]
        self.command = WebSocketCommand()

    #  ===============================================================================
    async def _bastion_read_message_(self):
        async for message in self.bastion_socket:
            dict_message = yaml.load(message, Loader=yaml.FullLoader)
            try:
                response_info = json.dumps(dict_message, indent=4)
                self.response_info.append(dict_message)
                # if self.log_response:
                # logger.debug(response_info)
            except Exception as e:
                raise BastionIntegrationError(f"Read message error: {e}")

    async def _bastion_web_socket_(self):
        self.bastion_socket = await websockets.connect(f"ws://{self.config.server_config.host}:"
                                                       f"{self.config.server_config.port}/api_v1")

    async def _bastion_send_message(self, message: dict, custom_web_socket: websockets.WebSocketClientProtocol = None):
        self.count += 1
        if message.get("request_name"):
            self.request_info.update({self.count: message.get("request_name")})
            message.pop("request_name")
        try:
            message['request']['id'] = self.count
            if self.log_request:
                logger.info(json.dumps(message, indent=4))
        except TypeError as e:
            logger.warning(message)
            raise BastionIntegrationError(f"Bastion send message error: {e}")

        if self.send_messages:
            try:
                if custom_web_socket:
                    await custom_web_socket.send(str(message))
                else:
                    await self.bastion_socket.send(str(message))
            except Exception as e:
                raise BastionIntegrationError(f"Integration not enabled: {e}")

    async def _get_response_info(self, _request_name: RequestName):
        for request_id, request_name in self.request_info.items():
            if request_name == _request_name.name:
                for response in self.response_info:
                    if replay := response.get("reply"):
                        if replay.get("exception"):
                            error_in = self.request_info.get(replay.get("requestId"))
                            raise BastionIntegrationError(
                                f"{error_in} - {replay.get('exception').get('message')} - {replay.get('exception').get('comments')}")
                        if request_id == replay.get("requestId"):
                            self.request_info.pop(request_id)
                            self.response_info.remove(response)
                            # logger.info(json.dumps(replay, indent=4))
                            return replay

    #  ===============================================================================
    async def _start_websocet(self):
        await self._bastion_web_socket_()
        asyncio.create_task(self._bastion_read_message_())

    async def init(self):

        await self._start_websocet()
        await self.net_center_status()
        await self.login(login=self.config.operator_info.login, password=self.config.operator_info.password)
        await self.handshake(self.config.handshake)

    #  ===============================================================================
    async def _send_message(self, data: dict):
        await self._bastion_send_message(data)
        await asyncio.sleep(self.sleep_time)

    #  ===============================================================================
    async def net_center_status(self):
        await self._send_message(data=self.command.net_center_status())
        response = await self._get_response_info(RequestName.NET_CENTER_STATUS)
        return {
            "session_id": response.get("body").get("sessionUid"),
            "status": response.get("body").get("state")
        }

    async def login(self, login: str, password: str) -> int:
        await self._send_message(data=self.command.login(login=login, password=password))
        response = await self._get_response_info(RequestName.LOGIN)
        return {"operator_id": response.get("body")}

    async def handshake(self, dto: HandShakeConfig):
        await self._send_message(data=self.command.handshake(dto=dto))
        return await self._get_response_info(RequestName.HANDSHAKE)

    #  ===============================================================================

    async def _check_connection(self, only_ping: bool = True, **kwargs):
        if only_ping:
            answer = await self.net_center_status()
            if not answer.get("status") == "Normal":
                logger.critical(f"Connection error. Status: {answer.get('status')}")
                return False
            else:
                return True

        host = kwargs.get("bastion_host") if kwargs.get("bastion_host") else self.config.server_config.host
        port = kwargs.get("bastion_port") if kwargs.get("bastion_port") else self.config.server_config.port
        login = kwargs.get("bastion_operator_login") if kwargs.get(
            "bastion_operator_login") else self.config.operator_info.login
        password = kwargs.get("bastion_operator_password") if kwargs.get(
            "bastion_operator_password") else self.config.operator_info.password

        socket_id = kwargs.get("bastion_handshake_socket_id") if kwargs.get(
            "bastion_handshake_socket_id") else self.config.handshake.socket_id
        host_name = kwargs.get("bastion_handshake_host_name") if kwargs.get(
            "bastion_handshake_host_name") else self.config.handshake.host_name
        role_type = kwargs.get("bastion_handshake_role_type") if kwargs.get(
            "bastion_handshake_role_type") else self.config.handshake.role_type
        try:
            # web_socket = await websockets.connect(f"ws://{host}:{port}/api_v1")

            await self._bastion_send_message(self.command.net_center_status())
            await asyncio.sleep(self.sleep_time)
            check_host_and_port_answer = await self._get_response_info(RequestName.NET_CENTER_STATUS)
            if not check_host_and_port_answer.get("body").get("state") == "Normal":
                logger.critical(
                    f"Check host and port. Connection error. Status: {check_host_and_port_answer.get('body').get('state')}")
                return False
            await self._bastion_send_message(self.command.login(login=login, password=password))
            await asyncio.sleep(self.sleep_time)
            check_login_and_password_answer = await self._get_response_info(RequestName.LOGIN)
            if not check_login_and_password_answer.get("body"):
                logger.critical(
                    f"Check login and password. Connection error. Status: {check_login_and_password_answer.get('body')}")
                return False
            await self._bastion_send_message(
                self.command.handshake(dto=HandShakeConfig(role_type=role_type, host_name=host_name, socket_id=socket_id)))
            await asyncio.sleep(self.sleep_time)
            await self._get_response_info(RequestName.HANDSHAKE)
        except Exception as e:
            logger.warning(e)
            return False

        return True

    #  ===============================================================================

    async def get_operator_info(self, operator_id: int):
        await self._send_message(data=self.command.get_operator_info(operator_id=operator_id))
        response = await self._get_response_info(RequestName.GET_OPERATOR_INFO)
        return {
            "operator_id": response.get("body").get("id"),
            "operator_name": response.get("body").get("name"),
            "operator_role_id": response.get("body").get("roleId"),
            "operator_active": response.get("body").get("isActive")
        }

    async def get_pass_category(self):
        await self._send_message(data={"request_name": RequestName.GET_PASS_CATEGORY.name,
                                       "$type": REQUEST_COMMAND,
                                       "request": {
                                           "$type": "ESprom.Taurus.Roles.NetCenter.Persons.PassCategoriesRequest, "
                                                    "ESprom.Taurus.NetCenter.Common.Persons",
                                           "id": 0
                                       }})
        response = await self._get_response_info(RequestName.GET_PASS_CATEGORY)
        passes = response.get("body").get("$values")
        _passes = []
        for _pass in passes:
            _passes.append({
                "id": _pass.get("id"),
                "name": _pass.get("name"),
                "time_restriction_value": _pass.get("timeRestrictionValue"),
                "photo_identification_form_id": _pass.get("photoIdentificationFormId"),
                "is_change_pass_end_date_allowed": _pass.get("isChangePassEndDateAllowed"),
                "is_pass_prolongation_allowed": _pass.get("isPassProlongationAllowed"),
                "time_restriction_rule": _pass.get("timeRestrictionRule"),
                "time_restriction_unit": _pass.get("timeRestrictionUnit")
            })
        return _passes

    async def get_rights_for_person(self):
        await self._send_message(data={"request_name": RequestName.GET_RIGHTS_FOR_PERSON.name,
                                       "$type": REQUEST_COMMAND,
                                       "request": {
                                           "$type": "ESprom.Taurus.Roles.NetCenter.GlobalSettingsEntryRequest, "
                                                    "ESprom.Taurus.NetCenter.Common",
                                           "entryType": "ESprom.Taurus.Roles.NetCenter.Persons.ComparePersonRule, "
                                                        "ESprom.Taurus.NetCenter.Common.Persons,Version=2.2.0.0, "
                                                        "Culture=neutral, PublicKeyToken=null",
                                           "id": 0
                                       }})
        response = await self._get_response_info(RequestName.GET_RIGHTS_FOR_PERSON)
        right_info = {
            "compare_by_full_name": response.get("body").get("compareByFullName"),
        }
        return right_info

    async def _get_organizations_and_departments(self):
        await self._send_message(data=self.command.get_all_organization_and_departments())
        response = await self._get_response_info(RequestName.GET_ORGANIZATIONS_AND_DEPARTMENTS)
        org_and_dep_info = []
        for info in response.get("body").get("$values"):
            org_and_dep_info.append({
                "id": info.get("id"),
                "name": info.get("name"),
                "parent_id": info.get("parentId"),
                "type": info.get("type")
            })
        return org_and_dep_info

    async def get_organization(self, organization_name: str = None):
        response = await self._get_organizations_and_departments()
        organizations = []
        departments = []
        items = []
        for model in response:
            if model.get("type") == 0:
                organizations.append({"organization_name": model.get("name"), "id": model.get("id")})
            if model.get("type") == 1:
                if model not in departments:
                    departments.append(model)

        for organization in organizations:
            departments_list = []
            for department in departments:
                if organization.get("id") == department.get("parent_id"):
                    departments_list.append(department.get("name"))
            items.append({"organization_name": organization.get("organization_name"), "departments_name": departments_list})
        if organization_name:
            for item in items:
                if item.get("organization_name") == organization_name:
                    return item
            return None
        return items

    async def get_department(self, department_name: str = None) -> DepartmentResponseDto | List[DepartmentResponseDto]:
        response = await self._get_organizations_and_departments()
        organizations = {}
        departments = []
        for model in response:
            if model.get("type") == 0:
                organizations.update({model.get("id"): model.get("name")})
        for model in response:
            if model.get("type") == 1:
                departments.append(
                    {"department_name": model.get("name"), "organizatioin": organizations.get(model.get("parent_id"))})

        departments_info = []
        if department_name:
            for department in departments:
                if department.get("department_name") == department_name:
                    departments_info.append(
                        {"department_name": department.get("department_name"),
                         "organizatioin": department.get("organizatioin")})
            return departments_info
        return departments

    async def _check_organization(self, name: str, exist: bool = False):
        organizations = await self.get_organization()
        _organization_names = []
        for org in organizations:
            _organization_names.append(org.name)
        if name not in _organization_names:
            return False
            # raise BastionV3Error(**get_bastion_error(BastionErrorTypes.organization_not_found_error))
        else:
            return True
            # raise BastionV3Error("Организация с таким именем уже существует")

    async def _check_department(self, name) -> bool:
        departments = await self.get_department()
        if type(departments) == list:
            for dep in departments:
                if name == dep.name:
                    raise BastionIntegrationError(f"Department with name {name} already exist")
        else:
            if name == departments.name:
                raise BastionIntegrationError(f"Department with name {name} already exist")

    async def create_organization(self, organization_name: str) -> OrganizationResponseDto:
        if await self.get_organization(organization_name):
            raise BastionIntegrationError("Организация с таким именем уже существует")
        await self._send_message(data=self.command.create_organization(organization_name))
        await self._get_response_info(RequestName.CREATE_ORGANIZATION)
        return await self.get_organization(organization_name=organization_name)

    async def update_organization(self, old_name: str, new_name: str) -> OrganizationResponseDto:
        await self._send_message(data=self.command.get_all_organization_and_departments())
        response = await self._get_response_info(RequestName.GET_ORGANIZATIONS_AND_DEPARTMENTS)
        org_and_dep_info = []
        organizations_names = []
        organizations_dict = {}
        for info in response.get("body").get("$values"):
            if info.get("type") == 0:
                org_and_dep_info.append({
                    "id": info.get("id"),
                    "name": info.get("name"),
                    "parent_id": info.get("parentId"),
                    "type": info.get("type")})
                organizations_names.append(info.get("name"))
                organizations_dict.update({info.get("name"): info.get("id")})
        if old_name not in organizations_names:
            raise BastionIntegrationError("Организация с таким именем не существует")
        if new_name in organizations_names:
            raise BastionIntegrationError("Организация с таким именем уже существует")

        await self._send_message(data=self.command.update_organization(organizations_dict.get(old_name), new_name))
        await self._get_response_info(RequestName.UPDATE_ORGANIZATION)

        return await self.get_organization(organization_name=new_name)

    async def create_department(self, department_name: str, organization_name: str) -> DepartmentResponseDto:
        response = await self._get_organizations_and_departments()
        organizations = {}
        departments = {}
        for model in response:
            if model.get("type") == 0:
                organizations.update({model.get("name"): model.get("id")})
            if model.get("type") == 1:
                departments.update({model.get("name"): [model.get("id"), model.get("parent_id")]})

        if not (_id := organizations.get(organization_name)):
            raise BastionIntegrationError("Организация с таким именем не существует")
        if depart := departments.get(department_name):
            if depart[1] == _id:
                raise BastionIntegrationError("Департамент с таким именем уже существует")

        await self._send_message(data=self.command.create_department(department_name=department_name,
                                                                     organization_id=_id))
        await self._get_response_info(RequestName.CREATE_DEPARTMENT)
        return await self.get_department(department_name=department_name)

    async def update_department(self, old_name: str, new_name: str, organization_name: str,
                                new_organization_name: str = None):
        await self._send_message(data=self.command.get_all_organization_and_departments())
        response = await self._get_response_info(RequestName.GET_ORGANIZATIONS_AND_DEPARTMENTS)
        org_id = None
        new_org_id = None
        for info in response.get("body").get("$values"):
            if info.get("type") == 0:
                if organization_name == info.get("name"):
                    org_id = info.get("id")
                if new_organization_name and new_organization_name == info.get("name"):
                    new_org_id = info.get("id")
        if not org_id:
            raise BastionIntegrationError("Организация с таким именем не существует")

        depart = [{"id": info.get("id"), "name": info.get("name")} for info in response.get("body").get("$values") if
                  info.get("type") == 1 and info.get("parentId") == org_id]
        dep_id = None
        for dep in depart:
            if dep.get("name") == new_name:
                raise BastionIntegrationError("Департамент с таким именем уже существует")
            if dep.get("name") == old_name:
                dep_id = dep.get("id")
        if not dep_id:
            raise BastionIntegrationError("Департамент с таким именем не существует")

        await self._send_message(
            data=self.command.update_department(dep_id, new_name, new_org_id if new_org_id else org_id))
        await self._get_response_info(RequestName.UPDATE_DEPARTMENT)

        return await self.get_department(department_name=new_name)

    async def delete_organization(self, organization_name: str):
        await self._send_message(data=self.command.get_all_organization_and_departments())
        response = await self._get_response_info(RequestName.GET_ORGANIZATIONS_AND_DEPARTMENTS)
        org_and_dep_info = []
        organizations_names = []
        organizations_dict = {}
        departments_info = []
        for info in response.get("body").get("$values"):
            if info.get("type") == 0:
                org_and_dep_info.append({
                    "id": info.get("id"),
                    "name": info.get("name"),
                    "parent_id": info.get("parentId"),
                    "type": info.get("type")})
                organizations_names.append(info.get("name"))
                organizations_dict.update({info.get("name"): info.get("id")})
            if info.get("type") == 1:
                departments_info.append({
                    "id": info.get("id"),
                    "name": info.get("name"),
                    "parent_id": info.get("parentId"),
                    "type": info.get("type")})
        deleted_departments = []
        if organization_name not in organizations_names:
            raise BastionIntegrationError("Организация с таким именем не существует")
        for department in departments_info:
            if department.get("parent_id") == organizations_dict.get(organization_name):
                deleted_departments.append(department)
                await self._send_message(data=self.command.delete_department(department.get("id")))
                await self._get_response_info(RequestName.GET_ORGANIZATIONS_AND_DEPARTMENTS)
                time.sleep(1)

        await self._send_message(data=self.command.delete_organization(organizations_dict.get(organization_name)))
        await self._get_response_info(RequestName.DELETE_ORGANIZATION)
        return {"organization_name": organization_name, "departments_name": deleted_departments}

    async def delete_department(self, department_name: str, organization_name: str):
        await self._send_message(data=self.command.get_all_organization_and_departments())
        response = await self._get_response_info(RequestName.GET_ORGANIZATIONS_AND_DEPARTMENTS)
        org_id = None
        dep_id = None
        department_info = []
        for info in response.get("body").get("$values"):
            if info.get("type") == 0:
                if organization_name == info.get("name"):
                    org_id = info.get("id")
            if info.get("type") == 1:
                if department_name == info.get("name"):
                    department_info.append({
                        "id": info.get("id"),
                        "name": info.get("name"),
                        "parent_id": info.get("parentId"),
                        "type": info.get("type")
                    })
        if not org_id:
            raise BastionIntegrationError("Организация с таким именем не существует")
        for depart in department_info:
            if org_id == depart.get("parent_id"):
                dep_id = depart.get("id")
        if not dep_id:
            raise BastionIntegrationError("Департамент с таким именем не существует")

        await self._send_message(data=self.command.delete_department(dep_id))
        await self._get_response_info(RequestName.DELETE_DEPARTMENT)
        return [{"department_name": department_name, "organization_name": organization_name}]

    async def get_dict_info(self, dict_category_id: int = None):
        if dict_category_id:
            await self._send_message(data={"request_name": RequestName.GET_DICT_INFO_ONE_CATEGORY.name,
                                           "$type": REQUEST_COMMAND,
                                           "request": {
                                               "$type": "ESprom.Taurus.Roles.NetCenter.Persons"
                                                        ".DictionaryRecordsRequest, "
                                                        "ESprom.Taurus.NetCenter.Common.Persons",
                                               "dictionaryHeaderId": dict_category_id,
                                               "id": 0}})
            response = await self._get_response_info(RequestName.GET_DICT_INFO_ONE_CATEGORY)
            dict_info = {}
            for info in response.get("body").get("$values"):
                dict_info.update({
                    "id": info.get("id"),
                    "dictionary_header_id": info.get("dictionaryHeaderId"),
                    "value": info.get("value"),
                })
            return dict_info
        else:
            await self._send_message(data={"request_name": RequestName.GET_DICT_INFO.name,
                                           "$type": REQUEST_COMMAND,
                                           "request": {
                                               "$type": "ESprom.Taurus.Roles.NetCenter.Persons"
                                                        ".DictionaryHeadersRequest, "
                                                        "ESprom.Taurus.NetCenter.Common.Persons",
                                               "id": 0}})
            response = await self._get_response_info(RequestName.GET_DICT_INFO)
            dict_info = []
            for info in response.get("body").get("$values"):
                dict_info.append({
                    "id": info.get("id"),
                    "name": info.get("name")
                })
            return dict_info

    async def get_access_level_info(self, access_level_id: int = None):
        if access_level_id:
            await self._send_message(data={"request_name": RequestName.GET_ONE_ACCESS_LEVEL.name,
                                           "$type": REQUEST_COMMAND,
                                           "request": {
                                               "$type": "ESprom.Taurus.Roles.NetCenter.Persons"
                                                        ".AccessLevelContentCompositionRequest, "
                                                        "ESprom.Taurus.NetCenter.Common.Persons",
                                               "accessLevelId": access_level_id,
                                               "id": 0
                                           }})
            response = await self._get_response_info(RequestName.GET_ONE_ACCESS_LEVEL)
            return response
        else:
            await self._send_message(data={"request_name": RequestName.GET_ALL_ACCESS_LEVELS.name,
                                           "$type": REQUEST_COMMAND,
                                           "request": {
                                               "$type": "ESprom.Taurus.Roles.NetCenter.Persons.AccessLevelListRequest, "
                                                        "ESprom.Taurus.NetCenter.Common.Persons",
                                               "id": 0
                                           }})
            response = await self._get_response_info(RequestName.GET_ALL_ACCESS_LEVELS)
            _infos = []
            for info in response.get("body").get("$values"):
                _infos.append({
                    "id": info.get("id"),
                    "physical_number": info.get("physicalNumber"),
                    "name": info.get("name"),
                    "main_time_block_id": info.get("mainTimeBlockId")
                })
            return _infos

    async def get_time_block(self, time_block_id: int = None):
        if time_block_id:
            await self._send_message(data={"request_name": RequestName.GET_ONE_TIME_BLOCK.name,
                                           "$type": REQUEST_COMMAND,
                                           "request": {
                                               "$type": "ESprom.Taurus.Roles.NetCenter.Persons.TimeBlockRequest, "
                                                        "ESprom.Taurus.NetCenter.Common.Persons",
                                               "timeBlockId": time_block_id,
                                               "id": 0}})

            response = await self._get_response_info(RequestName.GET_ONE_TIME_BLOCK)
            _infos = {}
            _infos.update({
                "id": response.get("body").get("id"),
                "physical_number": response.get("body").get("physicalNumber"),
                "name": response.get("body").get("name"),
                "period": response.get("body").get("period"),
                "time_zones": [{"end_time": time_zone.get("endTime"), "holidays_mask": time_zone.get("holidaysMask")}
                               for time_zone in response.get("body").get("timeZones").get("$values")]
            })
            return _infos
        else:
            await self._send_message(data={"request_name": RequestName.GET_ALL_TIME_BLOCK.name,
                                           "$type": REQUEST_COMMAND,
                                           "request": {
                                               "$type": "ESprom.Taurus.Roles.NetCenter.Persons.TimeBlockListRequest, "
                                                        "ESprom.Taurus.NetCenter.Common.Persons",
                                               "id": 0}})
            response = await self._get_response_info(RequestName.GET_ALL_TIME_BLOCK)
            _infos = []
            for info in response.get("body").get("$values"):
                _infos.append({
                    "id": info.get("id"),
                    "physical_number": info.get("physicalNumber"),
                    "name": info.get("name"),
                    "period": info.get("period"),
                    "time_zones": [
                        {"end_time": time_zone.get("endTime"), "holidays_mask": time_zone.get("holidaysMask")} for
                        time_zone in info.get("timeZones").get("$values")]
                })
            return _infos

    async def get_person(self, person_id: int) -> PersonResponseDto:
        await self._send_message(data={"request_name": RequestName.GET_PERSON_SHORT_INFO.name,
                                       "$type": REQUEST_COMMAND,
                                       "request": {
                                           "$type": "ESprom.Taurus.Roles.NetCenter.Persons.PersonRequest, "
                                                    "ESprom.Taurus.NetCenter.Common.Persons",
                                           "personId": person_id,
                                           "id": 0
                                       }})
        short_info_response = await self._get_response_info(RequestName.GET_PERSON_SHORT_INFO)
        short_info_response["body"].pop("$type")
        person_response_dto = PersonResponseDto(**short_info_response["body"])

        await self._send_message(data={"request_name": RequestName.GET_PERSONAL_INFO.name,
                                       "$type": REQUEST_COMMAND,
                                       "request": {
                                           "$type": "ESprom.Taurus.Roles.NetCenter.Persons.PersonalInfoRequest, "
                                                    "ESprom.Taurus.NetCenter.Common.Persons",
                                           "personId": person_id,
                                           "id": 0
                                       }})

        personal_info_response = await self._get_response_info(RequestName.GET_PERSONAL_INFO)

        personal_info_response["body"].pop("personId")
        personal_info_response["body"].pop("$type")
        # logger.debug(personal_info_response)
        # logger.debug(person_response_dto)
        # person_response_dto.model_copy(update=personal_info_response["body"])
        # logger.warning(person_response_dto)


        return person_response_dto

    async def _find_person(self, name: str, first_name: str, second_name: str):
        await self._send_message(data={"request_name": RequestName.FIND_PERSON.name,
                                       "$type": REQUEST_COMMAND,
                                       "request": {
                                           "$type": "ESprom.Taurus.Roles.NetCenter.Persons"
                                                    ".FindPersonRequest, "
                                                    "ESprom.Taurus.NetCenter.Common.Persons",
                                           "name": name,
                                           "firstName": first_name,
                                           "secondName": second_name,
                                           "id": 0}})
        return await self._get_response_info(RequestName.FIND_PERSON)

    async def create_person(self, dto: PersonDto.Create) -> PersonResponseDto:
        await self._send_message(data=self.command.get_all_organization_and_departments())
        response = await self._get_response_info(RequestName.GET_ORGANIZATIONS_AND_DEPARTMENTS)

        organization = [{"id": info.get("id"),
                         "name": info.get("name"),
                         "parent_id": info.get("parentId"),
                         "type": info.get("type")} for info in response.get("body").get("$values") if
                        dto.organization_name == info.get("name")][0]
        if not organization:
            raise BastionIntegrationError("Организация не найдена")
        department = [{"id": info.get("id"),
                       "name": info.get("name"),
                       "parent_id": info.get("parentId"),
                       "type": info.get("type")} for info in response.get("body").get("$values") if
                      dto.department_name == info.get("name") and info.get("parentId") == organization.get("id")][0]
        if not department:
            raise BastionIntegrationError("Отдел не найден")

        _personal_info = PersonalInfo(birthPlace=dto.birth_place,
                                      birthDate=dto.date_of_birth,
                                      documentNumber=dto.doc_number,
                                      documentSeries=dto.doc_series,
                                      documentIssueDate=dto.doc_issue_date,
                                      phone=dto.phone,
                                      address=dto.address)

        _dto = BastionWebSocketPersonDto.Create(name=dto.last_name,
                                                firstName=dto.first_name,
                                                secondName=dto.middle_name,
                                                comments=dto.comments if dto.comments else "",
                                                organizationNodeId=department.get("id"),
                                                personal_info=_personal_info
                                                )
        # if find_person_response.get("body"):
        #     if dto.name == find_person_response.get("body").get("name") and (dto.firstName == find_person_response.get(
        #             "body").get("firstName") and dto.secondName == find_person_response.get("body").get("secondName")):
        #         raise BastionV3Error(**get_bastion_error(BastionErrorTypes.person_already_exist_error))
        await self._send_message(data={"request_name": RequestName.CREATE_PERSON.name,
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
                                                                "ESprom.Taurus.Roles.NetCenter.Persons.Person,"
                                                                "ESprom.Taurus.NetCenter.Common.Persons]], "
                                                                "ESprom.Taurus.NetCenter.Common",
                                                       "target": _dto.dict(exclude_none=True,
                                                                                 exclude={"personal_info"}),
                                                   }
                                               ]
                                           },
                                           "id": 0
                                       }})
        response = await self._get_response_info(RequestName.CREATE_PERSON)
        # if personal_info:
        #     personal_info.personId = response.get("body").get("tempToFinallyIdMap").get("0")
        #     await self.update_personal_info(personal_info)
        return await self.get_person(person_id=response.get("body").get("tempToFinallyIdMap").get("0"))

    async def update_person(self, dto: BastionWebSocketPersonDto.Update):
        find_person_response = await self._find_person(name=dto.name, first_name=dto.firstName,
                                                       second_name=dto.secondName)
        if find_person_response.get("body"):
            if dto.name == find_person_response.get("body").get("name") and (dto.firstName == find_person_response.get(
                    "body").get("firstName") and dto.secondName == find_person_response.get("body").get("secondName")):
                raise BastionIntegrationError("Персона уже существует")

        if (await self.get_person(person_id=dto.id)).get("person_id"):
            await self._send_message(data={"request_name": RequestName.UPDATE_PERSON.name,
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
                                                                    "ESprom.Taurus.Roles.NetCenter.Persons.Person,"
                                                                    "ESprom.Taurus.NetCenter.Common.Persons]], "
                                                                    "ESprom.Taurus.NetCenter.Common",
                                                           "target": dto.dict(exclude_none=True)
                                                       }
                                                   ]
                                               },
                                               "id": 0
                                           }})
            return await self._get_response_info(RequestName.UPDATE_PERSON)

    async def delete_person(self, person_id):
        await self._send_message(data={"request_name": RequestName.DELETE_PERSON.name,
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
                                                                "ESprom.Taurus.Roles.NetCenter.Persons.Person,"
                                                                "ESprom.Taurus.NetCenter.Common.Persons]], "
                                                                "ESprom.Taurus.NetCenter.Common",
                                                       "target": {
                                                           "id": person_id
                                                       }
                                                   }
                                               ]
                                           },
                                           "id": 0
                                       }})

        return await self._get_response_info(RequestName.DELETE_PERSON)

    async def find_person(self, dto: BastionWebSocketPersonDto.Get):
        request = {"$type": "ESprom.Taurus.Roles.NetCenter.Persons.FindPersonRequest, "
                            "ESprom.Taurus.NetCenter.Common.Persons",
                   "id": 0}
        request.update(dto.dict(exclude_none=True))
        await self._send_message(data={"request_name": RequestName.FIND_PERSON.name,
                                       "$type": REQUEST_COMMAND,
                                       "request": request})
        response = await self._get_response_info(RequestName.FIND_PERSON)
        info = response.get("body")
        return {"id": info.get("id"),
                "name": info.get("name"),
                "firstName": info.get("firstName"),
                "secondName": info.get("secondName"),
                "depart_id": info.get("organizationNodeId"),
                "create_date": info.get("createDate")}

    async def get_card_ident(self, card_code: int):
        await self._send_message(data={"$type": REQUEST_COMMAND,
                                       "request": {
                                           "$type": "ESprom.Taurus.Roles.NetCenter.Persons.CardByCodeRequest, "
                                                    "ESprom.Taurus.NetCenter.Common.Persons",
                                           "cardCode": card_code,
                                           "id": 0}})

    async def get_org_settings_for_pass(self, org_id):
        await self._send_message(data={"$type": REQUEST_COMMAND,
                                       "request": {
                                           "$type": "ESprom.Taurus.Roles.NetCenter.Persons"
                                                    ".PassCategoryOrganizationSettingsRequest,"
                                                    "ESprom.Taurus.NetCenter.Common.Persons",
                                           "categoryId": 1,
                                           "organizationNodeId": org_id,
                                           "id": 0}})

    async def update_personal_info(self, dto: PersonalInfo):
        await self._send_message(data={"request_name": RequestName.UPDATE_PERSONAL_INFO.name,
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
                                                                "ESprom.Taurus.Roles.NetCenter.Persons.PersonalInfo,"
                                                                "ESprom.Taurus.NetCenter.Common.Persons]], "
                                                                "ESprom.Taurus.NetCenter.Common",
                                                       "target": dto.dict(exclude_none=True)
                                                   }
                                               ]
                                           },
                                           "id": 0
                                       }})
        return await self._get_response_info(RequestName.UPDATE_PERSONAL_INFO)

    async def create_pass(self, _dto: PersonDto.Create):
        if not _dto.rfid:
            raise Exception("RFID not found")
        if type(_dto.rfid) == str:
            _dto.rfid = _dto.rfid.rjust(12, '0')
        else:
            _dto.rfid = _dto.rfid

        find_person_dto = BastionWebSocketPersonDto.Get(name=_dto.last_name, firstName=_dto.first_name,
                                                        secondName=_dto.middle_name)

        if not (person := await self.find_person(find_person_dto)):
            raise BastionIntegrationError("Person not found")

        dto = PassDto.Create(passCategoryId=1,
                             accessLevelId=1,
                             personId=person.get("id"),
                             priority=1)
        categories_ids = []
        pass_categories = await self.get_pass_category()
        for category in pass_categories:
            categories_ids.append(category.get("id"))

        if dto.passCategoryId not in categories_ids:
            raise BastionIntegrationError("Pass category not found")

        access_levels_ids = []
        access_levels = await self.get_access_level_info()
        for level in access_levels:
            access_levels_ids.append(level.get("id"))

        if dto.accessLevelId not in categories_ids:
            raise BastionIntegrationError("Access level not found")

        await self._send_message(data=self.command.create_pass(dto))

        pass_info = await self._get_response_info(RequestName.CREATE_PASS)
        _pass_info = {"pass_id": pass_info.get("body").get("tempToFinallyIdMap").get("0")}
        card_info = await self.create_card(card_code=_dto.rfid)
        await self.issue_card(pass_id=pass_info.get("body").get("tempToFinallyIdMap").get("0"),
                              card_id=card_info.get("card_id"), )
        return _pass_info

    async def create_card(self, card_code: str):
        await self._send_message(data=self.command.create_card(card_code))
        card_info = await self._get_response_info(RequestName.CREATE_CARD)
        return {"card_id": card_info.get("body").get("tempToFinallyIdMap").get("0")}

    async def issue_card(self, pass_id: int, card_id: int):
        await self._send_message(data=self.command.issue_pass(pass_id, card_id))
        return await self._get_response_info(RequestName.ISSUE_PASS)

    async def set_pin_code(self, pass_id: int, pin_code: str):
        await self._send_message(data=self.command.set_pin_code(pass_id, pin_code))
        return await self._get_response_info(RequestName.SET_PIN_CODE)

    async def get_card_info(self, card_id: int):
        await self._send_message(data={
            "$type": "ESprom.Taurus.Protocol.RequestCommand, ESprom.Taurus.Platform",
            "request": {
                "$type": "ESprom.Taurus.Roles.NetCenter.Persons.CardRequest, ESprom.Taurus.NetCenter.Common.Persons",
                "cardId": card_id,
                "id": 0
            }})
