from dataclasses import dataclass
from typing import Optional


@dataclass
class Response:
    """
    Класс, описывающий ответ от конечной системы.

        ``result``: содержит исходный ответ от целевой системы;
        ``text``: содержится форматированный ответ от целевой системы;
        ``status``: содержится статус выполнения переданной команды.
    """
    result: str
    text: Optional[str] = None
    status: Optional[bool] = None