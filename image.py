from PIL import Image, ImageEnhance

for x in range(15):
    # Load the image
    image = Image.open("Sprites_all/grass_2.png")

    # Create an ImageEnhance object and darken the image
    enhancer = ImageEnhance.Brightness(image)
    darkened_image = enhancer.enhance((x+1)*(1/15)) # range from 0 (black) to 1 (original image)

    # Save the darkened image
    darkened_image.save(f"Sprites_all/grass_2-{x}.png")