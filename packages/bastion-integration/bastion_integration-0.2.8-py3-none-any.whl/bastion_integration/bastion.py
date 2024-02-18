from typing import Type

from loguru import logger

from bastion_integration.base_info.bastion_dto import PersonDto, BastionConfigDto
from bastion_integration.bastion_iks.async_core import CoreIKSAsync
from bastion_integration.bastion_web_socket.logic import CoreWebAsync


def wrap_logger(func):
    async def wrapper(*args, **kwargs):
        response = await func(*args, **kwargs)
        logger.debug(f"\n{func.__name__}--Result: {response}")
        return response

    return wrapper


class Bastion:

    def __init__(self, core: Type[CoreIKSAsync] | Type[CoreWebAsync], config: BastionConfigDto):
        self.core = core(config=config)

    # =============================================================================================
    @wrap_logger
    async def init(self):
        await self.core.init()

    # =============================================================================================
    @wrap_logger
    async def _check_connection(self, only_ping: bool = True, **kwargs):
        return await self.core._check_connection(only_ping=only_ping, **kwargs)

    @wrap_logger
    async def _reconnect(self):
        await self.core._reconnect()

    # =============================================================================================
    @wrap_logger
    async def get_organizations(self, organization_name: str = None):
        return await self.core.get_organizations(organization_name)

    @wrap_logger
    async def create_organization(self, organization_name: str):
        return await self.core.create_organization(organization_name)

    @wrap_logger
    async def update_organization(self, old_name: str, new_name: str):
        return await self.core.update_organization(old_name=old_name, new_name=new_name)

    @wrap_logger
    async def delete_organization(self, organization_name: str):
        return await self.core.delete_organization(organization_name=organization_name)

    # =============================================================================================
    @wrap_logger
    async def get_departments(self, department_name: str = None):
        return await self.core.get_departments(department_name=department_name)

    @wrap_logger
    async def create_department(self, department_name: str, organization_name: str):
        return await self.core.create_department(department_name, organization_name)

    @wrap_logger
    async def update_department(self, old_name: str, new_name: str, organization_name: str, new_organization_name: str = None):
        return await self.core.update_department(old_name, new_name, organization_name, new_organization_name)

    @wrap_logger
    async def delete_department(self, department_name: str, organization_name: str):
        return await self.core.delete_department(department_name, organization_name)

    # =============================================================================================
    @wrap_logger
    async def create_person(self, dto: PersonDto.Create):
        return await self.core.create_person(dto)

    # =============================================================================================
    @wrap_logger
    async def create_pass(self, dto: PersonDto.Create):
    
        return await self.core.create_pass(dto)
