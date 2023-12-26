import os
import subprocess

def upscale_images(input_folder, output_folder, realesrgan_path):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all PNG files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".png"):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name.replace(".png", "_rgan_win2.png"))

            # Construct the command
            command = [
                realesrgan_path,
                "-i", input_file,
                "-o", output_file,
                "-n", "realesrgan-x4plus-anime"
            ]

            # Run the command
            subprocess.run(command, check=True)

# Usage
input_folder = 'data/output_folder3'
output_folder = 'data/upscaled_output_folder3'
realesrgan_path = 'deps/realesrgan-ncnn-vulkan-20220424-windows/realesrgan-ncnn-vulkan.exe'

upscale_images(input_folder, output_folder, realesrgan_path)
