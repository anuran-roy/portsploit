import os
from pathlib import Path

class GenerateData:
    def __init__(self):
        pass

    def generate_ips(
        self,
        start: str = "",
        end: str = "",
        constraints={
            "port": {"gt": None, "lt": None, "eq": None},
            "address": {"gt": None, "lt": None, "eq": None},
        },
    ):
        pass

    def generate_hosts(
        self,
        start: str = "",
        end: str = "",
        constraints={
            "names": {"regex": None},
        },
    ):
        pass