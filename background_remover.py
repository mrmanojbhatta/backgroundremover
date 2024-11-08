from rembg import remove
from PIL import Image, UnidentifiedImageError
from tkinter import Tk, filedialog
import io
import os

# Supported input formats
SUPPORTED_FORMATS = ('.png', '.jpg', '.jpeg', '.gif', '.tiff', '.svg', '.webp', '.bmp')

def select_file():
    # Open a file dialog to select an input file
    Tk().withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.tiff *.svg *.webp *.bmp")]
    )
    return file_path

def select_save_location():
    # Open a file dialog to select the save location and output filename
    Tk().withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(
        title="Save Output Image",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
    )
    return file_path

def remove_background(input_path, output_path, output_format="png"):
    try:
        # Verify the input file format
        if not input_path.lower().endswith(SUPPORTED_FORMATS):
            print(f"Error: Unsupported file format. Please use one of {SUPPORTED_FORMATS}.")
            return

        # Open the input image and convert it to RGBA (transparency support)
        with Image.open(input_path) as img:
            img = img.convert("RGBA")

            # Save the image to bytes for rembg processing
            img_byte_array = io.BytesIO()
            img.save(img_byte_array, format="PNG")
            img_data = img_byte_array.getvalue()

        # Remove the background
        output_data = remove(img_data)

        # Convert output to PNG or JPG based on user preference
        if output_format == "jpg":
            # Convert bytes back to Image and add a white background for JPG
            output_image = Image.open(io.BytesIO(output_data)).convert("RGB")
            with open(output_path, 'wb') as output_file:
                output_image.save(output_file, format="JPEG")
        else:
            # Save as PNG with transparency
            with open(output_path, 'wb') as output_file:
                output_file.write(output_data)

        print(f"Background removed successfully! Check '{output_path}' for the result.")

    except UnidentifiedImageError:
        print("Error: Could not identify the image file format.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to prompt user for file paths and format
if __name__ == "__main__":
    # Select the input file
    input_path = select_file()
    if not input_path:
        print("No file selected. Exiting program.")
        exit()

    # Select the output file location and name
    output_path = select_save_location()
    if not output_path:
        print("No save location selected. Exiting program.")
        exit()

    # Ask for output format preference
    output_format = output_path.split('.')[-1].lower()
    if output_format not in ["png", "jpg"]:
        print("Invalid format. Defaulting to PNG.")
        output_format = "png"

    # Call the background removal function
    remove_background(input_path, output_path, output_format)
