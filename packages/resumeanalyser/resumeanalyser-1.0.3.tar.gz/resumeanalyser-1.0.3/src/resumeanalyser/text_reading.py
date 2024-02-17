# Imports
import os
from docx import Document
from pypdf import PdfReader

def docx_to_text(filepath):
    """
    Basic function to extract text from a Word document, given a specified file path.

    Parameters:
    filepath (str): A string containing the filepath.

    Returns:
    text (str): A string containing the extracted text.

    Example:
    >>> pdf_to_text('~/alphabet.docx')
    'abcdefghijklmnopqrstuvwxyz'
    """
    # Check that file path ends with docx
    if not filepath.lower().endswith('.docx'):
        raise ValueError("Please provide a .docx file. Consider the other functions if you want to use different file formats.")
    try:
        with open(filepath, 'rb') as f:
            document = Document(filepath)
            full_text = []
            for paragraph in document.paragraphs:
                full_text.append(paragraph.text)
                text = str(' '.join(full_text))
            return text
    except Exception as e:
        print('File reading error.')

def pdf_to_text(filepath):
    """
    Basic function to extract text from a PDF file, given a specified file path.

    Parameters:
    filepath (str): A string containing the filepath.

    Returns:
    text (str): A string containing the extracted text.

    Example:
    >>> pdf_to_text('~/alphabet.pdf')
    'abcdefghijklmnopqrstuvwxyz'
    """
    if not filepath.lower().endswith('.pdf'):
        raise ValueError("Please provide a .PDF file. Consider the other functions if you want to use different file formats.")
    try:
        with open(filepath, 'rb') as f:
            reader = PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + " "
            # Stripping whitespace
            text = text.strip()
            return text
    except Exception as e:
        print('File reading error.')

# Website text extraction has not been implemented yet
# def website_to_text(url):
#     """
#     Basic function to extract text from a website, given a URL.

#     Parameters:
#     url (str): A string containing the filepath.

#     Returns:
#     text (str): A string containing the extracted text.

#     Example:
#     >>> website_to_text('www.alphabet.com')
#     'abcdefghijklmnopqrstuvwxyz'
#     """

#     return text

