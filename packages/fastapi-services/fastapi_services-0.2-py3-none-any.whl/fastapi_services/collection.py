from typing import Optional, Callable

from fastapi_services.services import ServiceLifetime
from .descriptor import ServiceDescriptor
from .exc import ArgumentNullException, ServiceIsNotRegistered
from .factory import proxy
from .interfaces import IServiceCollection, IServiceProvider
from .types import TService, TImplementation

__all__ = ['ServiceCollection']


class ServiceCollection(IServiceCollection, IServiceProvider):

    def _add(
            self,
            service_type: type[TService],
            implementation_type: type[TImplementation],
            lifetime: ServiceLifetime,
            implementation_factory: Optional[Callable[[IServiceProvider], TImplementation]] = None,
            **kwargs
    ):
        if not service_type:
            raise ArgumentNullException('service_type')

        self[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation_type=implementation_type,
            lifetime=lifetime,
            implementation_factory=implementation_factory,
            **kwargs)

    def _get(self, service_type: type[TService]):
        if not service_type:
            raise ArgumentNullException('service_type')

        for k in self.keys():
            if k.__name__ == service_type.__name__:
                return self.get(k)

    def _remove(self, service_type: type[TService]):
        if not service_type:
            raise ArgumentNullException('service_type')

        del self[service_type]

    def add_scoped(
            self,
            service_type: type[TService],
            implementation_type: Optional[type[TImplementation]] = None,
            implementation_factory: Optional[Callable[[IServiceProvider], TImplementation]] = None,
            **parameters
    ):
        self._add(service_type=service_type,
                  implementation_type=implementation_type or service_type,
                  lifetime=ServiceLifetime.Scoped,
                  implementation_factory=implementation_factory,
                  **parameters)

    def add_singleton(
            self,
            service_type: type[TService],
            implementation_type: Optional[type[TImplementation]] = None,
            implementation_factory: Optional[Callable[[IServiceProvider], TImplementation]] = None,
            **parameters
    ):
        self._add(service_type=service_type,
                  implementation_type=implementation_type or service_type,
                  lifetime=ServiceLifetime.Singleton,
                  implementation_factory=implementation_factory,
                  **parameters)

    def get_service(self, service_type: type[TService]) -> Optional[ServiceDescriptor]:
        if descriptor := self._get(service_type):
            return descriptor

    def get_required_service(self, service_type: type[TService]) -> ServiceDescriptor:
        if descriptor := self.get_service(service_type):
            return descriptor

        raise ServiceIsNotRegistered(service_type.__name__)

    def mount(self, app):
        proxy.provider = self
        app.dependency_overrides.update({k: proxy(v) for k, v in self.items()})

    def remove(self, service_type: type[TService]):
        if not self._get(service_type):
            raise ServiceIsNotRegistered(service_type.__name__)

        self._remove(service_type)

    def try_add_scoped(
            self,
            service_type: type[TService],
            implementation_type: Optional[type[TImplementation]] = None,
            implementation_factory: Optional[Callable[[IServiceProvider], TImplementation]] = None,
            **parameters
    ):
        if not self._get(service_type):
            self.add_scoped(service_type=service_type,
                            implementation_type=implementation_type,
                            implementation_factory=implementation_factory,
                            **parameters)

    def try_add_singleton(
            self,
            service_type: type[TService],
            implementation_type: Optional[type[TImplementation]] = None,
            implementation_factory: Optional[Callable[[IServiceProvider], TImplementation]] = None,
            **parameters
    ):
        if not self._get(service_type):
            self.add_singleton(service_type=service_type,
                               implementation_type=implementation_type,
                               implementation_factory=implementation_factory,
                               **parameters)

    def try_remove(self, service_type: type[TService]):
        if self._get(service_type):
            self._remove(service_type)
