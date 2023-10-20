from shutil import move
import pylovepdf
from pylovepdf.ilovepdf import ILovePdf
import os



class PDFProcessor:
    """A class for processing PDF files."""

    public_key = "project_public_a0b2def94d84a4622b5322060808ca83_TK_9u4a3bb787c510af872f2798d789023a05"

    def __init__(self, output_directory):
        """Initialize the PDF processor.

        Args:
            output_directory: The output directory for processed PDF files.
        """
        self.ilovepdf = ILovePdf(public_key=self.public_key, verify_ssl=True)
        self.output_directory = output_directory

    def compress_pdf(self, pdf_file):
        """Compress a PDF file.

        Args:
            pdf_file: The path to the PDF file to compress.

        Returns:
            The path to the compressed PDF file.
        """
        task = self.ilovepdf.new_task('compress')
        task.add_file(pdf_file)
        task.set_output_folder(self.output_directory)
        task.execute()
        task.download()
        task.delete_current_task()
        return self.output_directory
    def merge_pdfs(self, pdf_file1, pdf_file2):
        """Merge two PDF files.
        Args:
            pdf_file1: The path to the first PDF file to merge.
            pdf_file2: The path to the second PDF file to merge.
        Returns:
            The path to the merged PDF file.
        """
        task = self.ilovepdf.new_task('merge')
        task.add_file(pdf_file1)
        task.add_file(pdf_file2)
        task.set_output_folder(self.output_directory)
        task.execute()
        task.download()
        task.delete_current_task()

    def split_pdf(self, input_file, output_files):
        """Split a PDF file into multiple PDF files.

        Args:
            input_file: The path to the PDF file to split.
            output_files: A list of paths to the output PDF files.
        """
        task = self.ilovepdf.new_task('split')
        task.add_file(input_file)

        for output_file in output_files:
            task.add_output_file(output_file)

        task.execute()
        task.download()

    def remove_pdf_password(self, input_file, output_file):
        """Remove the password from a PDF file.

        Args:
            input_file: The path to the PDF file to remove the password from.
            output_file: The path to the output PDF file without the password.
        """
        task = self.ilovepdf.new_task('unlock')
        task.add_file(input_file)

        task.execute()
        task.download(output_file)

    def extract_pdf_text(self, input_file, output_file):
        """Extract the text from a PDF file.

        Args:
            input_file: The path to the PDF file to extract the text from.
            output_file: The path to the output text file.
        """
        task = self.ilovepdf.new_task('text_to_pdf')
        task.add_file(input_file)

        task.execute()
        task.download(output_file)

    def convert_image_to_pdf(self, input_file, output_file):
        """Convert an image file to a PDF file.

        Args:
            input_file: The path to the image file to convert.
            output_file: The path to the output PDF file.
        """
        task = self.ilovepdf.new_task('image_to_pdf')
        task.add_file(input_file)

        task.execute()
        task.download(output_file)


def main():
    """The main function."""

    # Get the output directory from the user.
    output_directory = input("Enter the output directory: ")

    # Create a new PDF processor.
    pdf_processor = PDFProcessor(output_directory)
    # Get the user's selection.
    user_selection = input("What do you want to do with your PDF file? (compress, merge, split, remove password, extract text, or convert image to PDF): ")

    # Process the PDF file based on the user's selection.
    if user_selection == "compress":
        pdf_file = input("Enter the path to the PDF file you want to compress: ")
        compressed_pdf_file = pdf_processor.compress_pdf(pdf_file)

        print("Compressed PDF file saved to:", compressed_pdf_file)
    elif user_selection == "merge":
        pdf_file1 = input("Enter the path to the PDF file you want to merge: ") 
        pdf_file2 = input("Enter the path to the PDF file you want to merge with the first: ") 
        pdf_processor.merge_pdfs(pdf_file1, pdf_file2)

        print("Merged PDF saved to:", pdf_processor.output_directory)
    elif user_selection == "split":
        input_file = input("Enter the path to the PDF file you want to split: ")
        output_files = input("Enter the paths to the output PDF files, separated by commas: ").split(",")

        pdf_processor.split_pdf(input_file, output_files)

        print("Split PDF files saved to:", output_files)
    elif user_selection == "remove password":
        input_file = input("Enter the path to the PDF file you want to remove the password from: ")
        output_file = input("Enter the path to the output PDF file without the password: ")

        pdf_processor.remove_pdf_password(input_file, output_file)

        print("PDF file without password saved to:", output_file)
    elif user_selection == "extract text":
        input_file = input("Enter the path to the PDF file you want to extract text from: ")
        output_file = input("Enter the path to the output text file: ")

        pdf_processor.extract_pdf_text(input_file, output_file)

        print("Text extracted from PDF file and saved to:", output_file)
    elif user_selection == "convert image to PDF":
        input_file = input("Enter the path to the image file you want to convert to PDF: ")
        output_file = input("Enter the path to the output PDF file: ")

        pdf_processor.convert_image_to_pdf(input_file, output_file)

        print("Image file converted to PDF and saved to:", output_file)
    else:
        print("Invalid selection.")


if __name__ == "__main__":
    main()
