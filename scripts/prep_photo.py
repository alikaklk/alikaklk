import cv2
import numpy as np
from rembg import remove
from PIL import Image
import sys

if len(sys.argv) < 2:
    print("Kullanım: python scripts/prep_photo.py <fotograf_yolu>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = "source-prepped.png"

input_image = Image.open(input_path)
output_image = remove(input_image)

background = Image.new("RGBA", output_image.size, (255, 255, 255, 255))
alpha_composite = Image.alpha_composite(background, output_image).convert("L")

np_img = np.array(alpha_composite)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl_img = clahe.apply(np_img)

cv2.imwrite(output_path, cl_img)
print(f"Hazırlanan görsel kaydedildi: {output_path}")
