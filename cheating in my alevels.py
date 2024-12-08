from docx import Document

def word_to_hidscript(docx_path, output_path):
    """
    Transforms a Word document into an HIDScript.
    
    :param docx_path: Path to the input Word document.
    :param output_path: Path to save the HIDScript file.
    """
    # Load the Word document
    doc = Document(docx_path)
    
    # Start building the HIDScript
    hidscript = []
    hidscript.append('// Set typing speed (0ms delay for fastest typing)')
    hidscript.append('typingSpeed(0, 0);')
    hidscript.append('layout("gb");\n')
    
    # Iterate over paragraphs in the document
    hidscript.append('// Type the text')
    hidscript.append('type("')
    
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():  # Skip empty paragraphs
            # Escape special characters in the text
            text = paragraph.text.replace('"', '\\"').replace('\\', '\\\\').replace('\n', '\\n')
            hidscript.append(f"{text}\\n\\n")
    
    hidscript.append('");\n')  # Close the `type` command
    
    # Save the HIDScript to a file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(hidscript))
    
    print(f"HIDScript saved to {output_path}")

# Example usage
word_to_hidscript(r'C:\Users\ethan\Documents\Nea answers.docx', 'output_hidscript.txt')
