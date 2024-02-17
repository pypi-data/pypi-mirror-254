from sqlalchemy.dialects import registry
import pytest

registry.register(
    "altibase.pyodbc", "sqlalchemy_altibase.pyodbc", "AltibaseDialect_pyodbc"
)

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")

from sqlalchemy.testing.plugin.pytestplugin import *