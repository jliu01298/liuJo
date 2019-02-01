def draw():
    picture=open("picture.ppm","w")
    picture.write("P3\n500 500\n255\n")
    for i in range(500):
        for j in range(500):
            R=(i+j)%256
            G=(i-j)%256
            B=(i*j)%256
            picture.write(str(R)+" "+str(G)+" "+str(B)+" ")
    picture.close()

draw()
