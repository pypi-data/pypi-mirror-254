from dataclasses import dataclass
from typing import Optional, Union, List


@dataclass
class Query:
    """
    Класс, описывающий запросы, передаваемые конечной системе.

        ``command``: содержит командe, которую необходимо выполнить;
        ``timeout``: содержит время, отведенное на выпонение команды;
        ``expects``: содержит регулярные выражения, которые описывают
        ожидаемый ответ от конечной системы;
        ``sudo``: содержит пароль от супер пользователя или enable.
    """
    command: str
    timeout: int = None
    expects: Optional[Union[List[str], str]] = None
    sudo: Optional[str] = None