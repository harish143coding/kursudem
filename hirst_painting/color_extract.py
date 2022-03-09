import colorgram


def color_extract():

    colors = colorgram.extract("color_image.jpeg", 36)
    #print(colors)

    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_tuple = (r,g,b)
        rgb_colors.append(color_tuple)
    return rgb_colors
