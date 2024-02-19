import datetime
import re
from decimal import Decimal
from typing import Any

from ormspace import functions
from ormspace.bases import AbstractRegex

from detadoc.enum import Account, AccountType


class Package(AbstractRegex):
    GROUP_PATTERN = re.compile(r'(?P<size>\d+[.,]\d+|\d+)(\s+)?(?P<content>[\w\-]+(\s[\w\-]+)+|[\w\-]+)')


class ActiveDrug(AbstractRegex):
    GROUP_PATTERN = re.compile(r'(?P<name>[\w\-]+(\s[\w\-]+)+|[\w\-]+)\s+(?P<strength>\d+[.,]\d+|\d+)\s?(?P<unit>\w+/\w+|\w+)')


class ProfessionalId(AbstractRegex):
    GROUP_PATTERN = re.compile(r'(?P<ref1>\w+)\s(?P<ref2>[\w\-]+)|(?P<ref3>\w+)')


class Transaction(AbstractRegex):
    GROUP_PATTERN = re.compile(r'^(?P<account>[A-Z]{3})\s(?P<amount>\d+[.,]\d+|\d+)\s(?P<type>[CD])\s(?P<accounting_date>\d{4}-\d{2}-\d{2})\s(?P<invoice_key>\w+)')
    SEPARATOR = ' '
    
    def __init__(self, value):
        self.value = str(value)
        super().__init__(value)
    
    @property
    def account(self) -> Account:
        return Account[getattr(self, '_account')]
    
    @property
    def accounting_date(self) -> datetime.date:
        return datetime.date.fromisoformat(getattr(self, '_accounting_date'))
    
    @property
    def resolve(self) -> str:
        data = self.GROUP_PATTERN.search(self.value)
        if data:
            return self.SEPARATOR.join(data.groupdict().values())
        raise ValueError('error at Transaction.resolve')
    
    def __str__(self):
        return self.resolve
    
    @property
    def display(self):
        return f'{self.parsed_value} R$ {self.accounting_date} {self.account.title}'
    
    @property
    def parsed_value(self):
        if self.account.type == self.type:
            return self.amount
        return Decimal('0') - self.amount
    
    @property
    def type(self):
        return AccountType[getattr(self, '_type')]
    
    @property
    def invoice_key(self):
        return getattr(self, '_invoice_key')
    
    def is_credit(self):
        return self.type == AccountType.C
    
    def is_debit(self):
        return self.type == AccountType.D
    
    def is_current(self):
        if date:= self.accounting_date:
            if today:= datetime.date.today():
                return (date.year, date.month) == (today.year, today.month)
        raise ValueError('error at Transaction.is_current')
    
    @property
    def amount(self):
        return Decimal(getattr(self, '_amount', '0').replace(",", "."))
    
    @staticmethod
    def validate_transactions(value: Any) -> list[str]:
        if value:
            if isinstance(value, str):
                return [i.strip() for i in re.compile(r'[+;]').findall(value) if
                        all([i is not None, isinstance(i, str)])]
            elif isinstance(value, list):
                return [i.strip() for i in value if all([i is not None, isinstance(i, str)])]
            return value
        return []


class FloatString(AbstractRegex):
    NON_GROUP_PATTERN = re.compile(r'\d+[.,]\d+|\d+]')
    
    @property
    def resolve(self) -> str:
        if match:= self.NON_GROUP_PATTERN.search(self.value):
            return functions.parse_number(match.group(0))
        return ''
    
class IntegerString(AbstractRegex):
    NON_GROUP_PATTERN = re.compile(r'\d+')


if __name__ == '__main__':
    x = Transaction('CAT 2000 C 2024-01-01 ddddd')
    print(x)
    print(x.invoice_key)
    print(x.display)
