class ServiceIsNotRegistered(Exception):
    def __init__(self, service_name: str):
        self.service_name = service_name

    def __str__(self):
        return f"{self.service_name} is not registered."


class ArgumentNullException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name} is None."
