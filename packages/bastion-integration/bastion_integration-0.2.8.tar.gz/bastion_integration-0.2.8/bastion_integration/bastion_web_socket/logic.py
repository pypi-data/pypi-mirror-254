from loguru import logger

from bastion_integration.base_info.bastion_dto import PersonDto, BastionConfigDto
from bastion_integration.bastion_web_socket.core import CoreWebSocket
from bastion_integration.bastion_web_socket.response_dto import PersonResponseDto


def wrap_logger(func):
    async def wrapper(*args, **kwargs):
        response = await func(*args, **kwargs)
        logger.debug(f"\n{func.__name__}--Result: {response}")
        return response

    return wrapper


class CoreWebAsync:

    def __init__(self, config: BastionConfigDto):
        self.core = CoreWebSocket(config)

    async def init(self):
        await self.core.init()

    # =============================================================================================

    async def _check_connection(self, only_ping: bool = True, **kwargs):
        return await self.core._check_connection(only_ping=only_ping, **kwargs)

    async def _reconnect(self):
        pass

    # =============================================================================================

    async def get_organizations(self, organization_name: str = None):
        return await self.core.get_organization(organization_name=organization_name)

    async def create_organization(self, organization_name: str):
        return await self.core.create_organization(organization_name)

    async def update_organization(self, old_name: str, new_name: str):
        return await self.core.update_organization(old_name, new_name)

    async def delete_organization(self, organization_name: str):
        return await self.core.delete_organization(organization_name)

    # =============================================================================================

    async def get_departments(self, department_name: str = None):
        return await self.core.get_department(department_name)

    async def create_department(self, department_name: str, organization_name: str):
        return await self.core.create_department(department_name, organization_name)

    async def update_department(self, old_name: str, new_name: str, organization_name: str,
                                new_organization_name: str = None):
        return await self.core.update_department(old_name, new_name, organization_name, new_organization_name)

    async def delete_department(self, department_name: str, organization_name: str):
        return await self.core.delete_department(department_name, organization_name)

    # =============================================================================================
    async def create_person(self, dto: PersonDto.Create):
        return await self.core.create_person(dto)

    async def create_pass(self, dto: PersonDto.Create):
        return await self.core.create_pass(dto)


    # =============================================================================================

    async def get_operator_info(self, operator_id: int):
        return await self.core.get_operator_info(operator_id)

    async def get_pass_category(self):
        return await self.core.get_pass_category()

    async def get_rights_for_person(self):
        return await self.core.get_rights_for_person()

    async def get_dict_info(self, dict_category_id: int = None):
        return await self.core.get_dict_info(dict_category_id)

    async def get_access_levels(self, access_level_id: int = None):
        return await self.core.get_access_level_info(access_level_id)

    async def get_time_block(self, time_block_id: int = None):
        return await self.core.get_time_block(time_block_id)

    # =============================================================================================

    async def get_person(self, person_id: int) -> PersonResponseDto:
        return await self.core.get_person(person_id)

    #
    # async def update_person(self, dto: PersonDto.Update):
    #     return await self.core.update_person(dto)
    #
    #
    # async def delete_person(self, person_id: int):
    #     return await self.core.delete_person(person_id)
