import re

from ussl.utils import replace_all


def format_output(meta_input_json: dict, input_json: dict) -> dict:
    '''
    Функция предназначена для форматирования строк вывода скрипта/плейбука

        ``meta_input_json``: словарь, содержащий информацию для преобразований;

        ``input_json``: словарь, в котором необходимо совершить преобразования.
    '''
    format_templates: dict = meta_input_json.get('__SOAR.format')
    # Проверка используется ли функция форматирования
    if all([
        format_templates,
        isinstance(format_templates, dict)
    ]):
        # Из каждого шаблона форматирования выделяются форматируемые переменные
        for format_template in format_templates:
            format_variables = re.findall(r'(?<={)(.*?)(?=})', str(format_templates[format_template]))
            if format_variables:
                # Выделяются только те переменные, которые есть в input_json
                format_variables = list(filter(lambda x: x in input_json, format_variables))
                # Выделяются значения переменных
                values = [input_json[i] for i in format_variables]
                # Формируется словарь замены для функции replace_all
                format_dict = dict(zip(['{%s}' % i for i in format_variables], values))
                format_result = replace_all(
                    format_templates[format_template],
                    format_dict)
            else:
                # Если переменных для замены не найдено, то возвращается исходная строка
                format_result = format_templates[format_template]
            # Отформатированная строка добавляется с заданным ключём в input_json
            input_json[format_template] = format_result

    return input_json


def _assign_keys(meta_input_json: dict, input_: dict, target_key: str) -> dict:
    '''
    Функция предназначена для изменения ключей в переданных в неё словарях

        ``meta_input_json``: принимает в себя словарь, содержащий информацию
        для преобразований;

        ``input_``: принимает словарь, в котором необходимо совершить преобразования;

        ``target_key``: принимает в себя строку-указатель на фильтр, по которому
        выделяются и заменяются ключи (secrets/input).
    '''
    replace_dict: dict = meta_input_json.get(f'__SOAR.{target_key}')
    # Проверка используется ли функция замены ключей
    if all([
        replace_dict,
        isinstance(replace_dict, dict),
    ]):
        # Выделение только тех ключей, которые есть в _input
        replacements_keys = [i for i in replace_dict if i in input_]
        # Замена старых ключей на новые
        for old_key in replacements_keys:
            input_[replace_dict[old_key]] = input_.pop(old_key)
    return input_


def assign_input(meta_input_json: dict, input_: dict) -> dict:
    '''
    Функция для замены ключей в input_json

        ``meta_input_json``: принимает в себя словарь, содержащий информацию
        для преобразований;

        ``input_``: принимает словарь, в котором необходимо совершить преобразования;
    '''
    return _assign_keys(meta_input_json, input_, 'input')


def assign_secrets(meta_input_json: dict, input_: dict) -> dict:
    '''
    Функция для замены ключей в secrets

        ``meta_input_json``: принимает в себя словарь, содержащий информацию
        для преобразований;

        ``input_``: принимает словарь, в котором необходимо совершить преобразования;
    '''
    return _assign_keys(meta_input_json, input_, 'secrets')
