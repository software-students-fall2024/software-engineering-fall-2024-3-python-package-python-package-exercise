import os
from PIL import Image
# create your own tamagotchi

G_SCALE_1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
G_SCALE_2 = '@%#*+=-:. '

def get_ascii_art(image_path, scale=0.1, character_map=G_SCALE_1):
    """Converts an image to ASCII art using the specified character map."""
    try:
        # Open the image
        image = Image.open(image_path)

        # Convert to grayscale
        image = image.convert("L")

        # Resize the image to make it suitable for ASCII art
        width, height = image.size
        aspect_ratio = height / width
        new_width = int(width * scale)
        new_height = int(new_width * aspect_ratio * 0.55)  # Adjust for character aspect ratio
        image = image.resize((new_width, new_height))

        # Generate ASCII art
        ascii_art = ""
        for y in range(new_height):
            for x in range(new_width):
                gray_value = image.getpixel((x, y))
                ascii_char = character_map[int((gray_value / 255) * (len(character_map) - 1))]
                ascii_art += ascii_char
            ascii_art += "\n"
        
        print(ascii_art)  # Print the ASCII art to the console
        return ascii_art

    except FileNotFoundError:
        print(f"Image file '{image_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def getpet(number):
    """Returns the pet associated with the number input"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, f'tama-{number}.txt')
    try:
        with open(filename, 'r') as f:
            pet = f.read()
            print(pet) 
            return pet
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

