import asyncio
import time

import loguru

from bastion_integration.bastion import Bastion
from bastion_integration.base_info.bastion_dto import BastionConfigDto, BastionServerConfig, BastionOperatorInfo, \
    HandShakeConfig
from bastion_integration.base_info.fake_dto_info import create_organization_name, update_name_organization, \
    create_department_fake_dto, person_fake_create_dto, person_info_for_issye_pass
from bastion_integration.bastion_iks.async_core import CoreIKSAsync
from bastion_integration.bastion_web_socket.logic import CoreWebAsync


async def test_organizations(bastion: Bastion):
    await bastion.get_organizations()
    await bastion.create_organization(organization_name=create_organization_name)
    await bastion.get_organizations(organization_name=create_organization_name)
    await bastion.update_organization(old_name=create_organization_name, new_name=update_name_organization)
    await bastion.get_organizations(organization_name=update_name_organization)
    await bastion.delete_organization(organization_name=update_name_organization)
    await bastion.get_organizations(update_name_organization)


async def test_departments(bastion: Bastion):
    await bastion.get_departments()
    await bastion.create_department(department_name=create_department_fake_dto.department_name,
                                    organization_name=create_department_fake_dto.organization_name)
    await bastion.get_departments(department_name=create_department_fake_dto.department_name)
    await bastion.update_department(old_name=create_department_fake_dto.department_name,
                                    new_name=create_department_fake_dto.department_name,
                                    organization_name=create_department_fake_dto.organization_name,
                                    new_organization_name=create_department_fake_dto.organization_name)
    await bastion.get_departments(department_name=create_department_fake_dto.department_name)
    await bastion.delete_department(department_name=create_department_fake_dto.department_name,
                                    organization_name=create_department_fake_dto.organization_name)
    await bastion.get_departments(create_department_fake_dto.department_name)


async def create_pass(bastion: Bastion):
    await bastion.create_person(person_fake_create_dto)
    await bastion.create_pass(person_info_for_issye_pass)


async def bastion_v2_test():
    bastion_config_v2 = BastionConfigDto(server_config=BastionServerConfig(host="192.168.4.198", port=5005),
                                         operator_info=BastionOperatorInfo(login="q", password="q"), handshake=None)
    bastion = Bastion(CoreIKSAsync, bastion_config_v2)
    await bastion.init()
    await bastion._check_connection()
    await create_pass(bastion)



async def bastion_v3_test():
    bastion_config_v3 = BastionConfigDto(server_config=BastionServerConfig(host="192.168.3.188", port=8045),
                                         operator_info=BastionOperatorInfo(login="q", password="q"),
                                         handshake=HandShakeConfig(role_type="Bastion",
                                                                   host_name="EEJKEEHOME",
                                                                   socket_id=100))
    loguru.logger.warning(bastion_config_v3)
    bastion = Bastion(CoreWebAsync, bastion_config_v3)
    await bastion.init()
    await bastion._check_connection()
    await create_pass(bastion)



async def main():
    await bastion_v2_test()

    # time.sleep(3)
    # await bastion_v3_test()


if __name__ == "__main__":
    asyncio.run(main())


# pypi-AgEIcHlwaS5vcmcCJGRiN2EyOTY2LTAwNTMtNDA4YS1iNTMzLTAzMmNmYzdiMjVlMwACG1sxLFsiYmFzdGlvbi1pbnRlZ3JhdGlvbiJdXQACLFsyLFsiYzc1NTAxMWItNGEyMy00MGEyLTliNzItODkyMzdmMDI2OGJjIl1dAAAGIM1sGAV7sW9DEEjjijZ7T1_D0e052zS_AOivO0lETtXh