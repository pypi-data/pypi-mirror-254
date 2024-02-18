from utype.parser.base import BaseParser
from utype.parser.field import ParserField
from utype.utils.datastructures import unprovided
from utype import Field
from typing import List, Union, Type
from utilmeta.utils import awaitable
import inspect
from functools import partial


class ParserProperty:
    def __init__(self, prop: Union[Type['Property'], 'Property'], field: ParserField):
        self.prop = prop
        self.field = field
        self.get = partial(self.prop.getter, field=self.field)
        self.set = partial(self.prop.setter, field=self.field)
        self.delete = partial(self.prop.deleter, field=self.field)

    # @property
    # def get(self):
    #     return partial(self.prop.getter, field=self.field)
    #
    # @property
    # def set(self):
    #     return partial(self.prop.setter, field=self.field)
    #
    # @property
    # def delete(self):
    #     return partial(self.prop.deleter, field=self.field)


class Property(Field):
    __instance_cls__ = ParserProperty
    __in__ = None
    __key__ = None
    __type__ = None
    __ident__ = None
    __private__ = False
    __no_default__ = None

    @classmethod
    def getter(cls, obj, field: ParserField = None):
        return obj

    @classmethod
    def setter(cls, obj, value, field: ParserField = None):
        return

    @classmethod
    def deleter(cls, obj, field: ParserField = None):
        return

    def init(self, field: ParserField):
        return self.__instance_cls__(self, field)


class DuplicateContextProperty(ValueError):
    def __init__(self, msg='', ident: str = None):
        super().__init__(msg)
        self.ident = ident


class ContextWrapper:
    """
    A universal context parser, often used to process Request context
    """
    context_cls = object
    default_property = None

    def __init__(self, parser: BaseParser, excluded_names: List[str] = None):
        properties = {}
        ident_props = {}
        for key, val in parser.fields.items():
            if excluded_names and key in excluded_names:
                continue
            if isinstance(val.field, Property):
                prop = val.field
            elif self.default_property:
                # fallback to default
                prop = self.default_property()
            else:
                continue
            if prop.__ident__:
                if prop.__ident__ in ident_props:
                    raise DuplicateContextProperty(ident=prop.__ident__)
                ident_props[prop.__ident__] = prop
            properties[key] = self.init_prop(prop, val)
        self.properties = properties
        self.parser = parser

    def init_prop(self, prop, val):    # noqa, to be inherit
        return prop.init(val)

    def parse_context(self, context: object) -> dict:
        if not isinstance(context, self.context_cls):
            # should raise TypeError
            pass
        params = {}
        for key, prop in self.properties.items():
            value = prop.get(context)
            if not unprovided(value):
                params[key] = value
        return params

    @awaitable(parse_context)
    async def parse_context(self, context: object) -> dict:
        if not isinstance(context, self.context_cls):
            # should raise TypeError
            pass
        params = {}
        for key, prop in self.properties.items():
            value = prop.get(context)
            if inspect.isawaitable(value):
                value = await value
            if not unprovided(value):
                params[key] = value
        return params
