from datetime import datetime
from decimal import Decimal
from typing import Union, TypeVar, Generic, Iterator, Optional, TypedDict
import peewee

CharField = Union[peewee.CharField, str]
DatetimeField = Union[peewee.DateTimeField, datetime]
TextField = Union[peewee.TextField, str]
IntegerField = Union[peewee.IntegerField, int]
BooleanField = Union[peewee.BooleanField, bool]
FloatField = Union[peewee.FloatField, float]
DoubleField = Union[peewee.DoubleField, float]
DateField = Union[peewee.DateField, str]
DateTimeField = Union[peewee.DateTimeField, str]
TimeField = Union[peewee.TimeField, str]
DecimalField = Union[peewee.DecimalField, Decimal]
PrimaryKeyField = Union[peewee.PrimaryKeyField, int]

T = TypeVar('T')


class ModelSelect(peewee.ModelSelect, Generic[T]):
    def __iter__(self) -> Iterator[T]:
        pass

    def where(self, *expressions) -> 'ModelSelect[T]':
        pass

    def limit(self, value: Optional[int] = None) -> 'ModelSelect[T]':
        pass

    def offset(self, value: Optional[int] = None) -> 'ModelSelect[T]':
        pass


class BackrefAccessor(peewee.BackrefAccessor, Generic[T]):
    pass


class ModelUpdate(peewee.ModelUpdate, Generic[T]):
    def where(self, *expressions) -> 'ModelUpdate[T]':
        pass

    def execute(self, database=None) -> int:
        pass


class BaseModel(peewee.Model):
    id: PrimaryKeyField

