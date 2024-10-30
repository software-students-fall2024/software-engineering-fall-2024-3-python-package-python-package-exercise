import tamagotchi.tamagotchi as t
from PIL import Image

def main():
    # Convert an image to ASCII art
    image_path = "src/tamagotchi/input_image.png"  # Make sure this path points to your image
    print("\n--- ASCII Art of the Image ---")
    t.get_ascii_art(image_path, scale=0.1, character_map=t.G_SCALE_1)

    t.getpet(1)
    print('1----')
    t.getpet(2)
    print('2----')
    t.getpet(3)
    print('3----')

if __name__ == "__main__":
    main()