from typing import Callable, Any

Validator = Callable[[str], dict]
KeyGetter = Callable[[Any], str]
PayloadInjector = Callable[[dict], None]
