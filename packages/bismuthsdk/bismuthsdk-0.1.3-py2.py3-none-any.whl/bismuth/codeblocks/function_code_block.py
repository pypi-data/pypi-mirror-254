from .base_code_block import BaseCodeBlock
from typing import Callable, Any


class FunctionCodeBlock(BaseCodeBlock):
    def __init__(self, func: Callable[[Any], Any], network_enabled: bool = False):
        self.network_enabled = network_enabled
        self.func = func

        super()

    def exec(self):
        self.func()
