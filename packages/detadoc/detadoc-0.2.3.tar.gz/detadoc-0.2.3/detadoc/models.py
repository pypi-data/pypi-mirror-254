from __future__ import annotations

import calendar
import datetime
import io
from decimal import Decimal
from io import StringIO
from typing import Annotated, Any, ClassVar, NamedTuple, Optional

import bcrypt
from hx_markup import Element
from hx_markup.element import NodeText
from markdown import markdown
from markupsafe import Markup
from ormspace import functions
from ormspace.enum import StrEnum
from ormspace.functions import string_to_list
from spacestar.model import SpaceModel
from ormspace.model import modelmap, SearchModel
from ormspace.annotations import DateField, DateTimeField, ListOfStrings, OptionalDate, OptionalFloat, PasswordField, \
    PositiveDecimalField, \
    PositiveIntegerField
from pydantic import BaseModel, BeforeValidator, computed_field, Field, RootModel
from typing_extensions import Self

from detadoc.annotations import BodyMeasureFloat, BodyMeasureInteger, OptionalBoolean
from detadoc.bases import EmailBase, FinancialBase, Profile, SpaceSearchModel, Staff, Transaction
from detadoc.enum import Account, AccountSubtype, CashFlow, Engagement, enummap, EyeContact, FacialExpression, \
    Frequency, \
    Intensity, \
    InvoiceType, AccountType, \
    DosageForm, \
    Kinship, Level, MedicationRoute, \
    Month, PaymentMethod, Period, PsychomotorActivity, Quality, Rapport, Recurrence
from detadoc.regex import ActiveDrug, Package


    
@modelmap
class User(EmailBase):
    EXIST_QUERY = 'email'
    password: PasswordField
    created: DateField
    updated: Optional[datetime.date] = Field(None)
    
    def __str__(self):
        return self.email
    
    @classmethod
    async def get_and_check(cls, email: str, password: str) -> Optional[User]:
        user = await cls.get_by_email(email)
        if user:
            if user.check(password):
                return user
        return None
    
    @classmethod
    def create_encrypted(cls, email: str, password: str) -> Self:
        return cls(email=email, password=cls.encrypt_password(password))
    
    @classmethod
    def encrypt_password(cls, password: str) -> bytes:
        return bcrypt.hashpw(functions.str_to_bytes(password), bcrypt.gensalt())
    
    def check(self, password: str) -> bool:
        return bcrypt.checkpw(functions.str_to_bytes(password), self.password)
    
    def __eq__(self, other):
        return isinstance(other, type(self)) and self.email == other.email
    
    def __hash__(self):
        return hash(self.email)


@modelmap
class Register(User):
    TABLE_NAME = 'User'
    password_repeat: bytes
    
    def model_post_init(self, __context: Any) -> None:
        assert self.password == self.password_repeat
        self.password = self.encrypt_password(self.password)
    
    def asjson(self):
        data = super().asjson()
        data.pop('password_repeat', None)
        return data
    

@modelmap
class Patient(Profile):
    MODEL_GROUPS = ['Profile']
    
    
class CreatedBase(SpaceModel):
    created: DateTimeField
    
    def __lt__(self, other):
        return self.created < other.created
    
    @property
    def past_days(self) -> int:
        return (datetime.date.today() - self.created.date()).days
    
    
class PactientKeyBase(CreatedBase):
    patient_key: Patient.Key = Field(title='Chave do Paciente')
    

    def children_elements(self) -> list[Element]:
        return [
                self.list_group_item('Paciente', self.patient),
                self.list_group_item('Idade', f'{self.patient.age} anos'),
                self.list_group_item('Nascimento', self.patient.bdate),
                self.list_group_item('Gênero', self.patient.gender.value),
                self.list_group_item('CPF', self.patient.cpf or "não cadastrado"),
                self.list_group_item('Telefone', f'{self.patient.phone}' or 'não cadastrado'),
        ]
    
    def container_element(self) -> Element:
        return Element('ul', '.list-group', children=self.children_elements())
    
    def element_detail(self) -> Element:
        container: Element = Element('div', id=self.tablekey)
        container.children.append(Element('div', '.card .bg-dark bg-opacity-50', children=[
                Element('div', '.card-header', NodeText(str(self))),
                Element('div', '.card-body', self.container_element()),
        ]))
        return container
    
    def element_list_group_item(self) -> Element:
        if isinstance(self, Prescription):
            content =   Element('i', '.bi .bi-sign-stop', htmx=dict(
                                        post=f'/api/stop/{self.item_name()}/{self.key}?patient_key={self.patient_key}',
                                        target=f'#htmx-{self.item_name()}-container'))
        else:
            content = NodeText('')
        return Element('li', '.list-group-item .text-white', children=[
                Element('h6', NodeText(str(self)),
                        htmx=dict(get=f'/api/{self.item_name()}/{self.key}',
                                  target=f'#htmx-{self.item_name()}-container',
                                  indicator=f'#htmx-{self.item_name()}-indicator')),
                content
        ])
    
    def model_post_init(self, __context: Any) -> None:
        super().model_post_init(__context)
        if self.patient_key:
            if not self.patient_key.instance:
                if patient:= Patient.instance_from_context(self.patient_key.data):
                    self.patient = patient
                    
    @property
    def patient(self) -> Patient:
        return self.patient_key.instance if self.patient_key else None
    
    @patient.setter
    def patient(self, value: Patient) -> None:
        self.patient_key.set_instance(value)


class MentalExamBase(PactientKeyBase):
    notes: Optional[str] = None

@modelmap
class Symptom(PactientKeyBase):
    date: DateField
    intensity: Intensity = Intensity.I3
    recurrence: Recurrence = Recurrence.U
    name: str
    
    def __str__(self):
        if self.past_days > 2:
            return f'{self.name} (há {self.past_days} dias)'
        return f'{self.name}'



@modelmap
class Doctor(Staff):
    MODEL_GROUPS = ['Profile', 'Staff']
    EXIST_QUERY = 'key'
    crm: Optional[str] = None
    specialties: ListOfStrings
    subspecialties: ListOfStrings
    
    @classmethod
    async def data(cls) -> dict:
        return await cls.fetch_one('admin')
    
    @classmethod
    async def instance(cls) -> Optional[Self]:
        if data := await cls.data():
            return cls(**data)
        return None
    
    def model_post_init(self, __context: Any) -> None:
        super().model_post_init(__context)
        self.key = 'admin'
    
    def __str__(self):
        if self.gender.value.lower().startswith('masculino'):
            return f'Dr. {self.name}'
        return f'Dra. {self.name}'


@modelmap
class Employee(Staff):
    MODEL_GROUPS = ['Profile', 'Staff']


@modelmap
class Service(SearchModel):
    FETCH_QUERY = {'active': True}
    name: str
    price: PositiveDecimalField
    return_days: PositiveIntegerField = Field(0)
    active: bool = Field(True)
    notes: ListOfStrings
    created: DateField
    
    def __str__(self):
        return f'{self.name} valor R$ {self.price}'
    
    
# FINANCIAL

@modelmap
class JournalEntry(SpaceModel):
    transaction: Transaction
    description: str = ''
    
    def __lt__(self, other):
        assert isinstance(other, type(self))
        return self.transaction.accounting_date < other.transaction.accounting_date
    
    def __str__(self):
        return f'{self.transaction.display} {self.description}'
    
    @property
    def value(self) -> Decimal:
        if self.account.type == self.transaction_type:
            return self.amount
        return Decimal('0') - self.amount
    
    @property
    def account(self):
        return self.transaction.account
    
    @property
    def amount(self):
        return self.transaction.amount
    
    @property
    def account_subtype(self):
        return self.account.subtype
    
    @property
    def account_type(self):
        return self.account.subtype.type
    
    @property
    def transaction_type(self):
        return self.transaction.type
    
    @property
    def date(self) -> datetime.date:
        return self.transaction.accounting_date
    
    def balance(self):
        return sum([i.amount for i in self.assets()]) - sum([i.amount for i in self.liabilities()]) - sum(
                i.amount for i in self.equity())
    
    def revenues(self):
        return [i for i in self.transactions if i.account.type == AccountSubtype.RE]
    
    def expenses(self):
        return [i for i in self.transactions if i.account.type == AccountSubtype.EX]
    
    def assets(self):
        return [i for i in self.transactions if i.account.type == AccountSubtype.AT]
    
    def liabilities(self):
        return [i for i in self.transactions if i.account.type == AccountSubtype.LI]
    
    def equity(self):
        return [i for i in self.transactions if i.account.type == AccountSubtype.SE]
    
    def dividends(self):
        return [i for i in self.transactions if i.account.type == AccountSubtype.DI]
    
    def profit(self):
        return sum([i.amount for i in self.revenues()]) - sum([i.amount for i in self.expenses()])

@modelmap
class Invoice(FinancialBase):
    REVENUE_ACCOUNT: ClassVar[Account] = Account.GRE
    EXPENSE_ACCOUNT: ClassVar[Account] = Account.GEX
    PAYABLE_ACCOUNT: ClassVar[Account] = Account.PLI
    RECEIVABLE_ACCOUNT: ClassVar[Account] = Account.RAT
    CASH_ACCOUNT: ClassVar[Account] = Account.CAT
    BANK_ACCOUNT: ClassVar[Account] = Account.BAT
    DIVIDEND_ACCOUNT: ClassVar[Account] = Account.WDI
    INVOICE_TYPE: ClassVar[InvoiceType] = InvoiceType.G
    
    def children_elements(self) -> list[Element]:
        result = [
                self.list_group_item('Data', self.date),
                self.list_group_item('Valor', self.amount),
                self.list_group_item('Método de Pagamento', self.method.value),
        ]
        if (datetime.date.today() - self.date) <= datetime.timedelta(days=1):
            result.append(self.list_group_item('', f'<i class="bi bi-trash" hx-post="/financial/delete/invoice/{self.key}"> excluir</i>'))
        return result
    
    @computed_field
    @property
    def type(self) -> str:
        return self.INVOICE_TYPE.name
    
    def __str__(self):
        if self.flow == CashFlow.EX:
            if self.has_payment():
                return f'- {self.amount} R$ {self.date} {self.EXPENSE_ACCOUNT.title} {self.description}'
            return f'{self.amount} R$ {self.date + datetime.timedelta(days=31)} {self.PAYABLE_ACCOUNT.title} {self.description}'
        if self.has_payment():
            return f'{self.amount} R$ {self.date} {self.REVENUE_ACCOUNT.title} {self.description}'
        return f'{self.amount} R$ {self.date + datetime.timedelta(days=31)} {self.RECEIVABLE_ACCOUNT.title} {self.description}'
    
    def has_payment(self):
        return self.method != PaymentMethod.NO
    
    async def setup_instance(self):
        pass
    
    def not_same_day(self):
        return self.created != self.date
    
    @classmethod
    async def save_journal_entry(cls, data: dict):
        instance = cls(**data)
        await instance.setup_instance()
        transactions = []
        if instance.type == 'A':
            if instance.has_payment():
                assert instance.flow == CashFlow.RE
                transactions.append(f'{Account.RAT} {instance.amount} C {instance.date} {instance.key} {instance.description}')
                if instance.method == PaymentMethod.CA:
                    transactions.append(f'{instance.CASH_ACCOUNT} {instance.amount} D {instance.date} {instance.key} {instance.description}')
                elif instance.method in [PaymentMethod.PI, PaymentMethod.TR, PaymentMethod.DC, PaymentMethod.AD, PaymentMethod.CH, PaymentMethod.CC]:
                    transactions.append(f'{instance.BANK_ACCOUNT} {instance.amount} D {instance.date} {instance.key} {instance.description}')
            else:
                raise ValueError('Contas a receber somente podem ser recebidas.')
        elif instance.type == 'D':
            if instance.has_payment():
                assert instance.flow == CashFlow.EX
                transactions.append(f'{Account.WDI} {instance.amount} D {instance.date} {instance.key} {instance.description}')
                if instance.method == PaymentMethod.CA:
                    transactions.append(f'{instance.CASH_ACCOUNT} {instance.amount} C {instance.date} {instance.key} {instance.description}')
                elif instance.method in [PaymentMethod.PI, PaymentMethod.TR, PaymentMethod.DC, PaymentMethod.AD, PaymentMethod.CH, PaymentMethod.CC]:
                    transactions.append(f'{instance.BANK_ACCOUNT} {instance.amount} C {instance.date} {instance.key} {instance.description}')
            else:
                raise ValueError('Dividendos somente podem ser pagos.')
        elif instance.type == 'B':
            if instance.has_payment():
                assert instance.flow == CashFlow.EX
                transactions.append(f'{Account.PLI} {instance.amount} D {instance.date} {instance.key} {instance.description}')
                if instance.method == PaymentMethod.CA:
                    transactions.append(f'{instance.CASH_ACCOUNT} {instance.amount} C {instance.date} {instance.key} {instance.description}')
                elif instance.method in [PaymentMethod.PI, PaymentMethod.TR, PaymentMethod.DC, PaymentMethod.AD, PaymentMethod.CH, PaymentMethod.CC]:
                    transactions.append(f'{instance.BANK_ACCOUNT} {instance.amount} C {instance.date} {instance.key} {instance.description}')
            else:
                raise ValueError('Contas a pagar somente podem ser pagas.')
        else:
            account = instance.REVENUE_ACCOUNT if instance.flow == CashFlow.RE else instance.EXPENSE_ACCOUNT
            opposite_flow = "D" if account.type == AccountType.C else "C"
            if instance.has_payment():
                transactions.append(f'{account} {instance.amount} {account.type} {instance.date} {instance.key} {instance.description}')
                if instance.method == PaymentMethod.CA:
                    transactions.append(f'{instance.CASH_ACCOUNT} {instance.amount} {opposite_flow} {instance.date} {instance.key} {instance.description}')
                elif instance.method in [PaymentMethod.PI, PaymentMethod.TR, PaymentMethod.DC, PaymentMethod.AD, PaymentMethod.CH, PaymentMethod.CC]:
                    transactions.append(f'{instance.BANK_ACCOUNT} {instance.amount} {opposite_flow} {instance.date} {instance.key} {instance.description}')
            else:
                transactions.append(f'{account} {instance.amount} {account.type} {instance.created} {instance.key} {instance.description}')
                if instance.flow == CashFlow.RE:
                    transactions.append(f'{instance.RECEIVABLE_ACCOUNT} {instance.amount} {instance.RECEIVABLE_ACCOUNT.type} {instance.date} {instance.key} {instance.description}')
                else:
                    transactions.append(f'{instance.PAYABLE_ACCOUNT} {instance.amount} {instance.PAYABLE_ACCOUNT.type} {instance.date} {instance.key} {instance.description}')

        await JournalEntry.Database.put_all([i.asjson() for i in [JournalEntry(transaction=t, description=instance.description or str(instance)) for t in transactions]])

    
    async def save_new(self):
        new = await super().save_new()
        if new:
            await self.save_journal_entry(new)
        return new


@modelmap
class RentInvoice(Invoice):
    REVENUE_ACCOUNT = Account.RRE
    EXPENSE_ACCOUNT = Account.REX
    INVOICE_TYPE = InvoiceType.R
    TABLE_NAME = 'Invoice'

@modelmap
class ProductInvoice(Invoice):
    REVENUE_ACCOUNT = Account.PRE
    EXPENSE_ACCOUNT = Account.PEX
    INVOICE_TYPE = InvoiceType.P
    TABLE_NAME = 'Invoice'
    
@modelmap
class PatrimonialInvoice(Invoice):
    REVENUE_ACCOUNT = Account.PPE
    EXPENSE_ACCOUNT = Account.PPE
    INVOICE_TYPE = InvoiceType.T
    TABLE_NAME = 'Invoice'
    
    
@modelmap
class EarningsInvoice(Invoice):
    REVENUE_ACCOUNT = Account.REA
    EXPENSE_ACCOUNT = Account.REA
    INVOICE_TYPE = InvoiceType.E
    TABLE_NAME = 'Invoice'
    
@modelmap
class DividendInvoice(Invoice):
    INVOICE_TYPE = InvoiceType.D
    flow: CashFlow = CashFlow.EX
    TABLE_NAME: ClassVar[str] = 'Invoice'


@modelmap
class ServiceInvoice(Invoice, PactientKeyBase):
    REVENUE_ACCOUNT = Account.SRE
    EXPENSE_ACCOUNT = Account.SEX
    INVOICE_TYPE = InvoiceType.S
    TABLE_NAME = 'Invoice'
    service_key: Service.Key
    description: Optional[str] = Field('Receita de Serviço')
    discount: Annotated[
        PositiveDecimalField, Field(Decimal('0')), BeforeValidator(lambda x: Decimal('0') if not x else Decimal(x))]
    flow: CashFlow = CashFlow.RE

    def __str__(self):
        self.description = f'{self.service or self.service_key} {self.patient or self.patient_key}'
        return super().__str__()

    async def setup_instance(self):
        if not self.patient:
            self.patient_key.set_instance(await Patient.fetch_instance(self.patient_key.key))
        if not self.service:
            self.service_key.set_instance(await Service.fetch_instance(self.service_key.key))

    @property
    def service(self):
        return self.service_key.instance
    
    def balance(self):
        value = self.service.price - self.amount
        if value > self.discount:
            return value - self.discount
        return 0
    
    def ammount_check(self):
        return self.service.price - self.discount - self.amount
    

@modelmap
class ExpenseInvoice(Invoice):
    EXPENSE_ACCOUNT = Account.GEX
    INVOICE_TYPE = InvoiceType.G
    flow: CashFlow = CashFlow.EX
    TABLE_NAME: ClassVar[str] = 'Invoice'
    

@modelmap
class EnergyInvoice(ExpenseInvoice):
    EXPENSE_ACCOUNT = Account.EEX
    TABLE_NAME: ClassVar[str] = 'Invoice'
    
@modelmap
class WaterInvoice(ExpenseInvoice):
    EXPENSE_ACCOUNT = Account.WEX
    TABLE_NAME: ClassVar[str] = 'Invoice'
    
@modelmap
class PhoneInvoice(ExpenseInvoice):
    EXPENSE_ACCOUNT = Account.TEX
    TABLE_NAME: ClassVar[str] = 'Invoice'


@modelmap
class RevenueInvoice(Invoice):
    REVENUE_ACCOUNT = Account.GRE
    INVOICE_TYPE = InvoiceType.G
    flow: CashFlow = CashFlow.RE
    TABLE_NAME: ClassVar[str] = 'Invoice'
    
@modelmap
class DividendInvoice(Invoice):
    DIVIDEND_ACCOUNT = Account.WDI
    INVOICE_TYPE = InvoiceType.D
    flow: CashFlow = CashFlow.EX
    TABLE_NAME: ClassVar[str] = 'Invoice'
    
    
@modelmap
class ReceivableInvoice(Invoice):
    INVOICE_TYPE = InvoiceType.A
    
@modelmap
class PayableInvoice(Invoice):
    INVOICE_TYPE = InvoiceType.B
    
    
@modelmap
class Diagnosis(PactientKeyBase):
    FETCH_QUERY = {'end': None}
    SINGULAR = 'Diagnóstico'
    title: str
    description: Optional[str] = None
    start: DateField
    end: OptionalDate
    
    async def setup_instance(self):
        pass
    
    def __str__(self):
        return f'{self.start.year} {self.title}'

    def __lt__(self, other):
        return self.start < other.start
    
    def children_elements(self) -> list[Element]:
        result = [
                self.list_group_item('Início', self.start),
        ]
        if self.description:
            result.append(self.list_group_item('Descrição', f'{self.description}'))
        if self.end:
            result.append(self.list_group_item('Final', self.end))
        else:
            result.append(self.list_group_item('Finalizar', f'<i class="bi bi-x-circle font-x-large" hx-post="/api/stop/diagnosis/{self.key}" hx-target="#htmx-diagnosis-container"></i>'))
        return result
    
    
@modelmap
class FamilyHistory(PactientKeyBase):
    SINGULAR = 'História Familiar'
    PLURAL = 'Histórias Familiares'
    kinship: Kinship
    title: str
    description: Optional[str] = None


@modelmap
class Medication(SpaceSearchModel):
    SINGULAR = 'Medicação'
    PLURAL = 'Medicações'
    EXIST_QUERY = 'search'
    label: Optional[str] = Field(None)
    drugs: Annotated[list[ActiveDrug], BeforeValidator(string_to_list)]
    route: MedicationRoute = Field(MedicationRoute.O)
    dosage_form: DosageForm
    package: Package
    pharmaceutical: Optional[str] = Field(None)
    
    def __eq__(self, other):
        return isinstance(other, type(self)) and str(self) == str(other)
    
    def __hash__(self):
        return hash(str(self))
    
    @property
    def is_generic(self):
        return self.label in [None, '']
    
    @property
    def is_single_drug(self):
        return len(self.drugs) == 1
    
    @property
    def package_content(self):
        return getattr(self.package, '_content', None)
    
    @property
    def package_size(self):
        return Decimal(functions.parse_number(getattr(self.package, '_size', None)))

    @property
    def drug_names(self):
        return functions.join([getattr(i, '_name') for i in self.drugs], sep=" + ")
    
    @property
    def drug_strengths(self):
        return functions.join([f"{getattr(i, '_strength')}{getattr(i, '_unit')}" for i in self.drugs], sep=" + ")
    
    @property
    def name(self):
        if not self.is_generic:
            return f'{self.label} ({self.drug_names}) {self.drug_strengths}'
        return f'{self.drug_names.title()} {self.drug_strengths}'
    
    def __str__(self):
        return f'{self.name} {self.package}'


@modelmap
class Event(PactientKeyBase):
    SINGULAR = 'Evento'
    EXIST_QUERY = 'title date patient_key'
    title: str
    notes: Optional[str] = Field(None)
    date: OptionalDate
    age: OptionalFloat = Field(exclude=True)
    
    def children_elements(self) -> list[Element]:
        result = [
                Element('li', '.list-group-item', Element('span', '.text-darkorange', NodeText('Data: ')),
                        NodeText(f'{Month.read_int(self.date.month).value}/{self.date.year}')),
        ]
        if self.notes:
            result.append(Element('li', '.list-group-item', Element('span', '.text-darkorange', NodeText('Obs: ')), NodeText(self.notes)))
        result.append(f'<li class="list-group-item"><i class="bi bi-trash small-caps text-white" hx-post="/doctor/delete/event/{self.key}">Excluir</i></li>')
        return result
        
    async def setup_instance(self):
        self.patient = await Patient.fetch_instance(self.patient_key.key)
        self.setup_event_date()
        
    def setup_event_date(self):
        if all([self.age, not self.date]):
            days = datetime.timedelta(days=functions.parse_number(self.age) * 365)
            dt = self.patient.bdate + days
            leap_days = calendar.leapdays(self.patient.bdate.year, dt.year)
            self.date = dt + datetime.timedelta(days=leap_days)
    
    def __lt__(self, other):
        return self.date < other.date
    
    
    def __str__(self):
        return f'{functions.years(self.date, self.patient.bdate)} anos: {self.title}'
    
    
@modelmap
class Prescription(PactientKeyBase):
    SINGULAR = 'Prescrição'
    PLURAL = 'Prescrições'
    EXIST_QUERY = 'medication_key patient_key created'
    FETCH_QUERY = {'end': None}
    medication_key: Medication.Key
    period: Period = Period.D1
    frequency: Frequency = Frequency.N1
    dosage: Decimal = Field(Decimal('1'))
    notes: Optional[str] = None
    duration: Decimal = Field(Decimal('30'))
    end: OptionalDate = None
    
    def __str__(self):
        return f'{self.medication.name} {self.dosage} {self.medication.dosage_form.value} {self.frequency.value}x/{self.period.value}  {self.notes or ""} [{self.remaining_days} dias, {self.computed_boxes} cx]'
    
    def asjson(self):
        data = super().asjson()
        data.pop('search', None)
        return data

    def element_detail(self) -> Element:
        title = Element('h5', NodeText(str(self)))
        hr = Element('hr', )
        start = Element('h6', NodeText(f'início: {self.start}'))
        remaining = Element('h6', NodeText(f'dias restantes: {self.remaining_days}'))
        boxes = Element('h6', NodeText(f'caixas prescritas: {self.computed_boxes}'))
        interrupted = Element('h6', NodeText(f'interrompida: {self.end if self.end else "não"}'))
        return Element('div', title, hr, start, remaining, boxes, interrupted)
    
    def element_list_group_item(self) -> Element:
        return Element('li', '.list-group-item .text-white', children=[
                Element('div', '.row', children=[
                        Element('h6', '.col-10', NodeText(str(self)), htmx=dict(get=f'/api/prescription/{self.key}', target=f'#htmx-{self.item_name()}-container', indicator='#htmx-prescription-indicator')),
                        Element('ul', '.col-2', '.nav', children=[
                                Element('i', '.bi .bi-sign-stop', htmx=dict(post=f'/api/stop/prescription/{self.key}?patient_key={self.patient_key}', target=f'#htmx-{self.item_name()}-container'))
                        ])
                ])

        ])
    
    @property
    def medication(self):
        return self.medication_key.instance
    
    
    @property
    def computed_boxes(self) -> Optional[Decimal]:
        if self.duration:
            if self.medication.dosage_form == DosageForm.DRO:
                day_needed = self.daily_dosage/20
            else:
                day_needed = self.daily_dosage
            needed = self.duration * day_needed
            if package_size:= self.medication.package_size:
                return Decimal((needed/package_size).__ceil__())
        return Decimal('0')
    
    @property
    def daily_dosage(self):
        return ((self.dosage * int(self.frequency))/self.period.days).__round__(2)
    
    @property
    def expiration_date(self) -> datetime.date:
        return self.start + datetime.timedelta(days=self.total_days)
    
    @property
    def total_days(self):
        return  int((self.computed_boxes * self.medication.package_size)/ self.daily_dosage)
    
    @property
    def remaining_days(self):
        today = datetime.date.today()
        if self.created.date() < today:
            return self.total_days - (datetime.date.today() - self.created.date()).days
        return self.duration
    
    @medication.setter
    def medication(self, value: Medication):
        self.medication_key.set_instance(value)
        
    async def setup_instance(self):
        if not self.medication:
            self.medication = await Medication.fetch_instance(str(self.medication_key))
    
    
# @modelmap
# class BodyMeasure(PactientKeyBase):
#     SINGULAR = 'Medida Corporal'
#     PLURAL = 'Medidas Corporais'
#     key: Optional[str] = Field(None, title='Chave')
#     created: DateTimeField = Field(title='Criado em')
#     weight: BodyMeasureFloat = Field(title='Peso (Kg)')
#     height: BodyMeasureFloat = Field(title='Altura (cm)')
#     waist: BodyMeasureFloat = Field(title='Cintura (cm)')
#     hip: BodyMeasureFloat = Field(title='Quadril (cm)')
#     sbp: BodyMeasureInteger = Field(title='PAS')
#     dbp: BodyMeasureInteger = Field(title='PAD')
#     hr: BodyMeasureInteger = Field(title='FC (bpm)')
#     rr: BodyMeasureInteger = Field(title='FR (rpm)')
#
#     def __lt__(self, other):
#         return self.created < other.created
#
#     def __str__(self):
#         with StringIO() as buf:
#             buf.write(f'{self.created.date()} {self.created.hour}h')
#             for k, v in self.model_fields.items():
#                 if value:= getattr(self, k):
#                     if k == 'weight':
#                         buf.write(f", peso {value}Kg")
#                     elif k == 'height':
#                         buf.write(f", altura {value}cm")
#                     elif k == 'waist':
#                         buf.write(f", cintura {value}cm")
#                     elif k == 'hip':
#                         buf.write(f", quadril {value}cm")
#                     elif k == 'hr':
#                         buf.write(f", FC {value}bpm")
#                     elif k == 'rr':
#                         buf.write(f", FR {value}rpm")
#             if self.waist_hip_ratio:
#                 buf.write(f", CQR {self.waist_hip_ratio}")
#             if self.bmi:
#                 buf.write(f", IMC {self.bmi}Kg/m2")
#             if self.sbp and self.dbp:
#                 buf.write(f', PA {self.sbp}/{self.dbp}mmHg')
#             return buf.getvalue()
#
#     @property
#     def waist_hip_ratio(self):
#         if self.waist and self.hip:
#             return (self.waist / self.hip).__round__(2)
#         return None
#
#     @property
#     def bmi(self):
#         if self.weight and self.height:
#             return (self.weight / (self.height/100 * self.height/100)).__round__(1)
#         return None
#
#     def children_elements(self) -> list[Element]:
#         result = []
#         for k, v in self.model_fields.items():
#             if value:= getattr(self, k):
#                 result.append(self.list_group_item(v.title, value))
#         if bmi:= self.bmi:
#             result.append(self.list_group_item('IMC (Kg/m2)', bmi))
#         if whr:= self.waist_hip_ratio:
#             result.append(self.list_group_item('Indice C/Q', whr))
#         return result
#
#     # def element_detail(self) -> Element:
#     #     container: Element = Element('div', '.p-2', id=self.tablekey)
#     #     container.children.append(Element('h3', children=str(self)))
#     #     container.children.append(Markup(Element('hr')))
#     #     for k, v in self.model_fields.items():
#     #         if value:= getattr(self, k):
#     #             container.children.append(markdown(f'\n##### {v.title}\n{value}'))
#     #     return container
#

@modelmap
class PhysicalExam(PactientKeyBase):
    SINGULAR = 'Exame Físico'
    PLURAL = 'Exames Físicos'
    key: Optional[str] = Field(None, title='Chave')
    created: DateTimeField = Field(title='Criado em')
    weight: BodyMeasureFloat = Field(title='Peso (Kg)')
    height: BodyMeasureFloat = Field(title='Altura (cm)')
    waist: BodyMeasureFloat = Field(title='Cintura (cm)')
    hip: BodyMeasureFloat = Field(title='Quadril (cm)')
    sbp: BodyMeasureInteger = Field(title='PAS')
    dbp: BodyMeasureInteger = Field(title='PAD')
    hr: BodyMeasureInteger = Field(title='FC (bpm)')
    rr: BodyMeasureInteger = Field(title='FR (rpm)')
    notes: Optional[str] = None
    
    def __lt__(self, other):
        return self.created < other.created
    
    def __str__(self):
        with StringIO() as buf:
            buf.write(f'{self.created.date()} {self.created.hour}h')
            for k, v in self.model_fields.items():
                if value := getattr(self, k):
                    if k == 'weight':
                        buf.write(f", peso {value}Kg")
                    elif k == 'height':
                        buf.write(f", altura {value}cm")
                    elif k == 'waist':
                        buf.write(f", cintura {value}cm")
                    elif k == 'hip':
                        buf.write(f", quadril {value}cm")
                    elif k == 'hr':
                        buf.write(f", FC {value}bpm")
                    elif k == 'rr':
                        buf.write(f", FR {value}rpm")
            if self.waist_hip_ratio:
                buf.write(f", CQR {self.waist_hip_ratio}")
            if self.bmi:
                buf.write(f", IMC {self.bmi}Kg/m2")
            if self.sbp and self.dbp:
                buf.write(f', PA {self.sbp}/{self.dbp}mmHg')
            return buf.getvalue()
    
    @property
    def waist_hip_ratio(self):
        if self.waist and self.hip:
            return (self.waist / self.hip).__round__(2)
        return None
    
    @property
    def bmi(self):
        if self.weight and self.height:
            return (self.weight / (self.height / 100 * self.height / 100)).__round__(1)
        return None
    
    def children_elements(self) -> list[Element]:
        result = []
        for k, v in self.model_fields.items():
            if value := getattr(self, k):
                result.append(self.list_group_item(v.title, value))
        if bmi := self.bmi:
            result.append(self.list_group_item('IMC (Kg/m2)', bmi))
        if whr := self.waist_hip_ratio:
            result.append(self.list_group_item('Indice C/Q', whr))
        return result


class MentalExam(PactientKeyBase):
    def __str__(self):
        with io.StringIO(f'{self.created.date()}, ') as buf:
            for k, v in self.model_fields.items():
                if member:= getattr(self, k):
                    if isinstance(member, StrEnum):
                        if not member.name == 'I':
                            buf.write(f"{member.value}, ")
                    elif v.annotation in [bool, Optional[bool]]:
                        buf.write(f"{v.title}, ")
            return buf.getvalue().lower()
    
@modelmap
class Appearance(MentalExam):
    """
    This is a description of how a patient looks during observation.
    It can be determined within the first seconds of clinical introduction as well as noted throughout the interview.
    Details to be included are if they look older or younger than their stated age, what they are wearing,
    their grooming and hygiene, and if they have any tattoos or scars.
    If a patient looks more youthful than their stated age, they may have a developmental delay or dress in an
    age-inappropriate manner.
    Patients that look older than their stated age may have underlying severe medical conditions, years of substance
    abuse, or often years of poorly controlled mental illness.
    Grooming and hygiene can give an idea of a patient’s level of functioning.
    Those with poor hygiene and grooming generally denote that in the context of their mental illness that they
    currently have poor functioning.
    Those with poor grooming or hygiene may be severely depressed, have a neurocognitive disorder, or be experiencing
    a negative symptom of a psychotic disorder such as schizophrenia.
    Tattoos and scars can paint a picture of a patient’s history, personality, and behaviors.
    Scars tell stories about old, significant injuries from accidental trauma, harm caused by another individual,
    or self-inflicted harm. Self-inflicted injuries frequently include superficial cutting, needle tracks from IV
    drug use, or past suicide attempts.
    Tattoos often are the name of a family member, significant other, or lost loved one.
    They can also depict gang marks, vulgar imagery, or extravagant artwork.
    If a certain level of trust has been established through the interview, the interviewer can ask about the
    significance of the tattoos or scars and what story they tell about the patient.
    """
    SINGULAR = 'Aparência'
    hygiene: Quality = Field(Quality.Q2, title='higiene')
    clothing: Quality = Field(Quality.Q2, title='vestimenta')
    self_harm: Intensity = Field(Intensity.I0, title='automutilação')
    lesions: Intensity = Field(Intensity.I0, title='lesões')
    weight_status: Level = Field(Level.LN, title='peso')
    age_status: Level = Field(Level.LN, title='idade')
    notes: Optional[str] = None
    
    def __str__(self):
        with io.StringIO() as buffer:
            buffer.write(f'{self.hygiene.value.lower()} condição de higiene, ')
            buffer.write(f'{self.clothing.value.lower()} condição de vestimenta, ')
            if self.self_harm == Intensity.I0:
                buffer.write(f'ausência de automutilação')
            else:
                buffer.write(f'presença de automutilação de gravidade {self.self_harm.value.lower()}')
            buffer.write(', ')
            if self.self_harm == Intensity.I0:
                buffer.write(f'ausência de outras lesões, ')
            else:
                buffer.write(f'presença de outras lesões de gravidade {self.self_harm.value.lower()}, ')
            if self.notes:
                if self.weight_status == Level.LB:
                    buffer.write('baixo peso')
                elif self.weight_status == Level.LN:
                    buffer.write('peso normal')
                elif self.weight_status == Level.LA:
                    buffer.write('acima do peso')
                buffer.write(f', {self.notes}')
            else:
                if self.weight_status == Level.LB:
                    buffer.write('baixo peso')
                elif self.weight_status == Level.LN:
                    buffer.write('peso normal')
                elif self.weight_status == Level.LA:
                    buffer.write('acima do peso')
            return buffer.getvalue()

    
@modelmap
class Behaviour(MentalExam):
    """
    This is a description obtained by observing how a patient acts during the interview. First, it is essential to
    note whether or not the patient is in distress. If a patient is in distress it may be due to underlying medical
     problems causing discomfort, a patient having been brought against their will to the hospital for psychiatric
     evaluation, or due to the severity of their hallucinations or paranoia terrifying the patient. Next, a description
     of their interaction with the interviewer should be noted.[2] For example, is the patient cooperative, or are they
     agitated, avoidant, refusing to talk, or unable to be redirected? A patient that is not cooperative with the
     interview may be reluctant if the psychiatric evaluation was involuntary or are actively experiencing symptoms
     of mental illness. Patients that are unable to be redirected often are acutely responding to internal stimuli or
     exhibit manic behavior. Lastly, it is important to note if the behavior the patient is displaying is appropriate
     for the situation. For example, it can be considered appropriate for a patient who was brought in via police for
     involuntary evaluation to be irritable and not cooperative. However, if in that same scenario, the patient was
     laughing and smiling throughout the interview, it would be considered inappropriate.
    """
    SINGULAR = 'Comportamento'
    created: DateTimeField
    eye_contact: EyeContact = Field(EyeContact.R, title='contato visutal')
    facies: FacialExpression = Field(FacialExpression.R, title='expressão facial')
    psychomotor_activity: PsychomotorActivity = Field(PsychomotorActivity.R, title='atividade psicomotora')
    engagement: Engagement = Field(Engagement.R, title='engajamento')
    rapport: Rapport = Field(Rapport.R, title='raport')
    involuntary_movements: Optional[bool] = None
    tremor: OptionalBoolean
    akathisia: OptionalBoolean
    ataxia: OptionalBoolean
    bradykinesia: OptionalBoolean
    tics: OptionalBoolean
    dyskinesia: OptionalBoolean
    maneirisms: OptionalBoolean
    
    
@modelmap
class Speech(MentalExam):
    SINGULAR = 'Fala'
    amount: Level = Level.LN
    fluency: Level = Level.LN
    rate: Level = Level.LN
    rhythm: Level = Level.LN
    volume: Level = Level.LN
    tone: Level = Level.LN
    
    
@modelmap
class Perception(MentalExam):
    SINGULAR = 'Percepção'
    visual_hallucination: bool = False
    auditory_hallucination: bool = False
    olfactory_hallucination: bool = False
    tactile_hallucination: bool = False
    gustatory_hallucination: bool = False
    ilusions: bool = False
    
@modelmap
class Cognition(MentalExam):
    SINGULAR = 'Cognição'
    
    @enummap
    class Alertness(StrEnum):
        I = 'Indefinido'
        N = 'Alerta'
        D = 'Sonolento'
        O = 'Obnubilado'
        S = 'Estupor'
        C = 'Comatoso'
    alertness: Alertness = Alertness.N
    
    @enummap
    class Orientation(StrEnum):
        I = 'Indefinido'
        N = 'Orientado'
        T = 'Desorientado em relação ao Tempo'
        L = 'Desorientado em relação ao Espaço'
        P = 'Desorientado em relação a Pessoas'
        S = 'Desorientado em relação ao Eu'
        D = 'Desorientado'
    orientation: Orientation = Orientation.N
    
    @enummap
    class Attention(StrEnum):
        I = 'Indefinido'
        N = 'Atento'
        L = 'Pouco Desatento'
        M = 'Moderadamente Desatento'
        S = 'Muito Desatento'
        D = 'Totalmente Desatento'
    attention: Attention = Attention.N
    
    @enummap
    class Memory(StrEnum):
        I = 'Indefinido'
        N = 'Memória Normal'
        S = 'Memória Imediata Prejudicada'
        R = 'Memória Recente Prejudicada'
        D = 'Memória Tardia Prejudicada'
        L = 'Memória de Longo Prazo Prejudicada'
        G = 'Memória Globalmente Prejudicada'
    memory: Memory = Memory.N
    
    @enummap
    class AbstractReasoning(StrEnum):
        I = 'Indefinido'
        N = 'Raciocínio Abstrato Preservado'
        L = 'Raciocínio AbstratoLevemente Prejudicado'
        M = 'Raciocínio Abstrato Moderadamente Prejudicado'
        H = 'Raciocínio AbstratoMuito Prejudicado'
        G = 'Raciocínio Literal'
    abstract_reasoning: AbstractReasoning = AbstractReasoning.N
    
    @enummap
    class Intellect(StrEnum):
        I = 'Indefinido'
        N = 'Normal'
        L = 'Capacidade Intelectiva Reduzida'
        M = 'Capacidade Intelectiva Muito Reduzida'
        H = 'Capacidade Intelectiva Elevada'
    intellect: Intellect = Intellect.N
    
    # def __str__(self):
        # with io.StringIO() as buf:
        #     for k, v in self.model_fields.items():
        #         if member:= getattr(self, k):
        #             if isinstance(member, StrEnum):
        #                 if not member.name == 'I':
        #                     buf.write(f"{member.value}, ")
        #             elif v.annotation in [bool, Optional[bool]]:
        #                 buf.write(f"{v.title}, ")
        #     return buf.getvalue().lower()
            
            
    
    
@modelmap
class MoodAndAffect(MentalExam):
    SINGULAR = 'Humor e Afeto'
    mood: Optional[str] = Field(None, title='Humor')
    
    @enummap
    class AffectQuality(StrEnum):
        N = 'Eutímico'
        H = 'Feliz'
        S = 'Triste'
        I = 'Irritável'
        R = 'Raivoso'
        X = 'Agitado'
        Z = 'Bizarro'
        A = 'Ansioso'
        E = 'Exaltado'
        M = 'Eufórico'
        D = 'Disfórico'
        B = 'Embotado'
    affect: AffectQuality = AffectQuality.N
    
    @enummap
    class AffectRange(StrEnum):
        N = 'Amplo'
        L = 'Lábil'
        R = 'Constrito'
        F = 'Plano'

    affect_range: AffectRange = AffectRange.N
    
    @enummap
    class AffectCongruency(StrEnum):
        N = 'Humor e Afeto Congruentes'
        I = 'Humor e Afeto Incongruentes'
        
    congruency: AffectCongruency = AffectCongruency.N
    
    def __str__(self):
        if self.mood:
            with io.StringIO(f'humor {self.mood}, ') as buf:
                buf.write(super().__str__())
                return buf.getvalue()
    

# @modelmap
# class Cognition(PactientKeyBase):
    # speech: Optional[DataModel] = Field(default_factory=DataModel, title='Discurso')
    # mood: Optional[DataModel] = Field(default_factory=DataModel, title='Humor')
    # affect: Optional[str] = Field(None, title='Afeto')
    # thought_form: Optional[str] = Field(None, title='Forma do Pensamento')
    # thought_content: Optional[str] = Field(None, title='Conteúdo do Pensamento')
    # thought_possession: Optional[str] = Field(None, title='Possessão do Pensamento')
    # perception: Optional[str] = Field(None, title='Percepção')
    # cognition: Optional[str] = Field(None, title='Cognição')
    # insight: Optional[str] = Field(None, title='Insight')
    # judgement: Optional[str] = Field(None, title='Julgamento')
    # risk_to_self: Optional[str] = Field(None, title='Risco para Si')
    # risk_to_others: Optional[str] = Field(None, title='Risco para Outros')


@modelmap
class Visit(PactientKeyBase):
    SINGULAR = 'Visita'
    created: DateTimeField = Field(title='Início da Visita')
    complaints: str = Field(title='Queixa Principal')
    intro: Optional[str] = Field(None, title='Introdução')
    subjective: Optional[str] = Field(None, title='Sintomas')
    objective: Optional[str] = Field(None, title='Exame Médico')
    assessment: Optional[str] = Field(None, title='Avaliação')
    plan: Optional[str] = Field(None, title='Plano Terapêutico')
    end: DateTimeField = Field(title='Fim da Visita')
    
    def __lt__(self, other):
        return self.created < other.created
    
    def __str__(self):
        return f'{self.created.date()} {self.complaints}'
        
    def element_detail(self) -> Element:
        container: Element = Element('div', '.p-2', id=self.tablekey)
        container.children.append(Element('h3', children=str(self)))
        container.children.append(Markup(Element('hr')))
        container.children.append(markdown(f'\n##### Queixa Principal\n{self.complaints}'))
        if self.intro:
            container.children.append(markdown(f'\n##### Introdução\n{self.intro}'))
        if self.subjective:
            container.children.append(markdown(f'\n##### Sintomas\n{self.subjective}'))
        if self.objective:
            container.children.append(markdown(f'\n##### Exame\n{self.objective}'))
        if self.assessment:
            container.children.append(markdown(f'\n##### Avaliação\n{self.assessment}'))
        if self.plan:
            container.children.append(markdown(f'\n##### Plano Terapêutico\n{self.plan}'))
        return container
    


