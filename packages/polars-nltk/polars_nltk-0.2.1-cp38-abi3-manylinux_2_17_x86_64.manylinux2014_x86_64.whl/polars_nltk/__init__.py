import polars as pl
from polars.utils.udfs import _get_shared_lib_location

lib = _get_shared_lib_location(__file__)


@pl.api.register_expr_namespace("nltk")
class NltkOperations:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def snowball_stem(self, *, language: str) -> pl.Expr:
        return self._expr.register_plugin(
            lib=lib,
            symbol="snowball_stem",
            is_elementwise=True,
            kwargs={'language': language},
    )