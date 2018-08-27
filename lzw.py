import io
import dataCompression
import imageCompression


def user_choice():

    print("Welcome in LZW Copression:\n")
    
    string = str(input("1. Type 'D' for data compression.\n2.Type 'I' for image compression.\n=> "))
    if string is 'D':
        return 1
    elif string is 'I':
        return 2
    else:
       return 3



    
    
option = user_choice()
    
if option is 1:
    # for data:
    dataCompression.CompressDecompressData()
    
elif option is 2:
    #For Image

    list = [99,99,126,126,99,99,100,100,99,99,100,100,100,126,126,126]
    print("Image Values: ",list)

    convertedString = []
    realString = ""
    for f in list:
        convertedString.append(chr(f))


    for s in convertedString:
        realString +=str(s)

    
    print("Converted String: ",realString)

    imageCompression.CompressDecompressData(realString)
else:
    print("Select a valid option: ")    
 
 
 




