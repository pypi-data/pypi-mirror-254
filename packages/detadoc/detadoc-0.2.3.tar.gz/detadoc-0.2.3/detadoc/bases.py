from __future__ import annotations

import datetime
import io
import re
from collections import namedtuple
from decimal import Decimal
from enum import Enum
from typing import Annotated, Any, Callable, ClassVar, Optional

from ormspace import functions
from ormspace.bases import AbstractRegex
from spacestar.model import SpaceModel, SpaceSearchModel
from ormspace.model import modelmap
from ormspace.annotations import DateField, PositiveDecimalField, TitleField
from ormspace.enum import Gender, StrEnum
from pydantic import BeforeValidator, computed_field, EmailStr, Field, field_validator, InstanceOf
from typing_extensions import Self

from detadoc.annotations import ProfileKey, StaffKey
from detadoc.enum import Account, AccountSubtype, CashFlow, AccountType, PaymentMethod
from detadoc.regex import Transaction



class EmailBase(SpaceModel):
    email: EmailStr
    
    @classmethod
    async def get_by_email(cls, email: str) -> Optional[Self]:
        if data := await cls.instances_list(query={'email': email}):
            assert len(data) == 1
            return data[0]
        return None


@modelmap
class Person(SpaceSearchModel):
    EXIST_QUERY = ['code', 'cpf']
    fname: TitleField
    lname: TitleField
    gender: Gender
    bdate: DateField
    cpf: Optional[str] = None
    sname: Optional[str] = None
    
    @property
    def fullname(self):
        return self.sname if self.sname else ' '.join([self.fname, self.lname])
    
    @property
    def name(self):
        words = self.fullname.split()
        if len(words) >= 2:
            return f'{words[0]} {words[-1]}'
        return self.fullname

    
    def __str__(self):
        return self.fullname
    
    @property
    def age(self):
        return functions.years(datetime.date.today(), self.bdate)
    
    # noinspection PyNestedDecorators
    @field_validator('cpf')
    @classmethod
    def _cpf_validator(cls, v: str) -> str:
        if v:
            digits = ''.join(functions.find_digits(v))
            if len(digits) != 11:
                raise ValueError('CPF deve ter 11 digitos')
            return digits
        return v
    
    @computed_field
    @property
    def code(self) -> str:
        with io.StringIO() as f:
            f.write(self.bdate.isoformat().replace('-', ''))
            f.write(self.gender.name)
            f.write(self.fname[:2])
            f.write(self.lname.split()[-1][:2])
            return functions.normalize(f.getvalue().upper())
        
    async def save_new(self):
        data = self.asjson()
        if self.cpf:
            query = [{'cpf': self.cpf}, {'code': self.code}]
        else:
            query = {'code': self.code}
        exist = await self.fetch_all(query=query)
        if not exist:
            new = await self.Database.save(data)
            if new:
                return new
        return None


class ContactBase(SpaceModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    
    # noinspection PyNestedDecorators
    @field_validator('phone')
    @classmethod
    def _phone_validator(cls, v: str) -> str:
        if v:
            digits = ''.join(re.findall(r'\+|\d', v))
            return digits
        return v


class Profile(Person, ContactBase):
    MODEL_GROUPS = ['Provider', 'Employee', 'Patient']


class Staff(Profile):
    MODEL_GROUPS = ['Provider', 'Employee']
    cpf: str
    phone: str
    email: EmailStr
    address: str
    city: str


class FinancialBase(SpaceSearchModel):
    description: str
    amount: PositiveDecimalField
    created: DateField
    creator: str = 'Doctor.admin'
    method: PaymentMethod
    notes: Optional[str] = None
    date: DateField
    flow: CashFlow
    
    
    def __lt__(self, other):
        assert isinstance(other, type(self))
        if self.date == other.date:
            return self.amount < other.amount
        return self.date < other.date
        
    
    def __str__(self):
        return f' R$ {self.amount} {self.flow} {self.created} {self.description}'


# class Entry(SpaceModel):
#     transaction: Transaction
#     description: str = ''
#
#     def __lt__(self, other):
#         assert isinstance(other, type(self))
#         return self.transaction.accounting_date < other.transaction.accounting_date
#
#     def __str__(self):
#         return f'{self.transaction.display} {self.description}'
#
#     @property
#     def value(self) -> Decimal:
#         if self.account.type == self.transaction_type:
#             return self.amount
#         return Decimal('0') - self.amount
#
#     @property
#     def account(self):
#         return self.transaction.account
#
#     @property
#     def amount(self):
#         return self.transaction.amount
#
#     @property
#     def account_subtype(self):
#         return self.account.subtype
#
#     @property
#     def account_type(self):
#         return self.account.subtype.type
#
#     @property
#     def transaction_type(self):
#         return self.transaction.type
#
#

