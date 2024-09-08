"""
Calculator Tool

This module provides a powerful calculator tool that can evaluate mathematical
expressions. It supports basic arithmetic operations, as well as more complex
functions like exponentiation and trigonometric calculations.

Usage:
    from atomic_tools.calculator_tool import CalculatorTool, CalculatorToolInputSchema

    calculator = CalculatorTool()
    result = calculator.run(CalculatorToolInputSchema(expression="sin(pi/2) + cos(pi)"))
    print(result.result)  # Output: 1.00000000000000

See Also:
    - atomic_tools.scientific_calculator: For more advanced scientific calculations
    - atomic_tools.unit_converter: For unit conversion capabilities
"""

from pydantic import Field
from rich.console import Console
from sympy import sympify

from atomic_agents.agents.base_agent import BaseIOSchema
from atomic_agents.lib.tools.base_tool import BaseTool, BaseToolConfig


class CalculatorToolInputSchema(BaseIOSchema):
    """Schema for the input of the CalculatorTool.

    This schema defines the structure of the input data for the CalculatorTool.
    It accepts a mathematical expression as a string.

    Attributes:
        expression (str): Mathematical expression to evaluate.

    Examples:
        >>> input_schema = CalculatorToolInputSchema(expression="2 + 2")
        >>> input_schema.expression
        '2 + 2'
        >>> input_schema = CalculatorToolInputSchema(expression="sin(pi/2)")
        >>> input_schema.expression
        'sin(pi/2)'
    """

    expression: str = Field(
        ...,
        description="Mathematical expression to evaluate. Supports arithmetic operations, "
        "trigonometric functions, and constants like pi and e. For example: '2 + 2', 'sin(pi/2)', 'e^2'.",
    )


class CalculatorToolOutputSchema(BaseIOSchema):
    """Schema for the output of the CalculatorTool.

    This schema defines the structure of the output data from the CalculatorTool.
    It contains the result of the calculation as a string.

    Attributes:
        result (str): Result of the calculation.

    Examples:
        >>> output_schema = CalculatorToolOutputSchema(result="4.00000000000000")
        >>> output_schema.result
        '4.00000000000000'
    """

    result: str = Field(..., description="Result of the calculation as a string.")


class CalculatorToolConfig(BaseToolConfig):
    """Configuration for the CalculatorTool.

    This class can be extended to include any configuration options for the CalculatorTool.
    Currently, it doesn't define any additional options.
    """

    pass


class CalculatorTool(BaseTool):
    """Tool for performing calculations based on the provided mathematical expression.

    This tool evaluates mathematical expressions using the SymPy library, which allows
    for symbolic mathematics and precise numerical evaluation.

    Attributes:
        input_schema (Type[CalculatorToolInputSchema]): The schema for the input data.
        output_schema (Type[CalculatorToolOutputSchema]): The schema for the output data.

    Examples:
        >>> tool = CalculatorTool()
        >>> input_data = CalculatorToolInputSchema(expression="2 + 2")
        >>> result = tool.run(input_data)
        >>> print(result.result)
        4.00000000000000

        >>> input_data = CalculatorToolInputSchema(expression="sin(pi/2)")
        >>> result = tool.run(input_data)
        >>> print(result.result)
        1.00000000000000
    """

    input_schema = CalculatorToolInputSchema
    output_schema = CalculatorToolOutputSchema

    def __init__(self, config: CalculatorToolConfig = CalculatorToolConfig()):
        """Initialize the CalculatorTool.

        Args:
            config (CalculatorToolConfig, optional): Configuration for the tool.
                Defaults to CalculatorToolConfig().
        """
        super().__init__(config)

    def run(self, params: CalculatorToolInputSchema) -> CalculatorToolOutputSchema:
        """Run the CalculatorTool with the given parameters.

        This method evaluates the mathematical expression provided in the input
        and returns the result.

        Args:
            params (CalculatorToolInputSchema): The input parameters for the tool,
                adhering to the input schema.

        Returns:
            CalculatorToolOutputSchema: The output of the tool, adhering to the output schema.

        Examples:
            >>> tool = CalculatorTool()
            >>> input_data = CalculatorToolInputSchema(expression="2 * 3 + 4")
            >>> result = tool.run(input_data)
            >>> print(result.result)
            10.0000000000000

            >>> input_data = CalculatorToolInputSchema(expression="e^(i*pi) + 1")
            >>> result = tool.run(input_data)
            >>> print(result.result)
            0.e-15 + 0.e-15*I
        """
        parsed_expr = sympify(str(params.expression))
        result = parsed_expr.evalf()
        return CalculatorToolOutputSchema(result=str(result))


if __name__ == "__main__":
    rich_console = Console()
    calculator = CalculatorTool()

    examples = [
        "2 + 2",
        "sin(pi/2)",
        "e^2",
        "sqrt(16) + log(10)",
        "(3 + 4j) * (2 - 3j)",
    ]

    rich_console.print("[bold]Calculator Tool Examples:[/bold]")
    for expr in examples:
        result = calculator.run(CalculatorToolInputSchema(expression=expr))
        rich_console.print(f"Expression: {expr}")
        rich_console.print(f"Result: {result.result}\n")
