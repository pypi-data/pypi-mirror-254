import time
from typing import List

import loguru
import requests
from loguru import logger
from pydantic import BaseModel
from requests.cookies import RequestsCookieJar

from bastion_integration.base_info.bastion_dto import BastionConfigDto

#  Базовый класс, написанный для Бастиона-икс 2 версии. Работает на 3 версии бастион-икс
from bastion_integration.base_info.custom_error_handler import BastionIntegrationError
from bastion_integration.bastion_iks.bastion_iks_dto import PassInDto, EntryPoint, AccessPoint


def _handle_response(response: requests.Response, dto=None):
    model_list = []
    if dto:
        for info in response:
            # logger.warning(info)
            if info is None:
                continue
            model_list.append(dto(**info))
        # logger.info(model_list)
        return model_list[0] if len(model_list) == 1 else model_list
    else:
        return response.text


class CoreIKS:
    code_for_url: str
    cookies = RequestsCookieJar
    _code_for_url = ""
    token: str = ""

    def __init__(self, config: BastionConfigDto):
        self.bastion_servers = ""
        self.config = config

    def init(self):
        self.login(user_name=self.config.operator_info.login, password=self.config.operator_info.password)
        self.check_connection()
        self.get_servers()
        self.get_version()

    def _url_build(self, route: str, params: dict = None) -> str:
        params_string = ""
        if params:
            for key, value in params.items():
                params_string = params_string + f"&{key}={value}"
        if not route.startswith("/"):
            route = "/" + route
        if self.config.server_config.https:
            url = f"https://{self.config.server_config.host}/api{route}?{self.bastion_servers}{params_string if params_string else ''}"
        else:
            url = f"http://{self.config.server_config.host}:{self.config.server_config.port}/api{route}?{self.bastion_servers}{params_string if params_string else ''}"
        return url

    # =============================================================================================
    def _send_request(self, method: str, route: str, dto: dict | BaseModel = None,
                      params: dict = None) -> requests.Response:
        response = None

        if not self.token:
            raise BastionIntegrationError("Not authenticated in Bastion IKS")

        session = requests.Session()
        session.cookies = self.cookies
        url = self._url_build(route, params)

        headers = {
            'Content-type': 'application/body+json',
            'Accept': 'application/body+json',
        }

        logger.debug(url)
        try:
            match method:
                case "GET":
                    response = session.get(url=url)
                case "POST":
                    response = session.post(url=url, json=dto if dto else {}, headers=headers)
                case "PATCH":
                    response = session.patch(url=url, json=dto if dto else {}, headers=headers)
                case "PUT":
                    response = session.put(url=url, json=dto if dto else {}, headers=headers)
                case "DELETE":
                    response = session.delete(url=url)

            if response.status_code != 200:
                raise BastionIntegrationError(
                    f"\nStatus code {response.status_code}\nReason: {response.reason}\n Headers: {response.headers}")
            return response
        except Exception as ex:
            logger.warning(f"\nBastion connection error: {ex}\n")
            session.close()
        # except CookieJar.extract_cookies as e:
        #     logger.warning(f"Bastion connection error: validation error: {e}\n")
        #     session.close()

    # =============================================================================================
    def login(self, user_name: str, password: str) -> None:
        session = requests.Session()
        try:
            url = f"http://{self.config.server_config.host}:{self.config.server_config.port}/api/Login"
            logger.info(url)
            response = session.post(url, json={"Opername": user_name,
                                               "Password": password})
            if response.status_code != 200:
                raise BastionIntegrationError(
                    f"\nStatus code {response.status_code}\nReason: {response.reason}\n Headers: {response.headers}")
            elif response.json() == "success":
                logger.info("Authorization success")
                self.token = response.cookies.values()
                self.cookies = session.cookies
                return True
            else:
                logger.error(
                    f"\nAuthorization failed with operator info:\n    Login: {self.config.operator_info.login},\n    Password: {self.config.operator_info.password}")
                session.close()
                return False
        except requests.exceptions.ConnectionError as ex:
            logger.error(f"Bastion connection error: validation error:\n {ex}")
            session.close()
            return False

    def logout(self):
        self._send_request("POST", "LogOff")

    # =============================================================================================
    def get_servers(self, servers: list = None):
        if not self.token:
            raise BastionIntegrationError("Not authenticated in Bastion IKS")
        session = requests.Session()
        session.cookies = self.cookies
        url = f"http://{self.config.server_config.host}:{self.config.server_config.port}/api/GetServers"
        self.bastion_servers = session.get(url).text
        new_serves = []
        if servers:
            for server in servers:
                if server in self.bastion_servers:
                    new_serves.append(server)
                else:
                    raise BastionIntegrationError(message=f"Server not found: {server}")
        else:
            new_serves = self.bastion_servers
        for server_code in [new_serves]:
            self._code_for_url = self._code_for_url + f"srvCode={server_code}&"

    # =============================================================================================
    def get_version(self):
        return self._send_request("GET", "GetVersion")

    def check_connection(self, only_ping: bool = True, **kwargs) -> bool:
        """
        kwargs:
            names are installed in a third-party program with which we integrate this library
        """
        session = requests.Session()
        if only_ping:
            check_host_and_port = session.get(
                url=f"http://{self.config.server_config.host}:{self.config.server_config.port}/api/CheckConnection")
            if check_host_and_port.status_code != 200:
                logger.critical(
                    f"Check host and port failed. Status code {check_host_and_port.status_code}\nReason: {check_host_and_port.reason}\n Headers: {check_host_and_port.headers}")
                return False
            else:
                return True
        else:
            host = kwargs.get("bastion_host") if kwargs.get("bastion_host") else self.config.server_config.host
            port = kwargs.get("bastion_port") if kwargs.get("bastion_port") else self.config.server_config.port

            login = kwargs.get("bastion_operator_login") if kwargs.get(
                "bastion_operator_login") else self.config.operator_info.login
            password = kwargs.get("bastion_operator_password") if kwargs.get(
                "bastion_operator_password") else self.config.operator_info.password

            bastion_servers = kwargs.get("bastion_server_for_iks") if kwargs.get(
                "bastion_server_for_iks") else self.bastion_servers

            session = requests.Session()
            check_host_and_port = session.get(url=f"http://{host}:{port}/api/CheckConnection")
            if check_host_and_port.status_code != 200:
                logger.critical(
                    f"Check host and port failed. Status code {check_host_and_port.status_code}\nReason: {check_host_and_port.reason}\n Headers: {check_host_and_port.headers}")
                return False
            else:
                self.config.server_config.host = host
                self.config.server_config.port = port

            check_operator_info = session.post(
                f"http://{self.config.server_config.host}:{self.config.server_config.port}/api/Login",
                json={"Opername": login,
                      "Password": password})
            if check_operator_info.status_code != 200:
                logger.critical(
                    f"\nOperator check failed. Status code {check_operator_info.status_code}\nReason: {check_operator_info.reason}\n Headers: {check_operator_info.headers}")
                return False

            elif check_operator_info.json() == "success":
                logger.info("Authorization success")
                self.token = check_operator_info.cookies.values()
                self.cookies = session.cookies

            self.get_servers(servers=bastion_servers)
            return True

    # =============================================================================================
    def get_organizations(self, organization_name: str = None):
        organization = (self._send_request("GET", "GetOrgs")).json()
        organization_names = [org.get("orgName") for org in organization]
        items = []
        if organization_name:
            if organization_name not in organization_names:
                return None
            departments = self._send_request("GET", "GetDeparts", params={"parentOrgName": organization_name}).json()
            items = {"organization_name": organization_name,
                     "departments_name": [model.get("depName") for model in departments]}
        else:
            departments = self._send_request("GET", "GetDeparts").json()
            organization_set = set(model.get("orgName") for model in departments)
            for organization_name in organization_set:
                departments_name = []
                for department_info in departments:
                    if department_info.get("orgName") == organization_name:
                        departments_name.append(department_info.get("depName"))
                items.append({"organization_name": organization_name, "departments": departments_name})
        return items

    def create_organization(self, organization_name):
        if self.get_organizations(organization_name):
            raise BastionIntegrationError(f"Organization with name {organization_name} already exists")
        _handle_response((self._send_request("PUT", "PutOrg", dto={"orgName": organization_name})))
        return self.get_organizations(organization_name)

    def update_organization(self, old_name: str, new_name: str):
        if self.get_organizations(new_name):
            raise BastionIntegrationError(f"Organization with name {new_name} already exists")
        if not self.get_organizations(old_name):
            raise BastionIntegrationError(f"Organization with name {old_name} not found")
        _handle_response(
            (self._send_request("POST", "UpdateOrg", dto={"orgName": old_name}, params={"orgNewName": new_name})))
        return self.get_organizations(new_name)

    def delete_organization(self, organization_name: str):
        if not (organization := self.get_organizations(organization_name)):
            raise BastionIntegrationError(f"Organization with name {organization_name} not found")
        _handle_response((self._send_request("POST", "DeleteOrg", dto={"orgName": organization_name})))
        return organization

    # =============================================================================================
    def get_departments(self, department_name: str = None):
        params = None
        departments_info = []
        departments = self._send_request("GET", "GetDeparts", params=params).json()
        if department_name:
            for depart in departments:
                if depart.get("depName") == department_name:
                    departments_info.append(
                        {"department_name": depart.get("depName"), "organizatioin": depart.get("orgName")})
            return departments_info
        resp = [{"department_name": depart.get("depName"), "organizatioin": depart.get("orgName")} for depart in
                departments]
        return resp

    def create_department(self, department_name: str, organization_name: str):
        if not self.get_organizations(organization_name):
            raise BastionIntegrationError(f"Organization with name {organization_name} not found")
        departments = self.get_departments(department_name)
        if departments:
            for depart in departments:
                if depart.get("department_name") == department_name and depart.get(
                        "organizatioin") == organization_name:
                    raise BastionIntegrationError(
                        f"Department with name {department_name} already exists in organization {organization_name}")
        self._send_request("PUT", "PutDepart", dto={
            "srvCode": "",
            "DepName": department_name,
            "OrgName": organization_name
        })
        return self.get_departments(department_name)

    def update_department(self, old_name: str, new_name: str, org_name: str, new_org_name: str = None):
        organizations = self.get_organizations()
        org_names = []
        for org in organizations:
            org_names.append(org.get("organization_name"))
            if org.get("organization_name") == org_name:
                if new_name and new_name in org.get("departments") and not new_org_name:
                    raise BastionIntegrationError(f"Department with name {new_name} already exists")
            if new_org_name and org.get("organization_name") == new_org_name:
                if new_name and new_name in org.get("departments"):
                    raise BastionIntegrationError(f"Department with name {new_name} already exists")

        if org_name not in org_names:
            raise BastionIntegrationError(f"Organization with name {org_name} not found")
        if new_org_name and new_org_name not in org_names:
            raise BastionIntegrationError(f"Organization with name {new_org_name} not found")

        self._send_request("POST", "UpdateDepart",
                           params={"departNewName": new_name} if new_name else None,
                           dto={"srvCode": "",
                                "DepName": old_name,
                                "OrgName": new_org_name if new_org_name else org_name})

        return self.get_departments(new_name)

    def delete_department(self, department_name: str, organization_name: str) -> str:
        if organization_name not in [org.get("organization_name") for org in self.get_organizations()]:
            raise BastionIntegrationError(f"Organization with name {organization_name} not found")

        if not (department := self.get_departments(department_name=department_name)):
            raise BastionIntegrationError(f"Department with name {department_name} not found")

        self._send_request("POST", "DeleteDepart", dto={"depName": department_name, "orgName": organization_name})
        return department

    # =============================================================================================

    def create_person(self, dto: PassInDto, use_access_levels: bool):
        # Усли не передавать код карты будет создана заявка на пропуск, то есть объект Person.
        # Если передавать код карты, то будет создан пропуск с кодом карты.
        logger.debug(f'create_pass: {dto.dict(exclude_none=True, exclude_defaults=True)}')
        response = _handle_response(self._send_request("PUT", "PutPass",
                                                       params={
                                                           "useAccessLevelsInsteadOfEntryPoints": use_access_levels},
                                                       dto=dto.dict(exclude_none=True, exclude_defaults=True)))
        logger.info(f'create_person: {response}')
        return response

    def create_pass(self, dto: PassInDto, use_access_levels: bool = True):
        logger.critical(f'create_pass: {dto.dict(exclude_none=True, exclude_defaults=True)}')
        response = _handle_response(self._send_request("PUT", "PutPass",
                                                       params={
                                                           "useAccessLevelsInsteadOfEntryPoints": use_access_levels},
                                                       dto=dto.dict(exclude_none=True, exclude_defaults=True)))
        logger.critical(f'create_pass: {response}')
        return response

    def update_pass(self, dto: PassInDto, use_access_levels: bool = False):
        if dto.EntryPoints or dto.AccessLevels:
            return _handle_response(self._send_request(method="PUT", route="PutPass", params={
                "useAccessLevelsInsteadOfEntryPoints": use_access_levels}, dto=dto.dict()))
        else:
            raise BastionIntegrationError(message="Method update_bastion_pass can be used with card code")

    def block_pass(self, card_code: str, comment: str) -> str:
        return _handle_response(
            (self._send_request("GET", "BlockPass", params={"cardCode": card_code, "blockReason": comment})))

    def unblock_pass(self, card_code: str) -> str:
        return _handle_response(
            (self._send_request("GET", "UnBlockPass", params={"cardCode": card_code})))

    def archive_pass(self, card_code: str):
        """Возможно убрать в архив только выданную карту"""
        return _handle_response(
            (self._send_request("GET", "ReturnPass", params={"cardCode": card_code})))

    # =============================================================================================
    def get_entry_points(self) -> EntryPoint:
        return _handle_response((self._send_request("GET", "GetEntryPoints")).json(), EntryPoint)

    def get_access_levels(self) -> List[dict]:
        response = self._send_request("GET", "GetAccessLevels")

        return response.json()

    def get_access_points(self):
        return _handle_response(self._send_request("GET", "GetAccessPoints").json(), AccessPoint)

    # =============================================================================================

    # def get_bastion_dict_values(self, category: int = "") -> DictValues:
    #     response = _handle_response((self._send_request("GET", "GetDictVals", params={"category": category})).json(),
    #                                 DictValues)
    #     logger.info(response)
    #     for model in response:
    #         logger.info(model.dict())
    #     return response
    #
    # def get_devices(self, dto: DeviceDto) -> DeviceOutDto:
    #     return _handle_response(self._send_request("GET", "GetDevices", params=dto.dict()).json(), DeviceOutDto)

    # def get_passes(self, dto: GetPassInDto) -> List[PassOutDto]:
    #     """Метод предоставляет возможность одним запросом получить пропуска
    #          только с одного конкретного сервера и требует обязательного указания параметра srvCode."""
    #
    #     if len([self.bastion_servers]) != 1:
    #         raise BastionIntegrationError(message="Method get_bastion_pass can be used only with one server")
    #     if not dto.srvCode:
    #         raise BastionIntegrationError(message="Method get_bastion_pass can be used with srvCode")
    #     if dto.card_code:
    #         return _handle_response(self._send_request("GET", "GetPassesByCardCode",
    #                                                    params={"srvCode": dto.srvCode,
    #                                                            "cardCode": dto.card_code,
    #                                                            "withoutPhoto": dto.withoutPhoto}).json(), PassOutDto)
    #     else:
    #         return _handle_response(self._send_request("GET", "GetPasses", params=dto.dict()).json(), PassOutDto)

    # def issue_pass(self, dto: PassDto.Issue):
    #     if dto.cardCode == "" or not dto.cardCode:
    #         raise BastionIntegrationError(message="Method issue_bastion_pass can be used with card code")
    #     return _handle_response(
    #         (self._send_request("GET", "IssuePass", params=dto.dict())))

    # def get_control_areas(self):
    #     return _handle_response(self._send_request("GET", "GetControlAreas").json(), ControlArea)

    # def get_card_events(self, dto: GetCardEvents) -> GetCardEvents:
    #     return _handle_response((self._send_request("GET", "GetCardEvents", params=dto.dict())).json(), OutCardEvents)
    #
    # def get_attendance(self, dto: Attendance) -> Attendance:
    #     return _handle_response(self._send_request("GET", "GetAttendance", params=dto.dict() if dto else {}).json(),
    #                             OutAttendance)
