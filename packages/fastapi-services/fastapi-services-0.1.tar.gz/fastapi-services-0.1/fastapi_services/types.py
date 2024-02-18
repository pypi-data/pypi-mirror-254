from abc import abstractmethod, ABC


class Service(ABC):
    def __init__(self, service_type: type, implementation: type, **kwargs):
        self._service_type = service_type
        self._impl = implementation
        self._kw = kwargs

    @abstractmethod
    def invoke(self):
        pass


class IServiceCollection(ABC):
    def __init__(self):
        self._services: dict[type, Service] = {}

    @abstractmethod
    def add_transient(self, service_type: type, implementation_type: type, **kwargs):
        pass

    @abstractmethod
    def add_scoped(self, service_type: type, implementation_type: type, **kwargs):
        pass

    @abstractmethod
    def add_singleton(self, service_type: type, implementation_type: type, **kwargs):
        pass

    @abstractmethod
    def try_add_transient(self, service_type: type, implementation_type: type, **kwargs):
        pass

    @abstractmethod
    def try_add_scoped(self, service_type: type, implementation_type: type, **kwargs):
        pass

    @abstractmethod
    def try_add_singleton(self, service_type: type, implementation_type: type, **kwargs):
        pass

    @abstractmethod
    def get_service(self, service_type: type):
        pass

    @abstractmethod
    def get_required_service(self, service_type: type):
        pass

    def __getitem__(self, service_type: type):
        return self.get_required_service(service_type)
