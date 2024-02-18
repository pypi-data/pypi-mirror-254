from .base_code_block import BaseCodeBlock


class FunctionCodeBlock(BaseCodeBlock):
    def __init__(self, func: callable[any, any], network_enabled: bool = False):
        self.network_enabled = network_enabled
        self.func = func

        super()

    def exec(self):
        self.func()
