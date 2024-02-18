from google.oauth2.service_account import Credentials
from google.cloud import vision_v1
import json
import base64
import numpy as np
import cv2
import fitz

class DocumentOcr:

    def __init__(self, credentials_string):
        credentials_dict = json.loads(credentials_string)
        credentials = Credentials.from_service_account_info(credentials_dict)
        self.client = vision_v1.ImageAnnotatorClient(credentials = credentials)
    
    def detect_text(self, document):
        doc = fitz.open("pdf", document)
        try:
            # Extract text from each page
            text = ''
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                text += page.get_text()
            
            if not text:
                text = ''
                for page_num in range(doc.page_count):
                    page = doc.load_page(page_num)
                    # Convert each page to an image
                    pix = page.get_pixmap()
                    image = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, -1))
    
                    _, image_bytes = cv2.imencode('.png', image)
                    image = vision_v1.types.Image(content=image_bytes.tobytes())
                    response = self.client.text_detection(image=image)
                    texts = response.text_annotations
                    page_text = texts[0].description
                    text += page_text
            
            return text
    
        except Exception as e:
            print(f"Error: {e}")
            return ''
