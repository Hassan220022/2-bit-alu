#!/usr/bin/env python3
import os
import re
import subprocess
import shutil

def convert_md_to_pdf(md_file, output_pdf):
    """Convert a markdown file to PDF using pandoc with xelatex"""
    print(f"Converting {md_file} to {output_pdf}...")
    
    # Create temp directory if it doesn't exist
    temp_dir = "temp_html"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Create a processed version of the markdown file
    processed_md = f"{temp_dir}/{os.path.basename(md_file)}_processed.md"
    
    # Read the markdown file
    with open(md_file, 'r') as f:
        md_content = f.read()
    
    # Replace problematic Unicode characters
    md_content = md_content.replace('Ω', 'Ohm')
    md_content = md_content.replace('μ', 'u')
    
    # Process mermaid blocks - replace with a note
    md_content = re.sub(
        r'```mermaid(.*?)```',
        r'<div style="background-color: #ffffd9; padding: 10px; border: 1px solid #e6e6b8; border-radius: 4px;">\n<em>Mermaid diagram removed for PDF compatibility</em>\n</div>',
        md_content, 
        flags=re.DOTALL
    )
    
    # Handle ASCII diagrams by replacing with a note for box-drawing characters
    ascii_art_pattern = r'```(?!python|bash|javascript|json|html|css)(.+?)```'
    md_content = re.sub(
        ascii_art_pattern,
        r'<pre style="font-family: monospace; white-space: pre;">\1</pre>',
        md_content,
        flags=re.DOTALL
    )
    
    # Save the processed markdown file
    with open(processed_md, 'w') as f:
        f.write(md_content)
    
    # Try direct pandoc conversion (best compatibility)
    try:
        pandoc_cmd = [
            'pandoc',
            processed_md,
            '-o', output_pdf,
            '--pdf-engine=xelatex',
            '-V', 'geometry:margin=1in'
        ]
        subprocess.run(pandoc_cmd, check=True)
        print(f"PDF created at: {output_pdf}")
        return True
    except Exception as e:
        print(f"Pandoc direct conversion failed: {e}")
        
        # Fallback to grip + pandoc
        try:
            # First render as HTML
            html_output = f"{temp_dir}/{os.path.basename(md_file)}.html"
            subprocess.run(['grip', processed_md, '--export', html_output], check=True)
            
            # Then convert HTML to PDF
            pandoc_html_cmd = [
                'pandoc',
                html_output,
                '-o', output_pdf,
                '--pdf-engine=xelatex',
                '-V', 'geometry:margin=1in'
            ]
            subprocess.run(pandoc_html_cmd, check=True)
            print(f"PDF created with grip+pandoc at: {output_pdf}")
            return True
        except Exception as e2:
            print(f"All conversion methods failed: {e2}")
            return False

# Create pdfs directory if it doesn't exist
os.makedirs("pdfs", exist_ok=True)

# Files to convert
files_to_convert = [
    ("README.md", "pdfs/README.pdf"),
    ("docs/project_report.md", "pdfs/project_report.pdf"),
    ("hardware_design/circuit_implementation.md", "pdfs/circuit_implementation.pdf")
]

# Convert each file
results = []
for md_file, output_pdf in files_to_convert:
    if os.path.exists(md_file):
        success = convert_md_to_pdf(md_file, output_pdf)
        results.append((md_file, success))
    else:
        print(f"Error: File not found - {md_file}")
        results.append((md_file, False))

# Print summary
print("\nConversion Summary:")
for md_file, success in results:
    status = "Success" if success else "Failed"
    print(f"{md_file}: {status}")

print("\nPDFs in output directory:")
for f in os.listdir("pdfs"):
    if f.endswith(".pdf"):
        pdf_path = os.path.join("pdfs", f)
        file_size = os.path.getsize(pdf_path) / 1024  # in KB
        print(f"{f} ({file_size:.1f} KB)") 