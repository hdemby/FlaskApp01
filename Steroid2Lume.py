## ================= 3D Steroid images conversion =====================
## convert Android 3DSteroid app side-by-side images to '.2X1' side by side format
# 3D Steroid file info:
from commonImageTasks import *

STEROIDPATH = "C:\\Users\\hdemb\\Desktop\\MediaContent\\Saminine\\Phone\\3DSteroidPro\\Camera_org\\"
STEROIDOUT = "C:\\Users\\hdemb\\Desktop\\MediaContent\\converted3DPhotos\\"

def getPairTxt(refname, impath = STEROIDPATH):
    "return the text file for the refimg"
    imfile = refname
    txtloc = "{}{}".format(impath, imfile)
    pairtxt =open(txtloc,'r').readlines()
    return pairtxt

def getPriname(txtname):
    "extract the primary image name from the txt file name"
    priname = txtname[:-4]
    return priname

def getSecName(pairtxt):
    "return the paired image"
    print(pairtxt)
    secname = (pairtxt[0]).split(",")[0].split("/")[-1]
    return secname


def doSteroid(pairtxtfile, impath=STEROIDPATH):
    """process a 3D Steroid image pair into Lume Pad '.2x1' format"""
    assert(pairtxtfile[-4:] == '.txt')
     # get the pair text file:
    try:
        pairtxt = getPairTxt(pairtxtfile, impath)
        print(pairtxt)
    except IOError:
        print("File Not Found! Aborting")
        exit()
    # get the refernce image name:
    imgname = pairtxtfile[:-4]
     # get the companion image name exist:
    secname = getSecName(pairtxt)
    print(imgname, secname)
    # verify the reference image exist:
    try:
        refimg = getImg(imgname, impath)
    except IOError:
        print("File Not Found! Aborting")
        exit()
    # get the companion image if it exist:
    try:
        secimg = getImg(secname, impath)
    except IOError:
        print("File Not Found! Aborting")
        exit()
    #refimg.show()
    #secimg.show()
    # convert images to '_2x1' format:
    new_image = combineImgs(secimg, refimg)
    return new_image

if __name__ == '__main__':
    "run the code"
    imagetxtlst = [fil for fil in os.listdir(STEROIDPATH) if fil[-4:] == '.txt']
    listImages(imagetxtlst)
    reftxt = input("Enter the reference txt file for the 3D Steroid image that you want to convert to '.2x1' format: ")
    # refimg = '20210417_130158.jpg'
    new_image = doSteroid(reftxt)
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
        saveImage(reftxt[:-4], new_image, STEROIDOUT)
    else:
        print("Image not saved")

## sample: doSteroid('20210405_114846.jpg')
