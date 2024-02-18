import warnings


from typing import Callable
from utilmeta.utils import awaitable
from utype.utils.datastructures import unprovided
import inspect
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import Request


class RequestContextVar:
    def __init__(self, key: str, cached: bool = False, static: bool = False, default=None, factory: Callable = None):
        self.key = key
        self.default = default
        self.factory = factory
        self.cached = cached
        self.static = static

    def init(self, request: 'Request'):
        class c:
            @staticmethod
            def contains():
                return self.contains(request)

            @staticmethod
            def get():
                return self.get(request)

            @staticmethod
            @awaitable(get)
            async def get():
                return await self.get(request)

            @staticmethod
            def set(v):
                return self.set(request, value=v)
        return c

    def contains(self, request: 'Request'):
        return request.adaptor.in_context(self.key)

    def get(self, request: 'Request'):
        r = unprovided
        if self.contains(request):
            r = request.adaptor.get_context(self.key)
        else:
            if callable(self.factory):
                r = self.factory(request)
            if unprovided(r):
                if callable(self.default):
                    r = self.default()
                else:
                    r = self.default
        if self.cached:
            self.set(request, r)
        return r

    @awaitable(get)
    async def get(self, request: 'Request'):
        r = unprovided
        if self.contains(request):
            r = request.adaptor.get_context(self.key)
        else:
            if callable(self.factory):
                r = self.factory(request)
                if inspect.isawaitable(r):
                    r = await r
            if unprovided(r):
                if callable(self.default):
                    r = self.default()
                else:
                    r = self.default
            # else:
            #     raise KeyError(f'context: {repr(self.key)} missing')
        if self.cached:
            self.set(request, r)
        return r

    def set(self, request: 'Request', value):
        request.adaptor.update_context(**{self.key: value})

    def clear(self, request: 'Request'):
        request.adaptor.delete_context(self.key)

    def register_factory(self, func, force: bool = False):
        if self.factory:
            if self.factory != func:
                if force:
                    raise ValueError(f'factory conflicted: {func}, {self.factory}')
                else:
                    warnings.warn(f'factory conflicted: {func}, {self.factory}')
            return
        self.factory = func


# cached context var
user = RequestContextVar('_user', cached=True)
user_id = RequestContextVar('_user_id', cached=True)
scopes = RequestContextVar('_scopes', cached=True)
data = RequestContextVar('_data', cached=True)      # parsed str/dict data
# variable context var
time = RequestContextVar('_time', factory=lambda request: request.adaptor.time, static=True)
path_params = RequestContextVar('_path_params', default=dict)
allow_methods = RequestContextVar('_allow_methods', default=list)
allow_headers = RequestContextVar('_allow_headers', default=list)
unmatched_route = RequestContextVar('_unmatched_route', factory=lambda request: request.adaptor.route)
