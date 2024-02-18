from fastapi_services.exc import InvalidOperationException
from fastapi_services.types import Service, IServiceCollection


class Transient(Service):
    def __init__(self, service_type: type, implementation: type, **kwargs):
        super().__init__(service_type, implementation, **kwargs)

    def invoke(self):
        pass


class Scoped(Service):
    def __init__(self, service_type: type, implementation: type, **kwargs):
        super().__init__(service_type, implementation, **kwargs)

    def invoke(self):
        return self._impl(**self._kw)


class Singleton(Service):
    def __init__(self, service_type: type, implementation: type, **kwargs):
        super().__init__(service_type, implementation, **kwargs)
        self._instance = None

    def invoke(self):
        if not self._instance:
            self._instance = self._impl(**self._kw)
        return self._instance


class ServiceCollection(IServiceCollection):
    def add_transient(self, service_type: type, implementation_type: type, **kwargs):
        self._services[service_type] = Transient(service_type, implementation_type, **kwargs)

    def add_scoped(self, service_type: type, implementation_type: type, **kwargs):
        self._services[service_type] = Scoped(service_type, implementation_type, **kwargs)

    def add_singleton(self, service_type: type, implementation_type: type, **kwargs):
        self._services[service_type] = Singleton(service_type, implementation_type, **kwargs)

    def try_add_transient(self, service_type: type, implementation_type: type, **kwargs):
        if self._services.get(service_type):
            return False
        self.add_transient(service_type, implementation_type, **kwargs)
        return True

    def try_add_scoped(self, service_type: type, implementation_type: type, **kwargs):
        if self._services.get(service_type):
            return False
        self.add_scoped(service_type, implementation_type, **kwargs)
        return True

    def try_add_singleton(self, service_type: type, implementation_type: type, **kwargs):
        if self._services.get(service_type):
            return False
        self.add_singleton(service_type, implementation_type, **kwargs)
        return True

    def get_service(self, service_type: type):
        if service := self._services.get(service_type):
            return service.invoke()

    def get_required_service(self, service_type: type):
        if service := self._services.get(service_type):
            return service.invoke()
        raise InvalidOperationException(f"No service registered: {service_type}.")

    def __getitem__(self, service_type):
        return self.get_required_service(service_type)

    def _check_types(self, serv, impl):
        return issubclass(impl, serv)
