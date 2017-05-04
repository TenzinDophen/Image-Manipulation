"""images.py
    written by: Liam Sullivan and Tenzin Dophen, 2017-2-22
    Adapted from a program written by: Jed Yang, 2016-10-25
"""

import sys
from PIL import Image

################################################################################
##  Sample Functions  ##  Everything you need is demonstrated here.  ###########
################################################################################

def getRedImage(originalImage):
    """Returns a copy of originalImage where green and blue are removed. 
       This function demonstrates how to 
       - make a copy of the image given (so we don't muck it up),
       - load the pixels into a variable (so we can manipulate them),
       - loop through all pixels, and
       - set all the green and blue values to 0 (so only red parts remain).
    """

    # make a copy so we don't affect the original image
    redImage = originalImage.copy()

    width = redImage.width
    height = redImage.height

    # loads the pixels so we can manipulate them
    px = redImage.load()

    # loop through all the pixels
    for x in range(width):
        for y in range(height):
            redValue = px[x,y][0]
            # retains the R of RGB value but nukes G and B to 0
            px[x,y] = (redValue, 0, 0)

    return redImage


def getSmallImage(originalImage):
    """Returns a smaller copy of originalImage
    """

    size = originalImage.size
    #adjust the width and height to half the orignal size
    newWidth = size[0] // 2
    newHeight = size[1] // 2

    # create a new image with different dimensions
    scaledImage = Image.new("RGB", (newWidth, newHeight))

    # loads the pixels so we can manipulate them
    pxOriginal = originalImage.load()
    pxScaled = scaledImage.load()

    for x in range(newWidth):
        for y in range(newHeight):
            pxScaled[x,y] = pxOriginal[2*x, 2*y]

    return scaledImage


################################################################################
##  Basic Image Manipulations  ##  Implement these functions.  #################
################################################################################

def getGrayImage(originalImage):
    grayImage = originalImage.copy()

    width = grayImage.width
    height = grayImage.height
    #loads each individual pixel
    px = grayImage.load()

    # loop through all the pixels
    for x in range(width):
        for y in range(height):
            grayValue = px[x,y][1]
            # retains a single color value, then sets each value equal to grayValue, 
            #rendering the image gray
            px[x,y] = (grayValue, grayValue, grayValue)
    
    return grayImage


def getNegativeImage(originalImage):
    """Returns a copy of originalImage converted to "negative" form (like a
       photographic negative)
    """
    negativeImage = originalImage.copy()

    width = negativeImage.width
    height = negativeImage.height
    px = negativeImage.load()

    # loop through all the pixels
    for x in range(width):
        for y in range(height):
            redValue = px[x, y][0]
            greenValue = px[x,y][1]
            blueValue = px[x, y][2]
            #sets all the color value to the opposite value, by subtracting the original value
            #from the maximum color value of 255
            px[x,y] = (255-redValue, 255-greenValue, 255-blueValue)
    
    return negativeImage


def getMirrorImage(originalImage):
    """Returns a copy of originalImage, mirrored."""
    mirroredImage = originalImage.copy()
    
    width = mirroredImage.width
    height = mirroredImage.height
    
    gx = originalImage.load()
    px = mirroredImage.load()
    
    # loop through all the pixels
    for y in range(height):
        for x in range(width):
            # only exchanges the pixels in the x direction(width) from one side to the other side
            # of the image, without changing the y values. 
            px[x,y] = gx[x,y]
            gx[x,y]= gx[width - x-1, y]
            # added -1 to avoid index out of bounds error as x starts from zero
            gx[x,y]= px[x, y]
            px[x,y] = gx[width - x-1, y]
            
    return mirroredImage


def getRotatedImage(originalImage):
    """Returns a copy of originalImage, rotated by 90 degrees (counter-clockwise)
    """
    originalImage=getMirrorImage(originalImage)
    # saving a copy of the original image 
    size = originalImage.size
    
    newWidth = size[1] 
    newHeight = size[0] 
    # defining a new image called a RotatedImage using a new width and a new height
    RotatedImage = Image.new("RGB", (newWidth, newHeight))
    
    
    pxOriginal = originalImage.load()
    pxRotated = RotatedImage.load()
    
    width = originalImage.width
    height = originalImage.height

    # the loop runs through every pixel in the original image and switches the width and 
    # the height to get a new rotated image stored in RotatedImage 
    for y in range(height):
        for x in range(width):
            pxRotated[y, x] = pxOriginal [x, y]
    return RotatedImage



def getScaledImage(originalImage, scaling):
    # Returns a scaled copy of originalImage
    if scaling <= 0:
        return 
    # returns none if the scaling value is less than or equal to zero
    size = originalImage.size
    # defines a new width and height with the sizes multiplied by the scaling value, 
    # converted to integer
    newWidth = int(size[0] * scaling)
    newHeight = int(size[1] * scaling)

    # create a new image with different dimensions

    scaledImage = Image.new("RGB", (newWidth, newHeight))

    # loads the pixels so we can manipulate them
    pxOriginal = originalImage.load()
    pxScaled = scaledImage.load()
    
    #goes through, pixel by pixel, and adjusts to the scaling value specified 
    for x in range(newWidth):
        for y in range(newHeight):
            pxScaled[x,y] = pxOriginal[x/scaling, y/scaling]
    

    return scaledImage


################################################################################
##  Vacation Challenge  ##  First make sure your code above is working.  #######
################################################################################

def changeBlackboard(originalImage, red, green, blue):
    """Returns a copy of originalImage where all "blackboard" pixels are
       replaced by the colour specified by the supplied red, green, and blue
       values
    """
    
    # make a copy so we don't affect the original image
    bbImage = originalImage.copy()

    width = bbImage.width
    height = bbImage.height

    # loads the pixels so we can manipulate them
    px = bbImage.load()

    redTotal = 0
    greenTotal = 0
    blueTotal = 0
    
    # loop through the first four pixels of the x coordinate
    for x in range(4):
       redValue=px[x,0][0]
       greenValue=px[x, 0][1]
       blueValue=px[x, 0][2]
       #saves all the red, green, and blue values, and keeps a running total        
       
       redTotal = redTotal+redValue
       greenTotal = greenTotal+greenValue
       blueTotal = blueTotal+blueValue
    
    #averages the color values
    redAvg=redTotal/4
    greenAvg=greenTotal/4
    blueAvg=blueTotal/4
    
    #loops through all pixels, and if the pixel is within a range of the +-25 of the 
    #red AND green AND blue value, replaces it with the color values given
    for x in range(width):
        for y in range(height):
            if (px[x,y][0]<=redAvg+25 and px[x,y][0]>=redAvg-25) and (px[x,y][1]<=greenAvg+25 and px[x,y][1]>=greenAvg-25)  and (px[x,y][2]<=blueAvg+25 and px[x,y][2]>=blueAvg-25):
                px[x,y]=(red, green, blue)


    return bbImage


def vacationImage(blackboardImage, backgroundImage):
    """Returns a copy of previous image where the blackboard is replaced by
       some more pleasing background
    """
    bbImage = blackboardImage.copy()
    backImage = backgroundImage.copy()
    
    
    width = bbImage.width
    height = bbImage.height
    
    widthBack = backImage.width
    heightBack = backImage.height
     
    # loads the pixels so we can manipulate them
    px = bbImage.load()
    bx = backImage.load()
    
    picwidth = widthBack/2
    picheight = heightBack/2

    redTotal = 0
    greenTotal = 0
    blueTotal = 0
    
    # loop through the first four pixels of the x coordinate
    for x in range(4):
       redValue=px[x,0][0]
       greenValue=px[x, 0][1]
       blueValue=px[x, 0][2]
       #saves all the red, green, and blue values, and keeps a running total
        
       redTotal = redTotal+redValue
       greenTotal = greenTotal+greenValue
       blueTotal = blueTotal+blueValue
    
    #averages the color values
    redAvg=redTotal/4
    greenAvg=greenTotal/4
    blueAvg=blueTotal/4
    
    #loops through all pixels, and if the pixel is NOT within a range of the +-25 of the 
    #red AND green AND blue value of the blackboard, inputs the pixel into the background image
    for x in range(width):
        for y in range(height):
            if (px[x,y][0]<=redAvg+25 and px[x,y][0]>=redAvg-25) and (px[x,y][1]<=greenAvg+25 and px[x,y][1]>=greenAvg-25)  and (px[x,y][2]<=blueAvg+25 and px[x,y][2]>=blueAvg-25):
               pass
            else:
                bx[picwidth +x,picheight +y] = px[x,y]

    return backImage



def main():
    # Complain (and exit) if there is no command line argument.
    if len(sys.argv) <= 1:
        print('Usage: python3 {0} <image file, background file (requires both files to run)>'.format(sys.argv[0]))
        sys.exit(1)

    # Use the command line argument as the main testing image.
    filename = sys.argv[1]
    file1 = sys.argv [2]
    backgroundImage = Image.open(file1)
    myImage = Image.open(filename)
    scale = float(input('What would you like the scale value to be? '))
    redvalue = int(input('What would you like the red value for the blackboard to be? '))
    greenvalue = int(input('What would you like the green value for the blackboard to be? '))
    bluevalue = int(input('What would you like the blue value for the blackboard to be? '))
#    myImage.show()

####################
##  Sample Functions

    redImage = getRedImage(myImage)
    redImage.show()


    smallImage = getSmallImage(myImage)
    smallImage.show()

#############################
##  Basic Image Manipulations

    #shows grayscale image
    grayImage = getGrayImage(myImage)
    grayImage.show()

    #shows negative image
    negativeImage = getNegativeImage(myImage)
    negativeImage.show()

    #shows mirrored image
    mirrorImage = getMirrorImage(myImage)
    mirrorImage.show()

    #shows rotated image
    rotatedImage = getRotatedImage(myImage)
    rotatedImage.show()

    #shows image scaled to the input specified
    #For this to work, you have to manually enter the scale value in the function below
    scaledImage = getScaledImage(myImage, scale)
    if scaledImage != None:
       scaledImage.show()

    #shows the blackboard image with the background replaced with the color values specified
    bbImage = changeBlackboard(myImage, redvalue, greenvalue, bluevalue)
    bbImage.show()
    
    #shows Jed's face over the background image supplied in the command line
    vacation = vacationImage(myImage, backgroundImage)
    vacation.show()


if __name__ == '__main__':
    main()
