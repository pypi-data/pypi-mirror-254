import socket

from nwon_deployment.print_output import OutputType, print_output


def port_is_available(port: int) -> bool:
    """
    We can only check ports until port number 65.535. Otherwise we get an out
    of rang error.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        available = sock.connect_ex(("localhost", port)) != 0
        print_output(f"Port {port} available: {available}", output=OutputType.Debug)
        return available


__all__ = ["port_is_available"]
