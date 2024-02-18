from datetime import datetime

import loguru

from bastion_integration.base_info.bastion_dto import PersonDto, BastionConfigDto
from bastion_integration.base_info.custom_error_handler import BastionIntegrationError
from bastion_integration.bastion_iks.bastion_iks_dto import TimeIntervalDto, BastionIKSPersonDto, PassInDto
from bastion_integration.bastion_iks.core import CoreIKS


class CoreIKSAsync:

    def __init__(self, config: BastionConfigDto):
        self.config = config
        self.core = CoreIKS(self.config)

    async def init(self):
        self.core.login(user_name=self.config.operator_info.login, password=self.config.operator_info.password)
        self.core.check_connection()
        self.core.get_servers()
        self.core.get_version()

    # =============================================================================================
    async def _check_connection(self, only_ping: bool = True, **kwargs):
        return self.core.check_connection(only_ping=only_ping, **kwargs)

    # async def _reconnect(self):
    #     pass

    # =============================================================================================
    async def get_organizations(self, organization_name: str = None):
        return self.core.get_organizations(organization_name=organization_name)

    async def create_organization(self, organization_name: str):
        return self.core.create_organization(organization_name)

    async def update_organization(self, old_name: str, new_name: str):
        return self.core.update_organization(old_name, new_name)

    async def delete_organization(self, organization_name: str):
        return self.core.delete_organization(organization_name=organization_name)

    # =============================================================================================
    async def get_departments(self, department_name: str = None):
        return self.core.get_departments(department_name=department_name)

    async def create_department(self, department_name: str, organization_name: str):
        return self.core.create_department(department_name, organization_name)

    async def update_department(self, old_name: str, new_name: str, organization_name: str,
                                new_organization_name: str = None):
        return self.core.update_department(old_name, new_name, organization_name, new_organization_name)

    async def delete_department(self, department_name: str, organization_name: str):
        return self.core.delete_department(department_name, organization_name)

    # =============================================================================================
    async def create_person(self, dto: PersonDto.Create):
        try:
            access_levels = self.core.get_access_levels()
            loguru.logger.debug(access_levels)
            access_level = [level for level in access_levels if level.get("id") == dto.access_level_id]
            if not access_level:
                raise BastionIntegrationError("Access level not found")
            time_interval = TimeIntervalDto(timeStart="12:12:12",
                                            timeEnd="12:12:12",  # TODO set timezone in config
                                            inSaturday=1,
                                            inSunday=1,
                                            inHolidays=1)

            person_info = BastionIKSPersonDto(name=dto.last_name,
                                              firstName=dto.first_name,
                                              secondName=dto.middle_name,
                                              org=dto.organization_name,
                                              dep=dto.department_name,
                                              post=dto.job_title,
                                              birthDate=dto.date_of_birth,
                                              docIssueOrgan=dto.doc_issue_organ,
                                              docSer=dto.doc_series,
                                              docNo=dto.doc_number,
                                              birthPlace=dto.birth_place,
                                              phone=dto.phone)
            pass_dto = PassInDto(
                personData=person_info,
                passType="2",
                cardStatus=0,
                timeInterval=time_interval,
                passCat=dto.pass_category,
                createDate=datetime.now().strftime("%Y-%m-%d"),
                accessLevels=access_level

            )
            loguru.logger.warning(pass_dto)
            return self.core.create_person(pass_dto, use_access_levels=True)
        except Exception as e:
            raise BastionIntegrationError(f"Error creating person: {e}")

    # =============================================================================================
    async def create_pass(self, dto: PersonDto.Create):
        if not dto.rfid:
            raise Exception("RFID not found")
        if type(dto.rfid) == str:
            dto.rfid = dto.rfid.rjust(12, '0')
        else:
            dto.rfid = dto.rfid
        try:
            access_levels = self.core.get_access_levels()
            access_level = [level for level in access_levels if level.get("id") == dto.access_level_id]
            if not access_level:
                raise Exception("Access level not found")

            time_interval = TimeIntervalDto(timeStart="12:12:12",
                                            timeEnd="12:12:12",
                                            inSaturday=1,
                                            inSunday=1,
                                            inHolidays=1)

            person_info = BastionIKSPersonDto(name=dto.last_name,
                                              firstName=dto.first_name,
                                              secondName=dto.middle_name,
                                              org=dto.organization_name,
                                              dep=dto.department_name,
                                              post=dto.job_title,
                                              birthDate=dto.date_of_birth,
                                              docIssueOrgan=dto.doc_issue_organ,
                                              docSer=dto.doc_series,
                                              docNo=dto.doc_number,
                                              birthPlace=dto.birth_place,
                                              phone=dto.phone)
            pass_dto = PassInDto(
                cardCode=dto.rfid,
                personData=person_info,
                passType="2",
                cardStatus=0,
                timeInterval=time_interval,
                passCat=dto.pass_category,
                createDate=datetime.now().strftime("%Y-%m-%d"),
                issueDate=dto.visit_start_date,
                dateFrom=dto.visit_start_date,
                dateTo=dto.visit_end_date,
                accessLevels=access_level

            )

            return self.core.create_person(pass_dto, use_access_levels=True)
        except Exception as e:
            raise BastionIntegrationError(f"Error creating pass: {e}")
