calculator_tool
===============

CalculatorToolInputSchema
-------------------------

.. code-block:: python

    class CalculatorToolInputSchema(BaseIOSchema):

Schema for the input of the CalculatorTool.

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

CalculatorToolOutputSchema
--------------------------

.. code-block:: python

    class CalculatorToolOutputSchema(BaseIOSchema):

Schema for the output of the CalculatorTool.

This schema defines the structure of the output data from the CalculatorTool.
It contains the result of the calculation as a string.

Attributes:
    result (str): Result of the calculation.

Examples:
    >>> output_schema = CalculatorToolOutputSchema(result="4.00000000000000")
    >>> output_schema.result
    '4.00000000000000'

CalculatorToolConfig
--------------------

.. code-block:: python

    class CalculatorToolConfig(BaseToolConfig):

Configuration for the CalculatorTool.

This class can be extended to include any configuration options for the CalculatorTool.
Currently, it doesn't define any additional options.

CalculatorTool
--------------

.. code-block:: python

    class CalculatorTool(BaseTool):

Tool for performing calculations based on the provided mathematical expression.

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

__init__
--------

.. code-block:: python

    def __init__(self, config):

Initialize the CalculatorTool.

Args:
    config (CalculatorToolConfig, optional): Configuration for the tool.
        Defaults to CalculatorToolConfig().

run
---

.. code-block:: python

    def run(self, params):

Run the CalculatorTool with the given parameters.

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

README
------

.. include:: ../../../atomic_tools/calculator_tool/README.md
   :parser: myst_parser.sphinx_

