from typing import Optional, Callable, Any

from fastapi_services.exc import ArgumentNullException
from fastapi_services.lifetime import ServiceLifetime
from fastapi_services.types import TService, TImplementation

__all__ = ['ServiceDescriptor']


class ServiceDescriptor:
    def __init__(
            self,
            service_type: type[TService],
            implementation_type: type[TImplementation],
            lifetime: ServiceLifetime,
            implementation_factory: Optional[Callable[..., TImplementation]] = None,
            **parameters
    ):
        """

        :param service_type:
        :param implementation_type:
        :param lifetime:
        :param implementation_factory:
        :param parameters:
        """
        if not service_type:
            raise ArgumentNullException('service_type')

        if not service_type:
            raise ArgumentNullException('implementation_type')

        self.service_type = service_type
        self._implementation_type = implementation_type
        self._lifetime = lifetime
        self._implementation_factory = implementation_factory
        self._implementation_parameters = parameters
        self._implementation_instance = None

    @property
    def implementation_factory(self) -> Optional[Callable[..., TImplementation]]:
        return self._implementation_factory

    @property
    def implementation_instance(self) -> TImplementation:
        return self._implementation_instance

    @property
    def implementation_type(self) -> type[TImplementation]:
        return self._implementation_type

    @property
    def lifetime(self) -> ServiceLifetime:
        return self._lifetime

    @property
    def parameters(self) -> dict[str, Any]:
        return self._implementation_parameters

    @staticmethod
    def Scoped(  # noqa: N802
            service_type: type[TService],
            implementation_type: type[TImplementation],
            implementation_factory: Optional[Callable[..., TImplementation]] = None,
            **kwargs
    ) -> 'ServiceDescriptor':
        """

        :param service_type:
        :param implementation_type:
        :param implementation_factory:
        :param kwargs:
        :return:
        """
        return ServiceDescriptor(
            service_type=service_type,
            implementation_type=implementation_type,
            lifetime=ServiceLifetime.Scoped,
            implementation_factory=implementation_factory,
            **kwargs)

    @staticmethod
    def Singleton(  # noqa: N802
            service_type: type[TService],
            implementation_type: type[TImplementation],
            implementation_factory: Optional[Callable[..., TImplementation]] = None,
            **kwargs
    ) -> 'ServiceDescriptor':
        """

        :param service_type:
        :param implementation_type:
        :param implementation_factory:
        :param kwargs:
        :return:
        """
        return ServiceDescriptor(
            service_type=service_type,
            implementation_type=implementation_type,
            lifetime=ServiceLifetime.Singleton,
            implementation_factory=implementation_factory,
            **kwargs)

    def __call__(self):
        factory = self.implementation_factory

        match self.lifetime:
            case ServiceLifetime.Scoped:
                return factory

            case ServiceLifetime.Singleton:
                if not self.implementation_instance:
                    setattr(self, '_implementation_instance', factory)
                return lambda: self.implementation_instance
