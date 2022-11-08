from conftest import setup
import pytest


class Methods:
    @pytest.mark.usefixtures("setup")
    def __init__(self, setup):
        # self.driver=setup
        setup

