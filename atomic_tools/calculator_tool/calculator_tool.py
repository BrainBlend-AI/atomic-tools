from pydantic import Field
from rich.console import Console
from sympy import sympify

from atomic_agents.agents.base_agent import BaseIOSchema
from atomic_agents.lib.tools.base_tool import BaseTool, BaseToolConfig


class CalculatorToolInputSchema(BaseIOSchema):
    """Tool for performing calculations.

    Supports basic arithmetic operations like addition, subtraction,
    multiplication, and division, but also more complex operations like
    exponentiation and trigonometric functions. Use this tool to evaluate
    mathematical expressions.

    Attributes:
        expression: Mathematical expression to evaluate.

    Examples:
        >>> input_schema = CalculatorToolInputSchema(expression="2 + 2")
        >>> input_schema.expression
        '2 + 2'
    """

    expression: str = Field(
        ..., description="Mathematical expression to evaluate. For example, '2 + 2'."
    )


class CalculatorToolOutputSchema(BaseIOSchema):
    """Schema defining the output of the CalculatorTool.

    Attributes:
        result: Result of the calculation.

    Examples:
        >>> output_schema = CalculatorToolOutputSchema(result="4")
        >>> output_schema.result
        '4'
    """

    result: str = Field(..., description="Result of the calculation.")


class CalculatorToolConfig(BaseToolConfig):
    """Configuration for the CalculatorTool."""

    pass


class CalculatorTool(BaseTool):
    """Tool for performing calculations based on the provided mathematical expression.

    Attributes:
        input_schema: The schema for the input data.
        output_schema: The schema for the output data.

    Examples:
        >>> tool = CalculatorTool()
        >>> input_data = CalculatorToolInputSchema(expression="2 + 2")
        >>> result = tool.run(input_data)
        >>> print(result.result)
        4.00000000000000
    """

    input_schema = CalculatorToolInputSchema
    output_schema = CalculatorToolOutputSchema

    def __init__(self, config: CalculatorToolConfig = CalculatorToolConfig()):
        """Initialize the CalculatorTool.

        Args:
            config: Configuration for the tool.
        """
        super().__init__(config)

    def run(self, params: CalculatorToolInputSchema) -> CalculatorToolOutputSchema:
        """Run the CalculatorTool with the given parameters.

        Args:
            params: The input parameters for the tool, adhering to the input schema.

        Returns:
            The output of the tool, adhering to the output schema.

        Examples:
            >>> tool = CalculatorTool()
            >>> input_data = CalculatorToolInputSchema(expression="2 * 3")
            >>> result = tool.run(input_data)
            >>> print(result.result)
            6.00000000000000
        """
        # Explicitly convert the string form of the expression
        parsed_expr = sympify(str(params.expression))
        # Evaluate the expression numerically
        result = parsed_expr.evalf()
        return CalculatorToolOutputSchema(result=str(result))


if __name__ == "__main__":
    rich_console = Console()
    rich_console.print(
        CalculatorTool().run(CalculatorToolInputSchema(expression="2 + 2"))
    )
