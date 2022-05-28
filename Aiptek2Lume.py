## ================= Aiptek 3D images conversion =====================
## convert Aiptek 3D camera side-by-side images to '.2X1' side by side format
from commonImageTasks import *

# Aiptek 3D file info:
AIPTEKPATH = "E:\\100DIR3D\\"
AIPTEKOUT = "C:\\Users\\hdemb\\Desktop\\MediaContent\\converted3DPhotos\\"

def Aiptek2Lume(imgname, impath=AIPTEKPATH):
    "convert Aiptek image for Lume Pad use"
    # correct imgname for '.jpg' extension:
    if len(imgname.split('.')) != 2:
        imgname = imgname + ".jpg"
    name, ext = imgname.split('.')
    imloc = "{}{}".format(impath, imgname)
    # open the image:
    if DEBUG: print(f"opening image '{imgname}' from {imloc}'...")
    try:
        orig_img = Image.open("{}".format(imloc))
    except IOError:
        print("File Not Found! Aborting!")
        exit()
    # origimg.show()
    # get image parameters to use for conversion:
    wide, high = orig_img.size
    # split the stereo image:
    left_img, rght_img = splitLRImage(orig_img)
    if DEBUG: print(f"resizing left and right images...")
    # left_img = left_img.resize((wide, high))
    # right_img = rght_img.resize((wide, high))
    stereoimg = combineImgs(left_img.resize((wide, high)), rght_img.resize((wide, high)))
    return stereoimg
#test: Aiptek2Lume('PICT0027').show()

def doAiptek(imname, impath=AIPTEKPATH):
    "process an Aiptek stereo image"
    imloc = "{}{}".format(impath, imname)
    print(f"photo '{imname}' is located at '{imloc}'")
    try:
        stereoimg = Aiptek2Lume(imname, impath)
    except IOError:
        print("File Not Found: Aborted!!!")
        exit()
    return stereoimg


if __name__ == '__main__':
    "run the code"
    imglst = os.listdir(AIPTEKPATH)
    listImages(imglst)
    print()
    image = input("Enter the Aiptek 3D image that you want to convert to Lume Pad '.2xPICT1' format: ")
    # image = "PICT0026.jpg"
    new_image = doAiptek(image)
    new_image.show()
    while True:
        ans = input("flip it?: ")
        if ans in ['y','Y']:
            new_image = flipStereoImage(new_image)
            new_image.show()
        else:
            break
    if input("save the new stereo image?: ") in ('y', 'Y'):
        print(f"Image saved at:")
        saveImage(image, new_image, AIPTEKOUT)