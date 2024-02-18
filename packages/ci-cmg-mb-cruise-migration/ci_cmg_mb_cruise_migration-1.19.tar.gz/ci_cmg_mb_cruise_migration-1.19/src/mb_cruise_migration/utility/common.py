import datetime

from mb_cruise_migration.framework.consts.date_consts import ORACLE_DATE_FORMAT


def dict_value_or_none(dictionary, key):
    return dictionary[key] if key in dictionary else None


def multiple_values_in_survey_instrument(survey_instrument) -> bool:
    instruments = survey_instrument.split(";")
    return len(instruments) != 1


def strip_none(may_have_nones: list):
    return [item for item in may_have_nones if item is not None]


def strip_special_chars(string: str):
    return ''.join(char for char in string if char.isalnum())


def standardize_date_format_string(date_field_value, date_field_name, date_format_out):
    if date_field_value is None:
        return ""

    date_field_type = type(date_field_value)

    if date_field_type == str:
        try:
            date = datetime.datetime.strptime(date_field_value, ORACLE_DATE_FORMAT)
        except ValueError:
            raise ValueError("Date " + date_field_value + " did not match expected format " + ORACLE_DATE_FORMAT + " for field " + date_field_name)
            # try:
            #   date = datetime.datetime.fromisoformat(date_field_value)
            # except ValueError:
            #   raise ValueError("Date " + date_field_value + " did not match expected format " + ORACLE_DATE_FORMAT + " for field " + date_field_name)

        return date.strftime(date_format_out).upper()

    if date_field_type == datetime or date_field_type == datetime.datetime:
        return date_field_value.strftime(date_format_out)

    raise ValueError("date field " + date_field_name + " contained unsupported type: " + str(type(date_field_value)))


def oracle_date_format(date_field_value, date_field_name):
    return standardize_date_format_string(date_field_value, date_field_name, ORACLE_DATE_FORMAT)
