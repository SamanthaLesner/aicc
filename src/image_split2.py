import cv2
import numpy as np
from PIL import Image

def save_contours(image_path, output_folder):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding to get binary image
    _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process each contour
    for i, contour in enumerate(contours):
        # Create a mask for each contour
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [contour], -1, (255), thickness=cv2.FILLED)

        # Use the mask to extract the contour
        result = cv2.bitwise_and(image, image, mask=mask)
        
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Crop the result using the bounding box
        cropped_image = result[y:y+h, x:x+w]

        # Convert to PIL format and save the image
        cropped_pil = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
        cropped_pil.save(f"{output_folder}/image_{i}.png")

# Example usage
save_contours('/home/lenny/aicc/data/girl.jpg', 'data/output_folder2')
