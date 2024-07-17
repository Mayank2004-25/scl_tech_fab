import cv2
import pytesseract

# If Tesseract is not in your PATH, include the following line with the correct path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

# Read the image (ensure the path is correct and doesn't use 'r:')
img = cv2.imread(r"D:\OCR_Python\img 1.png")

# Get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)

# Thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Apply preprocessing functions
img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

# Perform OCR
print(ocr_core(img))
