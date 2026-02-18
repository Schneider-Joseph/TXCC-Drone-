import sys
sys.path.insert(1, '/home/tunxis001/my_project/lib/python3.13/site-packages')
import cv2
import imutils
from imutils import paths
import glob


def stitch_images(images):
    """
    Stitches a list of images into a panorama using OpenCV's Stitcher class.
    """
    # Initialize the Stitcher
    stitcher = cv2.Stitcher_create()
    
    # Stitch the images
    status, stitched = stitcher.stitch(images)
    
    if status == cv2.Stitcher_OK:
        print("[INFO] Image stitching successful.")
        # You may want to crop the black edges
        # stitched = cv2.detail_PostProcessor().process(stitched) # Advanced post-processing
        return stitched
    elif status == cv2.Stitcher_ERR_NEED_MORE_IMGS:
        print("[INFO] Image stitching failed: Need more images or not enough overlap.")
    elif status == cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
        print("[INFO] Image stitching failed: Homography estimation failed.")
    else:
        print("[INFO] Image stitching failed: Unknown error.")
    
    return None

# Perform the stitching
image_paths = glob.glob("/home/tunxis001/pi/*.jpg")
images_to_stitch = [cv2.imread(img) for img in image_paths]
stitched_image = stitch_images(images_to_stitch)

