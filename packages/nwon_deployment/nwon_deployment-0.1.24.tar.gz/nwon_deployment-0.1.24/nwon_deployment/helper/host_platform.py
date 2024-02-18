import platform


def host_platform():
    processor = platform.processor()
    return "linux/amd64" if processor == "arm" else processor
