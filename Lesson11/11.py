import cv2
from PIL import Image

image_path = 'Thinking-of-getting-a-cat.png'
image = cv2.imread(image_path)
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
#cat_face_cascade2 = cv2.CascadeClassifier('haarcascade_eye.xml')
cat_face = cat_face_cascade.detectMultiScale(image)
#cat_face = cat_face_cascade2.detectMultiScale(image)

cat = Image.open(image_path)
floor = Image.open('pngegg.png')
glasses = Image.open('MicrosoftTeams-image.png')
floor = floor.convert("RGBA")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
print(cat_face)
for (x, y, w, h) in cat_face:
    #cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,255), 3)
    glasses = glasses.resize((w, int(h/3)))
    floor = floor.resize((w, int(h/3)))
    cat.paste( floor, (x, int(y + h/2)), floor)
    cat.paste(glasses, (x, int(y + h / 4)), glasses)
    cat.save("newCat.png")
    cat_with_glasses = cv2.imread("newCat.png")
    cv2.imshow("Cat", cat_with_glasses)
    cv2.waitKey()
