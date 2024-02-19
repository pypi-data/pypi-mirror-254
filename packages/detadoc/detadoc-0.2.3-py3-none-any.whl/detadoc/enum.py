import datetime
import io
from collections import ChainMap, namedtuple
from decimal import Decimal
from enum import Enum
from functools import wraps

from hx_markup import Element
from hx_markup.element import NodeText
from markupsafe import Markup
from ormspace.enum import StrEnum

EnumMap = ChainMap()

def html_options(enum_class: StrEnum, value: str = None) -> Markup:
    with io.StringIO() as buffer:
        if value:
            for i in enum_class.__members__.values():
                buffer.write('\n')
                buffer.write(str(Element('option', NodeText(i.value), value=i.name)))
        else:
            for i in enum_class.__members__.values():
                buffer.write('\n')
                if value in [i.name, i.value]:
                    buffer.write(str(Element('option', 'selected', NodeText(i.value), value=i.name)))
                else:
                    buffer.write(str(Element('option', NodeText(i.value), value=i.name)))
        return Markup(buffer.getvalue())

def enummap(enum_class: type[StrEnum]):
    @wraps(enum_class)
    def wrapper():
        EnumMap[enum_class.__name__] = enum_class
        # setattr(enum_class, 'markup', classmethod(lambda cls, x = None: html_options(cls, x)))
        return enum_class
    return wrapper()



@enummap
class Mood(StrEnum):
    I = 'Indefinido'
    LOW = 'Rebaixado'
    ANX = 'Ansioso'
    EUT = 'Eutímico'
    ANG = 'Irritável'
    ENR = 'Irado'
    HEU = 'Hipomaníaco'
    EUP = 'Eufórico'
    GUI = 'Culposo'
    APA = 'Apático'
    
    
@enummap
class Affect(StrEnum):
    I = 'Indefinido'
    LOW = 'Rebaixado'
    ANX = 'Ansioso'
    EUT = 'Eutímico'
    ANG = 'Irritável'
    ENR = 'Irado'
    HEU = 'Hipomaníaco'
    EUP = 'Eufórico'
    GUI = 'Culposo'
    APA = 'Apático'
    
@enummap
class AffectRange(StrEnum):
    I = 'Indefinido'
    F = 'Fixo'
    R = 'Restrito'
    L = 'Lábil'
    A = 'Amplo'
    
@enummap
class AffectIntensity(StrEnum):
    I = 'Indefinido'
    H = 'Intensificado'
    R = 'Normal'
    L = 'Embotado'

@enummap
class ThoughtFlow(StrEnum):
    I = 'Indefinido'
    NOR = 'Normal'
    LOA = 'Perda de Associações'
    CIR = 'Circunstancial'
    TAN = 'Tangencial'
    FLI = 'Fuga de Idéias'
    
    
@enummap
class Month(StrEnum):
    JAN = "Janeiro"
    FEB = "Fevereiro"
    MAR = 'Março'
    APR = "Abril"
    MAY = 'Maio'
    JUN = 'Junho'
    JUL = 'Julho'
    AUG = 'Agosto'
    SEP = 'Setembro'
    OCT = 'Outubro'
    NOV = 'Novembro'
    DEC = 'Dezembro'
    
    @classmethod
    def read_int(cls, key):
        if isinstance(key, int):
            if key == 1: return cls.JAN
            elif key == 2: return cls.FEB
            elif key == 3: return cls.MAR
            elif key == 4: return cls.APR
            elif key == 5: return cls.MAY
            elif key == 6: return cls.JUN
            elif key == 7: return cls.JUL
            elif key == 8: return cls.AUG
            elif key == 9: return cls.SEP
            elif key == 10: return cls.OCT
            elif key == 11: return cls.NOV
            elif key == 12: return cls.DEC
        return None
    
@enummap
class MedicationRoute(StrEnum):
    O = 'Oral'
    P ='Parenteral'
    T = 'Tópica'
    F = 'Oftalmológica'
    N = 'Nasal'
    A = 'Otoscópica'
    R = 'Retal'
    
    
@enummap
class Intensity(StrEnum):
    I = 'Indefinido'
    I0 = 'Ausente'
    I1 = 'Mínima'
    I2 = 'Leve'
    I3 = 'Moderada'
    I4 = 'Severa'
    I5 = 'Extrema'
    
@enummap
class Quality(StrEnum):
    I = 'Indefinido'
    Q0 = 'Péssima'
    Q1 = 'Ruim'
    Q2 = 'Regular'
    Q3 = 'Boa'
    Q4 = 'Ótima'
  
@enummap
class Level(StrEnum):
    I = 'Indefinido'
    LA = 'Acima'
    LN = 'Normal'
    LB = 'Abaixo'
    
@enummap
class Engagement(StrEnum):
    I = 'Indefinido'
    L = 'Pouco Cooperativo'
    R = 'Cooperativo'
    H = 'Muito Cooperativo'
    
@enummap
class FacialExpression(StrEnum):
    I = 'Indefinido'
    A = 'De Raiva'
    R = 'Relaxada'
    D = 'Apática'
    F = 'De Medo'
    
@enummap
class PsychomotorActivity(StrEnum):
    I = 'Indefinido'
    L = 'Psicomotricidade Reduzida'
    R = 'Psicomotricidade Normal'
    H = 'Psicomotricidade Aumentada'
    
@enummap
class Rapport(StrEnum):
    I = 'Indefinido'
    L = 'Raport Reduzido'
    R = 'Raport Regular'
    H = 'Raport Intenso'
    
@enummap
class EyeContact(StrEnum):
    I = 'Indefinido'
    L = 'Contato Visual Reduzido'
    R = 'Contato Visual Regular'
    H = 'Contato Visual Intenso'
    F = 'Olhar Fixo'
    
    
@enummap
class SpeechRate(StrEnum):
    I = 'Indefinido'
    L = 'Velocidade da Fala Reduzida'
    R = 'Velocidade da Fala Normal'
    H = 'Velocidade da Fala Aumentada'
    
@enummap
class SpeechQuality(StrEnum):
    I = 'Indefinido'
    L = 'Fala de Qualidade Empobrecida'
    R = 'Fala de Qualidade Regular'
    H = 'Fala de Qualidade Elaborada'


@enummap
class SpeechTone(StrEnum):
    I = 'Indefinido'
    M = 'Tom da Fala Monotônico'
    R = 'Tom da Fala Regular'
    T = 'Tom da Fala Trêmulo'
    C = 'Tom da Fala Cantarolante'

@enummap
class SpeechFluence(StrEnum):
    I = 'Indefinido'
    G = 'Guagueira'
    A = 'Fluência Arrastada'
    P = 'Fluência Artificial'
    R = 'Fluência Regular'
    
@enummap
class SpeechVolume(StrEnum):
    I = 'Indefinido'
    L = 'Volume Baixo'
    R = 'Volume Normal'
    H = 'Volume Alto'
    
    
@enummap
class ThoughtContent(StrEnum):
    I = 'Indefinido'
    D = 'Delírios'
    O = 'Obsessões'
    C = 'Compulsões'
    H = 'Idéias Supervalorizadas'
    R = 'Normal'
    
@enummap
class SuicidalThought(StrEnum):
    I = 'Indefinido'
    A = 'Ausente'
    S = 'Pensamento Suicida'
    P = 'Planejamento Suicida'
    
@enummap
class Tenacity(StrEnum):
    I = 'Indefinido'
    L = 'Hipotenaz'
    N = 'Normotenaz'
    H = 'Hipertenaz'
    
@enummap
class Vigilance(StrEnum):
    I = 'Indefinido'
    L = 'Hipovigil'
    N = 'Normovigil'
    H = 'Hipervigil'
    
@enummap
class Intelect(StrEnum):
    I = 'Indefinido'
    V = 'Deficiência Intelectual'
    L = 'Abaixo do Esperado'
    N = 'Mediana'
    H = 'Acima do Esperrado'
    G = 'Altas Habilidades'

@enummap
class DosageForm(StrEnum):
    TAB = 'Comprimido'
    CAP = 'Cápsula'
    PAT = 'Adesivo'
    LIQ = 'Líquido'
    STR = 'Strip'
    POW = 'Pó'
    PAS = 'Pasta'
    DRO = 'Gota'
    AER = 'Aerosol'
    AMP = 'Ampola'
    
@enummap
class PaymentMethod(StrEnum):
    NO = 'Nenhum'
    CA = 'Dinheiro'
    PI = 'Pix'
    TR = 'Transferência'
    CC = 'Cartão de Crédito'
    DC = 'Cartão de Débito'
    AD = 'Débito em Conta'
    CH = 'Cheque'

@enummap
class AccountType(StrEnum):
    C = 'Crétido'
    D = 'Débito'
    
    def __str__(self):
        return self.name
    
@enummap
class AccountSubtype(namedtuple('AccountTypeMember', 'title type'), Enum):
    DI = 'Dividendo', AccountType.D
    AT = 'Ativo', AccountType.D
    EX = 'Despesa', AccountType.D
    SE = 'Equidade', AccountType.C
    LI = 'Dívida', AccountType.C
    RE = 'Receita', AccountType.C
    
    def __str__(self):
        return self.name

@enummap
class Account(namedtuple('AccountMember', 'title subtype'), Enum):
    # ativos
    CAT = 'Dinheiro', AccountSubtype.AT
    BAT = 'Conta Bancária', AccountSubtype.AT
    RAT = 'Contas a Receber', AccountSubtype.AT
    SAT = 'Investimento de Curto Prazo', AccountSubtype.AT
    LAT = 'Investimento de Longo Prazo', AccountSubtype.AT
    PPE = 'Propriedade, Planta e Equipamento', AccountSubtype.AT
    INV = 'Inventario', AccountSubtype.AT
    PAT = 'Produtos', AccountSubtype.AT
    # receitas
    GRE = 'Receita Geral', AccountSubtype.RE
    SRE = 'Receita de Serviço', AccountSubtype.RE
    RRE = 'Receita de Aluguel', AccountSubtype.RE
    PRE = 'Receita de Produto', AccountSubtype.RE
    # despesas
    GEX = 'Despesa Geral', AccountSubtype.EX
    SEX = 'Despesa com Serviço', AccountSubtype.EX
    REX = 'Despesa com Aluguel', AccountSubtype.EX
    PEX = 'Despesa com Produto', AccountSubtype.EX
    IEX = 'Despesa com Imposto', AccountSubtype.EX
    SAE = 'Despesa com Salários', AccountSubtype.EX
    EEX = 'Despesa com Energia', AccountSubtype.EX
    WEX = 'Despesa com Água/Esgoto', AccountSubtype.EX
    TEX = 'Despesa com Telefone/Internet', AccountSubtype.EX
    # compromissos
    PLI = 'Contas a Pagar', AccountSubtype.LI
    STL = 'Empréstimo de Curto Prazo', AccountSubtype.LI
    LTL = 'Empréstimo de Longo Prazo', AccountSubtype.LI
    SLI = 'Salários a Pagar', AccountSubtype.LI
    CLI = 'Créditos Retidos', AccountSubtype.LI
    # equidade
    REA = 'Lucros Retidos', AccountSubtype.SE
    CAP = 'Capital Societário', AccountSubtype.SE
    # dividendos
    WDI = 'Saque de Lucro', AccountSubtype.DI

    
    def __str__(self):
        return self.name
    
    @property
    def type(self):
        return self.subtype.type

@enummap
class CashFlow(StrEnum):
    RE = 'Receita'
    EX = 'Despesa'
    
@enummap
class InvoiceType(StrEnum):
    G = 'Fatura Geral'
    S = 'Fatura de Serviço (obrigatórios paciente e serviço)'
    R = 'Fatura de Aluguel'
    P = 'Fatura de Produto'
    T = 'Fatura Patrimonial'
    A = 'Receber Conta'
    B = 'Pagar Conta'
    D = 'Pagamento de Dividendo'
    E = 'Reter Lucros'

    
@enummap
class Recurrence(StrEnum):
    I = 'Indefinido'
    U = 'Episódio Único'
    O = 'Ocasional'
    C = 'Contínuo'
    D = 'Diário'
    S = 'Semanal'
    Q = 'Quinzenal'
    M = 'Mensal'
    B = 'Bimestral'
    T = 'Trimestral'
    X = 'Semestral'
    A = 'Anual'
    


@enummap
class Period(StrEnum):
    H1 = 'por hora'
    H2 = 'a cada 2 horas'
    H3 = 'a cada 3 horas'
    H4 = 'a cada 4 horas'
    H5 = 'a cada 5 horas'
    H6 = 'a cada 6 horas'
    H7 = 'a cada 7 horas'
    H8 = 'a cada 8 horas'
    D1 = 'ao dia'
    D2 = 'a cada 2 dias'
    D3 = 'a cada 3 dias'
    W1 = 'por semana'
    W2 = 'a cada 2 semanas'
    W3 = 'a cada 3 semanas'
    W4 = 'a cada 4 semanas'
    M1 = 'ao mês'
    M2 = 'a cada 2 meses'
    M3 = 'a cada 3 meses'
    M4 = 'a cada 4 meses'
    M5 = 'a cada 5 meses'
    M6 = 'a cada 6 meses'
    Y1 = 'ao ano'
    
    def timedelta(self):
        integer = int(self.name[-1])
        if self.name.startswith('H'):
            return datetime.timedelta(days=1 * integer/24)
        elif self.name.startswith('D'):
                return datetime.timedelta(days=1 * integer)
        elif self.name.startswith('W'):
            return datetime.timedelta(days=7 * integer)
        elif self.name.startswith('M'):
            return datetime.timedelta(days=30 * integer)
        elif self.name.startswith('Y'):
            return datetime.timedelta(days=365 * integer)
        
    @property
    def days(self) -> Decimal:
        if self.timedelta() < datetime.timedelta(days=1):
            return Decimal((self.timedelta().total_seconds()/datetime.timedelta(days=1).total_seconds())).__round__(3)
        return Decimal(self.timedelta().days)
    
@enummap
class Frequency(StrEnum):
    _ignore_ = 'Frequency i'
    Frequency = vars()
    for i in range(1, 13):
        Frequency[f'N{i}'] = f'{i}'
        
    def __int__(self):
        return int(self.value)
        
@enummap
class Kinship(StrEnum):
    K1 = 'Primeiro Grau'
    K2 = 'Segundo Grau'
    K3 = 'Terceiro Grau'
    
    def __int__(self):
        return int(self.name[-1])
        
if __name__ == '__main__':
    for i in Period.__members__.values():
        print(i.days)
