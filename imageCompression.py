import io
from PIL import Image
import numpy

def select_your_choice():

    print("Select what to do:\n")
    
    string = str(input("1. Type '1' if you want to Enter image values.\n2. Type '2' if you want to Enter a image file.\n=> "))
    if string is '1':
        return 1
    elif string is '2':
        return 2
    else:
        return 3

def regenerate_the_image(code):
    print("Regenerating the compresed image:\n")
    pixelList = []
    for c in code:
        pixelList.append(ord(c))
    print("Key Values: ",pixelList)
    
    pixels_out = []
    for row in pixelList:  
        pixels_out.append((row,row,row))
        
    print("Image Pixels: ",pixels_out)
    
    # Convert the pixels into an array using numpy
    array = numpy.array(pixels_out, dtype=numpy.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('hello.jpg')

    
def compressing_and_decompressing(string):
    import image_compression
    import decompression

    compressed = image_compression.compress(string)
    print ("Compressed output: ",compressed)
    decompressed = decompression.decompress(compressed)
    print ("Decompressed output: ",decompressed)
    print("\n")

    print ("COMPARE:")
    if string == decompressed:
        print("Successfully Done")

    else:
        print("Not done!")
        print("\n")

    regenerate_the_image(decompressed)

def CompressDecompressData(string):

    print("*********************")
    print(" IMAGE COMPRESSION ")
    print("*********************")
    
    choice = select_your_choice()

    if choice is 2:
        
        imagePath = str(input("Enter the image path\n"))
        import imageValue
        values = []
        
        for v in imageValue.get_image_values(imagePath):
            values.append(v)
            
        
        print("Image Values: ",values)

    convertedString = []
    realString = ""
    for f in values:
        convertedString.append(chr(f))


    for s in convertedString:
        realString +=str(s)

    
    print("Converted String: ",realString)

    compressing_and_decompressing(realString)
        
    
        

