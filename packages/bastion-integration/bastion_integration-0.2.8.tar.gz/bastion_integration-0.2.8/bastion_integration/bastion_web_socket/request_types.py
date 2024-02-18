from enum import Enum


REQUEST_COMMAND = "ESprom.Taurus.Protocol.RequestCommand, ESprom.Taurus.Platform"


class RequestName(Enum):
    NET_CENTER_STATUS = "net_center_status"
    LOGIN = "login"
    HANDSHAKE = "handshake"

    GET_OPERATOR_INFO = "get_operator_info"
    GET_PASS_CATEGORY = "get_pass_category"
    GET_RIGHTS_FOR_PERSON = "get_rights_for_person"
    GET_ORGANIZATIONS_AND_DEPARTMENTS = "get_organizations_and_departments"
    GET_DICT_INFO = "get_dict_info"
    GET_DICT_INFO_ONE_CATEGORY = "get_dict_info_one_category"
    GET_ALL_ACCESS_LEVELS = "get_all_access_levels"
    GET_ONE_ACCESS_LEVEL = "get_one_access_level"
    GET_ALL_TIME_BLOCK = "get_all_time_block"
    GET_ONE_TIME_BLOCK = "get_one_time_block"

    GET_ORGANIZATIONS = "get_organizations"
    CREATE_ORGANIZATION = "create_organization"
    CREATE_DEPARTMENT = "create_department"

    UPDATE_ORGANIZATION = "update_organization"
    UPDATE_DEPARTMENT = "update_department"

    DELETE_ORGANIZATION = "delete_organization"
    DELETE_DEPARTMENT = "delete_department"

    GET_PERSONAL_INFO = "get_person"
    GET_PERSON_SHORT_INFO = "get_person_short_info"
    FIND_PERSON = "find_person"
    CREATE_PERSON = "create_person"
    UPDATE_PERSON = "update_person"
    DELETE_PERSON = "delete_person"

    UPDATE_PERSONAL_INFO = "update_personal_info"

    CREATE_PASS = "create_pass"
    CREATE_CARD = "create_card"

    ISSUE_PASS = "issue_pass"
    SET_PIN_CODE = "set_pin_code"
