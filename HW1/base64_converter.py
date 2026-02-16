import base64
import os

def convert_base64_to_png(input_file_path, output_file_path):
    """
    Reads a text file containing a base64 string and converts it to a PNG image.
    """
    try:
        # Read the base64 string from the text file
        with open(input_file_path, "r") as text_file:
            base64_string = text_file.read().strip()

        # Check for and remove the header if present
        if "," in base64_string:
            print("Header found. stripping header...")
            base64_string = base64_string.split(",")[1]

        # Decode the base64 string into bytes
        image_data = base64.b64decode(base64_string)

        # Write the bytes to the output PNG file
        with open(output_file_path, "wb") as image_file:
            image_file.write(image_data)

        print(f"Success! Image saved to: {output_file_path}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    except base64.binascii.Error:
        print("Error: The file content is not valid base64.")
    except Exception as e:
        print(f"Chill out, this is just a little script for a homework, not for QA engineer job interview! {e}")

def main():    
    # Configure directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Join that directory with filenames
    input_txt = os.path.join(script_dir, "screenshot.txt")
    output_png = os.path.join(script_dir, "screenshot.png")
    
    # Run the conversion
    convert_base64_to_png(input_txt, output_png)

if __name__ == "__main__":
    main()
