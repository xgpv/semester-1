import sys
import copy
from filters import Image


image = Image.create(3, 3)
image.read_pgm('week1.6/session2/images/feep.pgm')

print(image._write_pixels(sys.stdout))
print('\n\n')

def blur(image):
    blurimage = image.copy()                                                # creates a reference so that the original is not permanently changed
    for row in range(1, image.height - 1):                                  # for every row, besides the outer ones
        for col in range(1, image.width - 1):                               # for every column, besides the outer ones
            threebythreetotal = 0                                           # resets the average for each pixel
            for pixelrow in range(row-1, row+2):                            # for the row above and uninclusively to the second row down 
                for pixelcol in range(col-1, col+2):                        # from both columns to its side
                    threebythreetotal += image.get(pixelrow, pixelcol)      # get the value of this pixel and add to a total
            blurimage.set(row, col, threebythreetotal //9)                  # sets the selected pixel as the average of its 3x3 neighbours
    return blurimage                                                        # returns the new image, with every pixel blurred
blurredimage = blur(image)                                                  # calls the function the file selected in image  

image._write_pixels(sys.stdout)
print()
blurredimage._write_pixels(sys.stdout)