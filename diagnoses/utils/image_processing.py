
import cv2
import numpy as np
from io import BytesIO

def preprocess_image(uploaded_file, target_size=(224, 224)):
    """
    Preprocess the uploaded image to match the model input using OpenCV. Resize and normalize the image.
    :param uploaded_file: The uploaded file object from web.
    :param target_size: The target size corresponding to the model input.
    :return: The image in the form of a numpy array ready to be used for prediction.
    """
    
    # Read the uploaded file into a BytesIO object
    file_bytes = BytesIO(uploaded_file)
    
    # Convert BytesIO to numpy array
    file_bytes = np.asarray(bytearray(file_bytes.read()), dtype=np.uint8)
    
    # Read the image using OpenCV
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Resize the image
    img = cv2.resize(img, target_size)
    
    # Normalize the image (assuming values should be between 0 and 1)
    img = img.astype(np.float32)
    
    # Add batch dimension
    img_array = np.expand_dims(img, axis=0)
    
    return img_array
