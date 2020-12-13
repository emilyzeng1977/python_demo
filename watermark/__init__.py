from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    # drawing.text(pos, text, fill=black)
    photo.show()
    photo.save(output_image_path)


def watermark_photo(input_image_path,
                    output_image_path,
                    watermark_image_path,
                    position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    # add watermark to your image
    base_image.paste(watermark, position)
    base_image.show()
    base_image.save(output_image_path)


if __name__ == '__main__':
    img = 'FangchenNiu.jpg'
    watermark_photo(img, 'FangchenNiu_watermarked.jpg',
                    'MARKET.jpg', position=(0, 0))

# if __name__ == '__main__':
#     img = 'FangchenNiu.jpg'
#     watermark_text(img, 'FangchenNiu_watermarked.jpg',
#                    text='DigiHealth',
#                    pos=(0, 0))
