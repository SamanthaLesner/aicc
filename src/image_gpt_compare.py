import openai
import base64

def encode_image_to_base64(filepath):
    with open(filepath, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def compare_images(image1_path, image2_path, openai_api_key):
    # Encode images to base64
    image1_base64 = encode_image_to_base64(image1_path)
    image2_base64 = encode_image_to_base64(image2_path)

    # Set up OpenAI API key
    openai.api_key = openai_api_key

    # Prepare the prompt
    prompt = f"Are these images of the same person? Image 1: {image1_base64}, Image 2: {image2_base64}"

    # Call the OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",  # Replace with the latest available model
        prompt=prompt,
        max_tokens=100
    )

    return response.choices[0].text.strip()

# Use the function with your images and API key
api_key = 'your-openai-api-key'
result = compare_images('path/to/a.png', 'path/to/b.png', api_key)
print(result)
