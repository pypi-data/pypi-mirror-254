import re
import regex

from sigma.conversion.deferred import DeferredQueryExpression
from sigma.conversion.state import ConversionState
from sigma.exceptions import SigmaFeatureNotSupportedByBackendError
from sigma.conversion.base import TextQueryBackend
from sigma.conditions import ConditionItem, ConditionAND, ConditionOR, ConditionNOT
from sigma.types import SigmaCompareExpression
from typing import ClassVar, Dict, Tuple, Union, Pattern


def number_as_string(value):
    number_string: ClassVar[Pattern] = re.compile("^[0-9%']*$")
    return number_string.match(value)


class QRadarBackend(TextQueryBackend):
    """QRadar backend."""
    # See the pySigma documentation for further infromation:
    # https://sigmahq-pysigma.readthedocs.io/en/latest/Backends.html

    service_devicetype = dict()
    product_devicetype = dict()

    name: ClassVar[str] = "QRadar backend"
    formats: Dict[str, str] = {
        "default": "Plain QRadar queries",
    }
    requires_pipeline: bool = True  # does the backend requires that a processing
    # pipeline is provided? This information can be used by user interface programs
    # like Sigma CLI to warn users about inappropriate usage of the backend.

    parenthesize = True

    precedence: ClassVar[Tuple[ConditionItem, ConditionItem, ConditionItem]] = (
        ConditionNOT, ConditionAND, ConditionOR)
    group_expression: ClassVar[
        str] = "({expr})"  # precedence override grouping as format string

    # Generated query tokens
    token_separator: str = " "  # separator inserted between all boolean operators

    # String output
    ## Fields
    ### Quoting

    field_quote: ClassVar[
        str] = '"'  # Character used to quote field characters if field_quote_pattern
    # doesn't match

    field_quote_pattern_negation: ClassVar[
        bool] = True  # Negate field_quote_pattern result. Field name is quoted if
    # pattern doesn't match if set to True

    ## Values
    str_quote: ClassVar[
        str] = "'"  # string quoting character (added as escaping character)
    escape_char: ClassVar[
        str] = "'"  # Escaping character for special characrers inside string
    filter_chars: ClassVar[str] = ""  # Characters filtered
    bool_values: ClassVar[Dict[bool, str]] = {
        # Values to which boolean values are mapped.
        True: "true",
        False: "false",
    }

    # cidr expressions
    cidr_wildcard: ClassVar[str] = "_"  # Character used as single wildcard

    # Numeric comparison operators
    compare_op_expression: ClassVar[
        str] = "{field} {operator} {value}"  # Compare operation query as format string
    # Mapping between CompareOperators elements and strings used as replacement for
    # {operator} in compare_op_expression
    compare_operators: ClassVar[Dict[SigmaCompareExpression.CompareOperators, str]] = {
        SigmaCompareExpression.CompareOperators.LT: "<",
        SigmaCompareExpression.CompareOperators.LTE: "<=",
        SigmaCompareExpression.CompareOperators.GT: ">",
        SigmaCompareExpression.CompareOperators.GTE: ">=",
    }

    # Field value in list,
    # e.g. "field in (value list)" or "field containsall (value list)"
    convert_or_as_in: ClassVar[bool] = True  # Convert OR as in-expression
    # converted into in-expression

    device_type_or_in_operator: str
    list_separator: ClassVar[str] = ", "  # List element separator

    # Query finalization: appending and concatenating deferred query part
    deferred_start: ClassVar[
        str] = ""  # String used as separator between main query and deferred parts
    deferred_separator: ClassVar[
        str] = ""  # String used to join multiple deferred query parts
    deferred_only_query: ClassVar[
        str] = ""  # String used as query if final query only contains deferred

    # expression

    # implement custom methods for query elements not covered by the default backend base
    # Documentation: https://sigmahq-pysigma.readthedocs.io/en/latest/Backends.html

    def convert_condition_not(
            self, cond: ConditionNOT, state: ConversionState
    ) -> Union[str, DeferredQueryExpression]:
        """Conversion of NOT conditions:
        create 'NOT()' function"""
        arg = cond.args[0]
        try:
            if arg.__class__ in self.precedence:  # group if AND, OR condition negated
                return self.not_token + '(' + self.convert_condition_group(arg,
                                                                           state) + ')'
            else:
                expr = self.convert_condition(arg, state)
                if isinstance(expr, DeferredQueryExpression):  # negate deferred
                    # expression and pass it to parent
                    return expr.negate()
                else:  # convert negated expression to string
                    return self.not_token + '(' + expr + ')'
        except TypeError:  # pragma: no cover
            raise SigmaFeatureNotSupportedByBackendError(
                "Operator 'not' not supported by the backend")

    def device_type_expression(self, rule, device_type_field_name, device_types) -> str:
        """Creates an expression to match the rule's log source:
       using 'devicetype' field instead of 'LOGSOURCETYPENAME()' function for better
       performance"""
        device_type = ''
        log_sources_devicetype = set(
            d for d in
            (self.product_devicetype.get(rule.logsource.product, [])
             + self.service_devicetype.get(rule.logsource.service, [])
             )
            + device_types
            if d is not None
        )
        if len(log_sources_devicetype) == 1:
            device_type = f'{device_type_field_name}={next(iter(log_sources_devicetype))}'
        elif len(log_sources_devicetype) > 1:
            device_type = self.field_in_list_expression.format(
                field=f'{device_type_field_name}',
                op=self.device_type_or_in_operator,
                list=self.list_separator.join(
                    [str(log_source) for log_source in log_sources_devicetype]),
            )
        return (
            f'{device_type} {self.and_token} ' + '{query}'
            if device_type else '{query}'
        )

    def use_parenthesis(self, match_device_type: str, query: str) -> bool:
        """Wrap query with parenthesis if device_type is not empty and the query
        contains 'OR' outside parenthesis"""
        parenthesize = False
        if not match_device_type.startswith('{') and f' {self.or_token} ' in query:
            parentheses_pattern = r'\((?:[^()]+|(?R))*\)'
            or_expressions = [
                expression for expression in regex.split(parentheses_pattern, query)
                if f' {self.or_token} ' in expression
            ]
            if or_expressions:
                parenthesize = True
        return parenthesize
