


def get_image_values(path):
    
    from PIL import Image
    i = Image.open(path)

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
     
        
    return all_pixels


