## Imports
import pyautogui
import pytesseract
import os
import cv2


## Tesseract Config
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract"


## Reader Class
class reader:
     ## Read & Process String On Screen
    def read_string(XOrig, YOrig, XSize, YSize):
        ## Capture Screenshot of Number on Screen
        ss = pyautogui.screenshot(region=(XOrig, YOrig, XSize, YSize))
        ss.save(os.path.abspath("ss.png"))

        ## Process Number using OpenCV
        img = cv2.imread("ss.png")
        img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)

        ## Apply Threshold
        HSV_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(HSV_img)
        thresh = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        ## Run Processed Image through Tesseract
        result = pytesseract.image_to_string(thresh, config="--psm 7")
        
        ## Remove Screenshot -> Return Tesseract's Result
        os.remove("ss.png")
        return (result.rstrip())


    ## Read & Process Number On Screen
    def read_num(XOrig, YOrig, XSize, YSize):
        ## Capture Screenshot of Number on Screen
        ss = pyautogui.screenshot(region=(XOrig, YOrig, XSize, YSize))
        ss.save(os.path.abspath("ss.png"))

        ## Process Number using OpenCV
        img = cv2.imread("ss.png")
        img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)

        ## Apply Threshold
        HSV_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(HSV_img)
        thresh = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        ## Run Processed Image through Tesseract
        result = pytesseract.image_to_string(thresh, config="--psm 7 digit")

        ## Hacky Fix to 7 being read as '?'
        result = result.replace("?", "7")

        ## Remove Screenshot -> Return Tesseract's Result
        os.remove("ss.png")
        return (int(''.join(filter(str.isdigit, result.strip()))))


    ## Read Pixel Colour given Position on Screen
    def read_pixel(XOrig, YOrig):
        ## Create Snapshot of Pixel -> Return Pixel Colour
        ss = pyautogui.screenshot(region=(XOrig, YOrig, 1, 1))
        return ss.getpixel((0, 0))