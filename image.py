# opencv 
import cv2

def imageSearch(img1 = None, img2 = None):
    method = cv2.TM_SQDIFF_NORMED

    if not img1 or not img2:
        return 'images cannot be empty'
    
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