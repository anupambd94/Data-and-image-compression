import io

def select_your_choice():

    
        print("Select what to do:\n")
    
        string = str(input("1. Type '1' if you want to Enter data.\n2. Type '2' if you want to Enter a file.\n3.Type exit for close.\n=> "))
        if string is '1':
            return 1
        elif string is '2':
            return 2
        else:
            return 3

def user_input_file():
    filename = input("Enter the file name with path.\n")
    myfile = open(filename)
    info = myfile.readlines()

    return info

def compressing_and_decompressing(string):
    import data_compression
    import decompression
    
    print("Compressing Data >>>")
    compressed = data_compression.compress(string)
    print ("Compressed output: ",compressed)
    print("\n")
    
    print("Decompressing Data >>>")
    decompressed = decompression.decompress(compressed)
    print ("Decompressed output: ",decompressed)
    print("\n")

    print ("COMPARE:")
    if string == decompressed:
        print("Successfully Done")

    else:
        print("Not done!")
        print("\n")



def CompressDecompressData():

    print("*********************")
    print(" DATA COMPRESSION ")
    print("*********************")
    
    choice = select_your_choice()

    if choice is 1:
        string = str(input("Enter the string:\n"))
        print("Real Data: ",string)
        print("\n")
        compressing_and_decompressing(string)
        
    elif choice is 2:
        string = str(user_input_file())
        print("Real Data: ",string)
        print("\n")
        compressing_and_decompressing(string)
    

