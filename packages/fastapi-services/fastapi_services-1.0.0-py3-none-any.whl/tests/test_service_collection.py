from typing import Generic, TypeVar
from unittest import TestCase

from fastapi_services import ServiceCollection, ServiceLifetime
from fastapi_services.factory import proxy

TUser = TypeVar('TUser')
TRole = TypeVar('TRole')


class User: pass  # noqa: E701


class Role: pass  # noqa: E701


class IUserStore(Generic[TUser]): pass  # noqa: E701


class UserManager(Generic[TUser]):
    def __init__(self, repository: IUserStore[TUser]):
        self.repository = repository


class IdentityStore(Generic[TUser, TRole]):
    pass


class Identity(Generic[TUser, TRole]):
    def __init__(self, identity: IdentityStore[TUser, TRole]):
        self.identity = identity


class TestServiceCollection(TestCase):
    def setUp(self):
        self.services = ServiceCollection()

    def test_add_scoped(self):
        self.services.add_scoped(UserManager)
        self.assertTrue(
            self.services.get(UserManager) and
            self.services[UserManager].lifetime == ServiceLifetime.Scoped and
            self.services[UserManager].implementation_type == UserManager
        )

    def test_add_singleton(self):
        self.services.add_singleton(UserManager)
        self.assertTrue(
            self.services.get(UserManager) and
            self.services[UserManager].lifetime == ServiceLifetime.Singleton and
            self.services[UserManager].implementation_type == UserManager
        )

    def test_add_scoped_with_params(self):
        self.services.add_scoped(UserManager, repository='REPOSITORY')
        self.assertTrue(
            self.services.get(UserManager) and
            self.services[UserManager]._implementation_parameters.get('repository') == 'REPOSITORY'
        )

    def test_add_singleton_with_params(self):
        self.services.add_singleton(UserManager, repository='REPOSITORY')
        self.assertTrue(
            self.services.get(UserManager) and
            self.services[UserManager]._implementation_parameters.get('repository') == 'REPOSITORY'
        )

    def test_remove(self):
        self.services.add_scoped(UserManager)
        self.services.remove(UserManager)
        self.assertTrue(len(self.services) == 0)

    def test_get_service_with_generic(self):
        self.services.add_scoped(IdentityStore[User, Role])
        self.services.add_scoped(Identity[User, Role])
        identity = self.services.get_service(Identity[User, Role])
        proxy.provider = self.services
        serv = proxy(identity)()
        pass
