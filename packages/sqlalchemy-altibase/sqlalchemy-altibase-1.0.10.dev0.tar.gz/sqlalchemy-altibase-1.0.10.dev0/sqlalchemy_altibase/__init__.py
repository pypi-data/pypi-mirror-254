from sqlalchemy.dialects import registry as _registry
from . import base  # noqa
from . import pyodbc  # noqa
from .base import CHAR
from .base import DATE
from .base import FLOAT
from .base import NCHAR
from .base import VARCHAR
from .base import NCHAR
from .base import CLOB
from .base import BLOB
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.dialects.oracle.base import BINARY_DOUBLE
from sqlalchemy.dialects.oracle.base import BINARY_FLOAT
from .base import DECIMAL
from .base import BIGINT
from .base import INTEGER
from .base import SMALLINT
from .base import BYTE
from .base import NIBBLE
from .base import BIT
from .base import VARBIT
from .base import GEOMETRY


from .pyodbc import get_odbc_info

# default (and only) dialect
base.dialect = dialect = pyodbc.dialect

_registry.register(
    "altibase.pyodbc", "sqlalchemy_altibase.pyodbc", "AltibaseDialect_pyodbc"
)

__all__ = (
    "CHAR",
    "VARCHAR",
    "NCHAR",
    "CLOB",
    "BLOB",
    "NUMBER",
    "FLOAT",
    "BINARY_DOUBLE",
    "BINARY_FLOAT",
    "DECIMAL",
    "BIGINT",
    "INTEGER",
    "SMALLINT",
    "DATE",
    "BYTE",
    "NIBBLE",
    "BIT",
    "VARBIT",
    "GEOMETRY",
)
