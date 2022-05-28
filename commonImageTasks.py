# ========= common functions ========================
# FuUnctions used by all routines
from PIL import Image
import os

DEBUG = 0

def getImg(imname, impath):
    "get the 'ref' image"
    imloc = "{}{}".format(impath, imname)
    refimg = Image.open("{}".format(imloc))
    return refimg

def combineImgs(limg, rimg):
    """combine R+L images into single stereo image
    Lume Pad pairs are L|R (parallel stereo)
    """
    if DEBUG: print(f"combining left and right images...")
    width, height = rimg.size
    new_width = width * 2
    new_height = height
    new_im = Image.new('RGB', (new_width, height))
    x_offset = 0
    new_im.paste(limg, (x_offset, 0))
    x_offset += width
    new_im.paste(rimg, (x_offset, 0))
    # new_im.show()
    return new_im
#test: combineImgs(limg, rimg).show()

def flipStereoImage(stereoImg):
    "flip the order of the stereo pair"
    lftimg, rhtimg = splitLRImage(stereoImg)
    new_img = combineImgs(rhtimg, lftimg)
    return new_img

def splitLRImage(img):
    "split and resize AiptekLR stereo image"
    # split image: ex. im1 = im.crop((left, top, right, bottom)):
    if DEBUG: print(f"splitting image into left and right parts...")
    imgformat, imgsize, imgmode = (img.format, img.size, img.mode)
    wide, high = imgsize
    lftimg = img.crop((0, 0, int(wide / 2), high))
    rhtimg = img.crop((int(wide / 2), 0, wide, high))
    return (lftimg, rhtimg)
#test: img = load(AIPTEKPATH+"//"+'PICT0007.jpg"; limg,rimg = splitLRImage(img); rimg.show(); limg.show()

def ShowImage(image):
    "display submitted image"
    image.show()
    return

def saveImage(imgname, stereoimg, imgpath, ext = 'jpg'):
    "save '.2x1' formated image to file"
    if DEBUG: print(f"saving image '{imgname}' to file...")
    newpath = imgpath
    newname = f"{imgname[:-4]}_2X1.{ext}"
    print(f"{newpath}{newname}")
    stereoimg.save(f"{newpath}{newname}")
    return (newpath, newname)

def listImages(imglst, cols = 6):
    "list the available images to choose from"
    item = 1
    while imglst:
        print(imglst.pop(0), "\t", end=''),
        try:
            if (item % cols == 0):
                print()
        except ZeroDivisionError:
            print(len(aiptekfiles), "%", cols)
        item += 1

