#!/usr/bin/env python3
import markdown
import os
from weasyprint import HTML

# Create pdfs directory if it doesn't exist
os.makedirs("pdfs", exist_ok=True)

# Path to the markdown file
md_file = "hardware_design/circuit_implementation.md"
output_html = "temp_circuit.html"
output_pdf = "pdfs/circuit_implementation.pdf"

# Read the markdown file
with open(md_file, 'r') as f:
    md_content = f.read()

# Convert Markdown to HTML
html_content = markdown.markdown(
    md_content,
    extensions=['tables', 'fenced_code', 'codehilite']
)

# Add some CSS for styling
css = """
<style>
body {
    font-family: Arial, sans-serif;
    margin: 40px;
    line-height: 1.6;
}
h1, h2, h3, h4 {
    color: #333;
}
code {
    background-color: #f5f5f5;
    padding: 2px 4px;
    border-radius: 4px;
}
pre {
    background-color: #f5f5f5;
    padding: 10px;
    border-radius: 4px;
    overflow-x: auto;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}
table, th, td {
    border: 1px solid #ddd;
}
th, td {
    padding: 8px;
    text-align: left;
}
th {
    background-color: #f2f2f2;
}
</style>
"""

# Create a complete HTML document
html_document = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Circuit Implementation</title>
    {css}
</head>
<body>
    {html_content}
</body>
</html>
"""

# Write the HTML to a file
with open(output_html, 'w') as f:
    f.write(html_document)

# Convert HTML to PDF
HTML(output_html).write_pdf(output_pdf)

# Clean up temporary HTML file
os.remove(output_html)

print(f"PDF created at: {output_pdf}") 