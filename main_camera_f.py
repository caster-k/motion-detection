import subprocess
import os
from PIL import Image
import numpy as np
from pathlib import Path
import time  # Import the time module for sleep function

def copy_and_rename_pathlib(src_path, dest_path, new_name):
    # Create Path objects
    src_path = Path(src_path)
    dest_path = Path(dest_path)

    # Copy and rename the file
    new_path = dest_path / new_name
    src_path.rename(new_path)

while True:  # Use True instead of 1 for an infinite loop
    previous_path = "../../Wild_life/sak_cod/pic/previous.jpg"

    if not os.path.exists(previous_path):
        command = ["fswebcam", "-d", "/dev/video0", "../../Wild_life/sak_cod/pic/previous.jpg"]
        subprocess.call(command)

    # Define the command to capture the current image
    command = ["fswebcam", "-d", "/dev/video0", "../../Wild_life/sak_cod/pic/capture.jpg"]

    # Run the command to capture the current image using subprocess
    subprocess.call(command)

    # Function to calculate Mean Squared Error (MSE)
    def mse(image1, image2):
        err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
        err /= float(image1.shape[0] * image1.shape[1])
        return err

    # Load images
    image1_path = '../../Wild_life/sak_cod/pic/previous.jpg'
    image2_path = '../../Wild_life/sak_cod/pic/capture.jpg'

    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Convert images to numpy arrays
    img1_array = np.array(image1)
    img2_array = np.array(image2)

    # Calculate Mean Squared Error (MSE) between the two images
    mse_value = mse(img1_array, img2_array)
    print(mse_value)

    # Check if MSE value is above threshold
    if mse_value >= 5000:
        local_file = "../../Wild_life/sak_cod/pic/previous.jpg"
        remote_path = "../../Wild_life/sak_cod/pic/save"
        files = os.listdir(remote_path)

        num_of_images = len(files) + 1
        print(num_of_images)

        copy_and_rename_pathlib(local_file, remote_path, f"{num_of_images}.jpg")

    # Move the current capture.jpg to previous.jpg
    local_file = "../../Wild_life/sak_cod/pic/capture.jpg"
    remote_path = "../../Wild_life/sak_cod/pic"
    copy_and_rename_pathlib(local_file, remote_path, "previous.jpg")

    # Add a delay of 1 second before the next iteration
    time.sleep(1)
