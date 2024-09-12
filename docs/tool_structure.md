# Guide: Creating a Tool and Its Tests

## Tool Structure

A typical tool in this framework consists of the following components:

1. Input Schema
2. Output Schema
3. Tool Configuration
4. Tool Logic
5. Tests
6. README
7. Requirements

Let's break down each component:

### 1. Input Schema

Define an input schema class that inherits from `BaseIOSchema`:

```python
from pydantic import Field
from atomic_agents.agents.base_agent import BaseIOSchema

class YourToolInputSchema(BaseIOSchema):
    """Docstring describing the input schema."""
    expression: str = Field(..., description="The expression to evaluate.")
```

### 2. Output Schema

Define an output schema class that also inherits from `BaseIOSchema`:

```python
class YourToolOutputSchema(BaseIOSchema):
    """Docstring describing the output schema."""
    result: str = Field(..., description="The result of the evaluation.")
```

### 3. Tool Configuration

Create a configuration class that inherits from `BaseToolConfig`:

```python
from atomic_agents.lib.tools.base_tool import BaseToolConfig

class YourToolConfig(BaseToolConfig):
    # Add any tool-specific configuration options here
    pass
```

### 4. Tool Logic

Implement the main tool logic in a class that inherits from `BaseTool`:

```python
from atomic_agents.lib.tools.base_tool import BaseTool

class YourTool(BaseTool):
    input_schema = YourToolInputSchema
    output_schema = YourToolOutputSchema

    def __init__(self, config: YourToolConfig = YourToolConfig()):
        super().__init__(config)

    def run(self, params: YourToolInputSchema) -> YourToolOutputSchema:
        # Implement your tool logic here
        result = self._evaluate_expression(params.expression)
        return YourToolOutputSchema(result=result)

    def _evaluate_expression(self, expression: str) -> str:
        # Implement the actual evaluation logic
        pass
```

### 5. Tests

Create a test file in the `tests` directory:

```python
import os
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tool.your_tool import YourTool, YourToolInputSchema, YourToolOutputSchema

def test_your_tool():
    your_tool = YourTool()
    input_schema = YourToolInputSchema(expression="2 + 2")
    result = your_tool.run(input_schema)
    assert result == YourToolOutputSchema(result="4")

if __name__ == "__main__":
    test_your_tool()
```

### 6. README

Create a `README.md` file in the tool's root directory:

```markdown
# Your Tool Name

## Overview
Brief description of what your tool does.

## Features
- List key features of your tool

## Example Usage

```python
from your_tool import YourTool

tool = YourTool()
result = tool.run(expression="2 + 2")
print(result)  # Output: {"result": "4"}
```
```

### 7. Requirements

Create a `requirements.txt` file in the tool's root directory:

```
atomic_agents>=0.3.3
pydantic>=2.8.2
# Add any other specific dependencies for your tool
```

## Creating a New Tool

To create a new tool:

1. Create a new directory under `atomic_tools/` for your tool.
2. Implement the components described above.
3. Ensure your tool follows the structure of existing tools like Calculator or YouTube Transcript Scraper.
4. Write comprehensive tests covering various scenarios.
5. Keep your README up-to-date with accurate information and usage examples.

By following this guide, you can create well-structured, testable tools that integrate seamlessly with the existing framework.
