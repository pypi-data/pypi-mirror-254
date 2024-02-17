from typing import Any, Dict, List, Union


def replace_all(text: str, replace_dict: Dict[str, str]) -> str:
    '''
    Функция предназначена для замены множества значений в строке:

        ``text``: исходный текст, в котором необходимо сделать замены;

        ``replace_dict``: словарь, ключём которого является подстрока,
        которую надо заменить, а значением строка, на которую надо
        заменить.

    '''
    for i, j in replace_dict.items():
        text = text.replace(i, j)
    return text


def deep_get(
        obj: Union[dict, list],
        keys: List[Union[int, str]],
        default: Any = None
        ) -> Any:
    '''
    Функция предназначена для безопасного извлечения вложенного значения из объекта:

        ``obj``: объект, из которого необходимо извлечь значение;

        ``keys``: список ключей и индексов, по которым извлекаются вложенные объекты
        и значения;

        ``default``: значение, возвращаемое если не удалось извлечь искомое значений.
    '''
    for key in keys:
        if isinstance(obj, dict):
            obj = obj.get(key, default)
        elif isinstance(obj, list):
            try:
                obj = obj[key]
            except Exception:
                return default
        else:
            return default
    return obj
