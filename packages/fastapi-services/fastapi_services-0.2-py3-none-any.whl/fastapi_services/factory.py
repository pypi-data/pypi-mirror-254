import collections
import inspect
from types import GenericAlias
from typing import _GenericAlias, _SpecialGenericAlias, Generic, Union, ClassVar, get_origin  # noqa

from fastapi_services import IServiceProvider, ServiceDescriptor, ServiceLifetime

typingGenericAlias = (_GenericAlias, _SpecialGenericAlias, GenericAlias)

__all__ = ['proxy']


def _is_generic_type(tp):
    return (isinstance(tp, type) and issubclass(tp, Generic) or
            isinstance(tp, typingGenericAlias) and
            get_origin(tp) not in (Union, tuple, ClassVar, collections.abc.Callable))


def _get_origin_type(tp):
    if not _is_generic_type(tp):
        return tp

    if origin := get_origin(tp):
        return origin
    else:
        return tp


class proxy:
    provider: IServiceProvider

    def __init__(self, descriptor: ServiceDescriptor):
        self._descriptor = descriptor

    def __call__(self):
        factory = self._descriptor.implementation_factory or self._create_instance

        match self._descriptor.lifetime:
            case ServiceLifetime.Scoped:
                return factory(proxy.provider)

            case ServiceLifetime.Singleton:
                if not self._descriptor.implementation_instance:
                    setattr(self._descriptor, '_implementation_instance', factory(proxy.provider))

                return self._descriptor.implementation_instance

    def _create_instance(self, provider: IServiceProvider):
        origin = _get_origin_type(self._descriptor.implementation_type)
        params = {
            k: v for k, v in
            inspect.signature(origin.__init__).parameters.items() if
            k not in ('self', 'args', 'kwargs',)
        }
        params_values = {}

        for name, hint in params.items():
            if (
                    name not in self._descriptor.parameters and
                    hint.default in (inspect.Parameter.empty, None,)
            ):
                if _proxy := proxy(provider.get_required_service(hint.annotation)):
                    params_values.update({name: _proxy()})
            else:
                params_values.update({name: hint.default})

        return origin(**self._descriptor.parameters, **params_values)
