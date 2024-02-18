from datetime import datetime, timedelta

from bastion_integration.base_info.bastion_dto import BastionDepartmentDto, PersonDto
from faker import Faker

create_organization_name = "test_22_organization"
update_name_organization = "test_22_organization_update_1"

create_department_fake_dto = BastionDepartmentDto.Create(department_name="Test_department_16",
                                                         organization_name="test_1_organization_update")

fake = Faker()

person_fake_create_dto = PersonDto.Create(last_name=fake.last_name(),
                                          first_name=fake.first_name(),
                                          middle_name=fake.last_name(),
                                          organization_name="Jacobs Inc",
                                          department_name="Test_department_16",
                                          job_title="Test_job",
                                          date_of_birth=(datetime.now() - timedelta(weeks=1100)).strftime("%Y-%m-%d"),
                                          doc_issue_organ="Test_organ",
                                          doc_series="Test_ser",
                                          doc_number="Test_number",
                                          birth_place="Test_place",
                                          phone="Test_phone",
                                          access_level_id=1,
                                          pass_category="Посетители",
                                          address="Test_address",
                                          doc_issue_date=(datetime.now() - timedelta(weeks=600)).strftime(
                                              "%Y-%m-%d")
                                          )

person_info_for_issye_pass = person_fake_create_dto
person_info_for_issye_pass.rfid = "D3CDFFFC11"
# person_info_for_issye_pass.rfid = "123465646"
person_info_for_issye_pass.visit_start_date = "2024-02-12"
person_info_for_issye_pass.visit_end_date = "2024-02-14"
