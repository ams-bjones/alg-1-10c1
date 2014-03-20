import triangle

filein = open("triangles.txt")
fileOut = open ('answers.txt', 'wt')
for line in filein:
    height, width = line.split (',')
    area = triangle.area(float(height), float(width))
    fileOut.write("""A triangle of width {0}, and height {1}, 
    will have an area of {2}\n""".format(float(width), float(height), area))
fileOut.close()
    