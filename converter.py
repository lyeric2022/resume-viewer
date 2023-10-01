import fitz

def convert_pdf_to_png(pdf_path, output_png_path, dpi=300):
    pdf_document = fitz.open(pdf_path)
    page = pdf_document.load_page(0)  # Load the first page (index 0)
    
    # Adjust the DPI for higher quality (e.g., 300 DPI)
    image = page.get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72))

    # Save the pixmap as a PNG file
    image.save(output_png_path)

    # Close the PDF document
    pdf_document.close()

# Example usage
input_pdf_path = 'input2_example.pdf'  # Path to the input PDF file
output_png_path = 'output.png'  # Path to save the output PNG file

convert_pdf_to_png(input_pdf_path, output_png_path, dpi=300)
