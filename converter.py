from PIL import Image

def convert_jpg_to_png(input_path, output_path):
    try:
        # Open the input JPG image
        with Image.open(input_path) as img:
            # Convert and save as a PNG image
            img.save(output_path, 'PNG')
        print(f"Conversion successful. Saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_path = "input_example.jpg"  # Change this to the path of your JPG image
    output_path = "output.png"  # Change this to the desired output PNG file path
    convert_jpg_to_png(input_path, output_path)
