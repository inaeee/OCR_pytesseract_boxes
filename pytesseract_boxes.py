import cv2
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

img=cv2.imread('poster_5.jpg')

pytesseract.pytesseract.tessreact_cmd=r'C:\Program Files\Tesseract-OCR'

h,w,c=img.shape
boxes=pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    b=b.split(' ')
    img=cv2.rectangle(img, (int(b[1]), h-int(b[2])), (int(b[3]), h-int(b[4])), (0,255,0), 2)

print(pytesseract.image_to_string(Image.open('poster_5.jpg'), lang='eng+kor'))
cv2.imshow('img',img)
cv2.imwrite('box\poster_5.jpg',img)
cv2.waitKey(0)
