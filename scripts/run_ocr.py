import argparse
import time
import logging

import numpy as np
from PIL import Image

# Assume we have the OCR service in a module named services.ocr_service
# Adjust this import if your folder structure is different
from services.ocr_service import ocr_service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(image_path: str):
    start_time = time.perf_counter()

    # Load image
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)

    # Inference using OCR
    text, inference_time = ocr_service._process_image_sync(image_array)

    total_time = time.perf_counter() - start_time

    logger.info(f"Result: {text}")
    logger.info(f"Inference time (model only): {inference_time:.4f}s")
    logger.info(f"Total script time: {total_time:.4f}s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run OCR on a single image for baseline testing."
    )
    parser.add_argument(
        "--image_path", 
        type=str, 
        required=True, 
        help="Path to the image file."
    )
    args = parser.parse_args()

    main(args.image_path)
