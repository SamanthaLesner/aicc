import cv2
import numpy as np
from PIL import Image

def save_contours(image_path, output_folder):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding to get binary image
    _, binary = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process each contour
    for i, contour in enumerate(contours):
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Check if the size of the bounding box is at least 100x100
        if w < 100 or h < 100:
            continue

        if w == image.shape[1] or h == image.shape[0]:
            continue

        # Create a mask for each contour
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [contour], -1, (255), thickness=cv2.FILLED)

        # Use the mask to extract the contour
        result = cv2.bitwise_and(image, image, mask=mask)

        # Crop the result using the bounding box
        cropped_image = result[y:y+h, x:x+w]

        # Create a white background image
        white_background = np.ones_like(cropped_image, dtype=np.uint8) * 255

        # Copy the cropped image onto the white background
        mask_cropped = mask[y:y+h, x:x+w]
        white_background[mask_cropped > 0] = cropped_image[mask_cropped > 0]

        # Convert to PIL format and save the image
        final_image = Image.fromarray(cv2.cvtColor(white_background, cv2.COLOR_BGR2RGB))
        final_image.save(f"{output_folder}/image_{i}_penguin_split3.png")

# Example usage
save_contours('/home/lenny/aicc/data/penguin.png', 'data/output_folder')
