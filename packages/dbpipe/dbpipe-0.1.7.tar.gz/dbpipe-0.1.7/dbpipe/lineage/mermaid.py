import os
import json

def process_json_file(file_path, mermaid_diagrams):
    with open(file_path, 'r') as file:
        data = json.load(file)
        markdown = generate_mermaid_markdown(data)
        mermaid_diagrams.append(markdown)

def generate_mermaid_markdown(data):
    sources = data.get("sources", [])
    destination = data.get("destination", "")

    mermaid_markdown = ""
    for source in sources:
        mermaid_markdown += f"""
{source} -->{destination}"""
    return mermaid_markdown


def generate_mermaid_markdown_file(folder_path, output_file_path):
    mermaid_diagrams = []

    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            process_json_file(file_path, mermaid_diagrams)

    # Write all accumulated Mermaid diagrams to a new Markdown file
    with open(output_file_path, 'w') as output_file:
        output_file.write("```mermaid\n")
        output_file.write("graph LR;\n")
        for diagram in mermaid_diagrams:
            output_file.write(diagram.strip() + "\n")
        output_file.write("```\n")


# generate_mermaid_markdown_file('pipes','pipes.md')
