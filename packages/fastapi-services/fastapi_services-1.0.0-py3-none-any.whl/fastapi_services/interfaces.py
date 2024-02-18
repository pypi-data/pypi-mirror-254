import abc
from typing import Optional, Dict, Callable, TYPE_CHECKING

from fastapi_services.types import TService, TImplementation

if TYPE_CHECKING:
    from .descriptor import ServiceDescriptor

__all__ = ['IServiceProvider', 'IServiceCollection']


class IServiceProvider(abc.ABC):
    @abc.abstractmethod
    def get_service(self, service_type: type[TService]) -> Optional['ServiceDescriptor']:
        """

        :param service_type:
        :return:
        :exception ArgumentNullException: if service_type is None.
        """

    @abc.abstractmethod
    def get_required_service(self, service_type: type[TService]) -> 'ServiceDescriptor':
        """

        :param service_type:
        :return:
        :exception ArgumentNullException: if service_type is None.
        :exception ServiceIsNotRegistered: if service is not registered.
        """


class IServiceCollection(Dict[type, 'ServiceDescriptor']):
    @abc.abstractmethod
    def add_scoped(
            self,
            service_type: type[TService],
            implementation_type: Optional[type[TImplementation]] = None,
            implementation_factory: Optional[Callable[[IServiceProvider], TImplementation]] = None,
            **parameters
    ):
        """

        :param service_type:
        :param implementation_type:
        :param implementation_factory:
        :param parameters:
        :return:
        :exception ArgumentNullException: if service_type is None.
        """

    @abc.abstractmethod
    def add_singleton(
            self,
            service_type: type[TService],
            implementation_type: Optional[type[TImplementation]] = None,
            implementation_factory: Optional[Callable[[IServiceProvider], TImplementation]] = None,
            **parameters
    ):
        """

        :param service_type:
        :param implementation_type:
        :param implementation_factory:
        :param parameters:
        :return:
        :exception ArgumentNullException: if service_type is None.
        """

    @abc.abstractmethod
    def mount(self, app):
        """

        :param app:
        :return:
        """

    @abc.abstractmethod
    def remove(self, service_type: type[TService]):
        """

        :param service_type:
        :return:
        :exception ArgumentNullException: if service_type is None.
        :exception ServiceIsNotRegistered: if service is not registered.
        """

    @abc.abstractmethod
    def try_add_scoped(
            self,
            service_type: type[TService],
            implementation_type: Optional[type[TImplementation]] = None,
            implementation_factory: Optional[Callable[[IServiceProvider], TImplementation]] = None,
            **parameters
    ):
        """

        :param service_type:
        :param implementation_type:
        :param implementation_factory:
        :param parameters:
        :return:
        :exception ArgumentNullException: if service_type is None.
        """

    @abc.abstractmethod
    def try_add_singleton(
            self,
            service_type: type[TService],
            implementation_type: Optional[type[TImplementation]] = None,
            implementation_factory: Optional[Callable[[IServiceProvider], TImplementation]] = None,
            **parameters
    ):
        """

        :param service_type:
        :param implementation_type:
        :param implementation_factory:
        :param parameters:
        :return:
        :exception ArgumentNullException: if service_type is None.
        """

    @abc.abstractmethod
    def try_remove(self, service_type: type[TService]):
        """

        :param service_type:
        :return:
        :exception ArgumentNullException: if service_type is None.
        :exception ServiceIsNotRegistered: if service is not registered.
        """
