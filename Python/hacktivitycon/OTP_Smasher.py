from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cv2 
import pytesseract
import time
import os
from PIL import Image
import tesserocr
import subprocess as sp

driver = webdriver.Firefox()
driver.get("http://challenge.ctf.games:31014")

def pega():
	driver.find_element_by_xpath("/html/body/img[1]").screenshot('screenshot.png')
	text = os.system('tesseract screenshot.png otp nobatch digits -c tessedit_char_whitelist=0123456789 2>/dev/null')
	with open('otp.txt', 'r') as f:
		text = f.readlines()
		new = text[0]

	
	img = cv2.imread('screenshot.png')
	# If your image is not already grayscale :
	# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	threshold = 180 # to be determined
	_, img_binarized = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
	pil_img = Image.fromarray(img_binarized)
	ocr_result = pytesseract.image_to_string(pil_img)
	new2 = ocr_result.replace('\x0c', '')


	return new, new2


while 1:
	numeros_te, numeros_py = pega()


	print('resultado tesserocr:')
	print(numeros_te)

	print('\nresultado pytesseract:')
	print(numeros_py)
	print('='*30)
	box = driver.find_element_by_xpath('/html/body/form/input[1]')
	if len(numeros_te) <= 8:

		aws = box.send_keys(numeros_py)
	else:
		aws2 = box.send_keys(numeros_te)
	#time.sleep(2)
	send = driver.find_element_by_xpath('/html/body/form/input[2]').click()
	time.sleep(0.5)