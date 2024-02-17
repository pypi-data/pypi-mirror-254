import sys
import json
import warnings
import pathlib
from marshmallow import Schema, exceptions
from ..exceptions import DataError, SOARException


warnings.filterwarnings("ignore")


class BaseFunction:
    """
    Является базовым классом для всех скриптов, участвующих в обогащении и реагировании.
    При использовании класса необходимо реализовать метод ``function``.
    Автоматически принимаемые значения:
        ``input_json``: Первым аргументом принимает информацию, переданную на вход плейбука;
        ``secrets``: Вторым аргументом приниает секреты.
        ``ensure_ascii``: Указывает, должны ли символы не из набора ASCII быть экранированы. По умолчанию False.
    """
    def __init__(self, inputs_model: Schema = None, secrets_model: Schema = None, ensure_ascii: bool = False) -> None:
        """
        Инициализирует экземпляр класса.

        Args:
            ``ensure_ascii (bool)``: Указывает, должны ли символы не из набора ASCII быть экранированы. По умолчанию False
            ``inputs_model (Schema)``: модель входных данных
            ``secrets_model (Schema)``: модель секретов
        Returns:
            ``None``
        """

        self.inputs_model = inputs_model
        self.secrets_model = secrets_model
        self.ensure_ascii = ensure_ascii
        self._input_json = {}
        self._secrets = {}

        inputs = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
        secrets = pathlib.Path(sys.argv[2]).read_text(encoding='utf-8')

        if self.inputs_model is not None:
            self._input_json: dict = self._check_input_data(self.inputs_model, inputs, obj="Input data")
        else:
            self._input_json: dict = json.loads(inputs)

        if self.secrets_model is not None:
            self._secrets: dict = self._check_input_data(self.secrets_model, secrets, obj="Secrets")
        else:
            self._secrets: dict = json.loads(secrets)

        try:
            self.input_json = self.validate_inputs(self._input_json)
            self.secrets = self.validate_secrets(self._secrets)
        except DataError as e:
            self.output(e.__str__(), e.return_code)
        except NotImplementedError:
            self.input_json = self._input_json
            self.secrets = self._secrets

        try:
            result, message = self.function()
        except SOARException as e:
            self.output(e.__str__(), e.return_code)
        else:
            self.output(message, **result)

    def _check_input_data(self, model: Schema, data: str, obj: str) -> dict:
        """
        Проверка входных данных
        """
        try:
            checked_data = model.loads(data)
            return checked_data
        except exceptions.ValidationError as e:
            if isinstance(e.messages, dict):
                self.output(f"{obj} validation error", 1, **{"fields": e.messages})
            else:
                self.output(f"{obj} validation error: {e.__str__()}", 1)

    def validate_inputs(self, input_json: dict) -> dict:
        """
        Метод для дополнительной валидации входных данных.

        При ошибке валидации выбрасывает ValidationError
        """
        raise NotImplementedError

    def validate_secrets(self, secrets: dict) -> dict:
        """
        Метод для дополнительной валидации секретов.

        При ошибке валидации выбрасывает ValidationError
        """
        raise NotImplementedError

    def function(self) -> (dict, str):
        """
        В этом методе необходимо реализовать функцию по обогащению
        или реагированию.

        Методу доступны переменные input_json и secrets.

        Для получения данных используйте переменные input_json и secrets класса BaseFunction.
        Для вывода ошибок необходимо использовать исключения из модуля exceptions.
        Returns:
            (dict, str): Результат обогащения или реагирования и сообщение о результате.
        """
        raise NotImplementedError('Метод function не реализован')

    def output(self,
               message: str,
               return_code: int = 0,
               **kwargs) -> None:
        """
        Выводит результат работы скрипта в формате JSON.

        Args:
            ``message (str)``: Сообщение о результате выполнения скрипта, которое будет выведено.
            ``return_code (int)``: Код возврата, указывающий на успешное выполнение (0) или ошибку (ненулевое значение).
            ``**kwargs``: Дополнительные именованные аргументы. Например, результат сбора данных.

        Returns:
            ``None``
        """
        # Обновляем входной JSON с результатом или сообщением об ошибке
        self._input_json['error' if return_code else 'result'] = message

        # Обновляем входной JSON новыми аргументами
        self._input_json.update(kwargs)

        # Выводим входной JSON в форматированном виде
        print(json.dumps(self._input_json, ensure_ascii=self.ensure_ascii))

        if self._input_json.get("result"):
            del self._input_json["result"]
        # Завершаем выполнение скрипта с кодом 0 в случае успешного выполнения или ненулевым в случае ошибки
        exit(return_code)
