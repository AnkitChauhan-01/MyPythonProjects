'''THIS PROGRAM CONVERTS IMAGES TO PDFS'''

import os
import img2pdf

def func1(x,y):
    input_folder = x

    # Output PDF filename WITH SPECIFIED PATH
    output_pdf = y
    image_files = [file for file in os.listdir(input_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

    sorted_image_files = sorted( image_files, key=lambda x : int(x.split('(')[1].split(')')[0]) )

    # Create a PDF from the sorted image files
    pdf_bytes = img2pdf.convert([os.path.join(input_folder, image) for image in sorted_image_files])

    # Write the PDF bytes to the output PDF file
    with open(output_pdf, 'wb') as pdf_file:
        pdf_file.write(pdf_bytes)

    # print(f"Images converted and saved to {output_pdf}")
    print("PDF Created Successfully!!")


# Function call zone:
func1("D:\PYTHON\RECURSION\SCREENSHOTS","D:\PYTHON\RECURSION\SCREENSHOTS\L1.pdf")
