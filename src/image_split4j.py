import cv2
import numpy as np
from PIL import Image
import sys

def save_contours(output_template):
    # Read the image from STDIN
    image_stream = sys.stdin.buffer.read()
    nparr = np.frombuffer(image_stream, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert image to grayscale and apply threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    most_common_pixel_value = np.argmax(np.bincount(gray.flatten()))
    threshold_value = int(0.90 * most_common_pixel_value)

    _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY_INV)

    # Remove lines narrower than 8 pixels
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        if w < 100 or h < 100 or w == image.shape[1] or h == image.shape[0]:
            continue

        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [contour], -1, (255), thickness=cv2.FILLED)
        result = cv2.bitwise_and(image, image, mask=mask)
        cropped_image = result[y:y+h, x:x+w]

        white_background = np.ones_like(cropped_image, dtype=np.uint8) * 255
        mask_cropped = mask[y:y+h, x:x+w]
        white_background[mask_cropped > 0] = cropped_image[mask_cropped > 0]

        final_image = Image.fromarray(cv2.cvtColor(white_background, cv2.COLOR_BGR2RGB))
        final_image.save(f"{output_template}_cview_{i}.png")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an output file name template.")
    else:
        output_template = sys.argv[1]
        save_contours(output_template)
