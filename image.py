# opencv 
import cv2
import numpy as np

def imageSearch(img1 = None, img2 = None):
    if not img1 or not img2:
        return 'images cannot be empty'
    
    method = cv2.TM_SQDIFF_NORMED
    # Read the images from the file
    large_image = cv2.imread(img1)
    small_image = cv2.imread(img2)
    result = cv2.matchTemplate(large_image, small_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = large_image.shape[:2]

    # Step 3: Draw the rectangle on small_image
    # cv2.rectangle(small_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),1)
    # Display the original image with the rectangle around the match.
    # cv2.imshow('output',small_image)
    # The image is only displayed if we call this
    cv2.waitKey(0)

    position = dict(
        x = MPx + 15,
        y = MPy + 30 + 10
    )

    return position

def hasImageReturnCoor(img1 = None, img2 = None):
    if not img1 or not img2:
        return 'images cannot be empty'
    
    ana_gorsel = cv2.imread(img1)
    alt_gorsel = cv2.imread(img2)

    sonuc = cv2.matchTemplate(ana_gorsel, alt_gorsel, cv2.TM_CCOEFF_NORMED)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(sonuc)
    MPx,MPy = mnLoc

    threshold = 0.95
    yerler = np.where(sonuc >= threshold)
    smallImageFind = False

    print(yerler)

    for pt in zip(*yerler[::-1]):
        smallImageFind = True
        # cv2.rectangle(ana_gorsel, pt, (pt[0] + alt_gorsel.shape[1], pt[1] + alt_gorsel.shape[0]), (0, 255, 0), 2)

    if smallImageFind:
        position = dict(
        x = MPx + 15,
        y = MPy + 30 + 10 )
        return position
    else:
        return False