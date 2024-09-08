import os
import glob
import ast


def extract_docstring_and_signature(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        tree = ast.parse(content)

    docstrings = {}
    signatures = {}

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            docstring = ast.get_docstring(node)
            if docstring:
                docstrings[node.name] = docstring.strip()

            # Extract the signature
            if isinstance(node, ast.FunctionDef):
                args = [a.arg for a in node.args.args]
                signature = f"def {node.name}({', '.join(args)}):"
            else:  # ClassDef
                bases = [b.id for b in node.bases if isinstance(b, ast.Name)]
                signature = f"class {node.name}({', '.join(bases)}):"

            signatures[node.name] = signature

    return docstrings, signatures


def generate_rst_files():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tools_dir = os.path.join(root_dir, "atomic_tools")
    docs_dir = os.path.join(root_dir, "docs", "source", "tools")

    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    # Generate main tools page
    with open(os.path.join(docs_dir, "index.rst"), "w") as f:
        f.write("Tools\n=====\n\n")
        f.write(".. toctree::\n   :maxdepth: 2\n\n")

    for tool_dir in glob.glob(os.path.join(tools_dir, "*")):
        if os.path.isdir(tool_dir):
            tool_name = os.path.basename(tool_dir)

            # Generate RST file for each tool
            with open(os.path.join(docs_dir, f"{tool_name}.rst"), "w") as f:
                f.write(f'{tool_name}\n{"=" * len(tool_name)}\n\n')

                # Find the main Python file for the tool
                main_file = glob.glob(os.path.join(tool_dir, f"{tool_name}.py"))
                if main_file:
                    main_file = main_file[0]
                    docstrings, signatures = extract_docstring_and_signature(main_file)

                    # Document all objects with docstrings
                    for obj_name, docstring in docstrings.items():
                        f.write(f'{obj_name}\n{"-" * len(obj_name)}\n\n')
                        f.write(
                            f".. code-block:: python\n\n    {signatures[obj_name]}\n\n"
                        )
                        f.write(f"{docstring}\n\n")

                # Include README.md content if it exists
                readme_path = os.path.join(tool_dir, "README.md")
                if os.path.exists(readme_path):
                    f.write("README\n------\n\n")
                    f.write(
                        f".. include:: ../../../atomic_tools/{tool_name}/README.md\n   :parser: myst_parser.sphinx_\n\n"
                    )

            # Add tool to main tools page
            with open(os.path.join(docs_dir, "index.rst"), "a") as f:
                f.write(f"   {tool_name}\n")


if __name__ == "__main__":
    generate_rst_files()
