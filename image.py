from PIL import Image
i = Image.open("Images/image2.jpg")

pixels = i.load() # this is not a list, nor is it list()'able
width, height = i.size

all_pixels = []
for x in range(width):
    for y in range(height):
        #cpixel = pixels[x, y]
        #all_pixels.append(cpixel)
        cpixel = pixels[x, y]
        bw_value = int(round(sum(cpixel) / float(len(cpixel))))
                # the above could probably be bw_value = sum(cpixel)/len(cpixel)
        all_pixels.append(bw_value)
print(all_pixels)


l = [18, 11, 21, 5, 10, 11, 37, 107, 11, 13, 16, 1, 22, 8, 44, 186, 16, 
     0, 18, 23, 2, 22, 133, 248, 14, 27, 11, 7, 3, 64, 199, 250, 0, 9,
     15, 15, 1, 84, 222, 249, 14, 7, 5, 0, 49, 176, 247, 253, 73, 116,
     74, 17, 102, 231, 240, 236, 135, 230, 227, 184, 206, 255, 253,
     248, 165, 255, 253, 247, 251, 254, 228, 232, 97, 223, 240, 253,
     245, 247, 255, 250, 26, 218, 243, 247, 251, 251, 255, 253, 99, 221, 238, 255,
     249, 248, 254, 251]       