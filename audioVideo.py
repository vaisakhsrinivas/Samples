

f = open("test.txt" , "r")


mediaformat = []

medialist = ["m4a", "wav", "mp4", "mov", "mp3"]

#medialistdict = {'Audio': 'mp3' , 'Video': ["m4a", "wav", "mp4", "mov"]}


d = dict()


for i in f :


    mediaformat = i.split(".")



    for j in mediaformat[1:]:

        if j.rstrip() in medialist:

            print("Media file found" + " " + j)
