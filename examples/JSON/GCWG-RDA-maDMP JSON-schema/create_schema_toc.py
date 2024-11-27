import pandas as pd
import json
import numpy as np
import urllib.parse

"""
Depreciated: This script is no longer used. The TOC is now generated in the maDMP-Generation-Form.
"""

'''
This script generates the Table of Contents (TOC) in for the maDMP schema based on the Orange Tab. 
- The TOC is in the form of html, and can be immediately used in the form at https://github.com/FAIRERdata/maDMP-Generation-Form.
- The file is saved as table_of_contents.html in the current directory. Its information should be added to the metadata file.
'''


with open('./GCWG-RDA-maDMP-schema.json', "r", encoding="utf-8") as file:
    schema = json.load(file)

toc_json = {}

def extract_toc(schema, toc, id_path = "root_"):
    if 'properties' in schema:
        for key, value in schema['properties'].items():
            key_name = id_path + "/" + key
            toc[key_name] = {}
            if 'properties' in value:
                extract_toc(value, toc[key_name], key_name + "_")

extract_toc(schema, toc_json)

#json.dump(toc_json, open('toc.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)


def generate_html_table_of_contents(data, level=1):
    """
    Recursively generates an HTML table of contents from a nested dictionary.

    :param data: The dictionary to convert.
    :param level: The nesting level (used for indentation).
    :return: A string containing the HTML table of contents.
    """
    html = ""
    indent = "  " * level  # Indentation for better readability

    for key, value in data.items():
        key_list = key.split("/")
        link_content = key_list[-1] 
        id = "".join(key_list)
        html += f'{indent}<li> <a href="#{id}">{link_content}</a>\n'

        if isinstance(value, dict) and value:  # If the value is a nested dictionary
            html += f"{indent}  <ul>\n"
            html += generate_html_table_of_contents(value, level + 2)
            html += f"{indent}  </ul>\n"

        html += f"{indent}</li>\n"

    return html


# Generate the HTML table of contents
html_toc = "<ul>\n"
html_toc += generate_html_table_of_contents(toc_json)
html_toc += "</ul>"

# Save the HTML to a file
with open("table_of_contents.html", "w", encoding="utf-8") as file:
    file.write(html_toc)

print("HTML table of contents saved as 'table_of_contents.html'")


