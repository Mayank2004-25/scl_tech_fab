try:
    import pytesseract
    from PIL import Image
    print("Libraries imported successfully.")
except ImportError as e:
    print("Error importing libraries: ", e)

# Replace 'test_image.png' with the path to your test image
image_path = 'img 1.png'

try:
    # Open an image file
    with Image.open(image_path) as img:
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
        print("OCR Result:")
        print(text)
except Exception as e:
    print("Error processing image: ", e)
