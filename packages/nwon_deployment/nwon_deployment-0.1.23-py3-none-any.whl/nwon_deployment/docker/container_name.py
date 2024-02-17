from enum import Enum


def container_name(stack_name: str, service: Enum, counter: int = 1):
    return "-".join([stack_name, service.value, str(counter)])
