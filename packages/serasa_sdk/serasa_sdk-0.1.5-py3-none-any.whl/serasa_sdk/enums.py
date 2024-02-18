from enum import Enum


class TipoArquivo(Enum):
    FOTO = 'Foto'
    DOC_IDENTIFICACAO = 'Doc. de Identificação'


class IndexadorAdicional(Enum):
    CPF = 'Número do CPF'
    CONTRATO = 'Contrato'


class APIReturnCode(Enum):
    SUCCESS = '1'
    ERROR = '-1'


class APIErrorMessage(Enum):
    INVALID_FILES = 'Tipos de arquivo enviado inválido'
    INTERNAL_ERROR = 'Não foi possível cadastrar o registro'
    INVALID_TOKEN = 'Token enviado inválido'
    EXPIRED_TOKEN = 'Token enviado expirado'
