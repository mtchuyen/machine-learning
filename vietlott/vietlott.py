#!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom
import sys, os

# Open XML document using minidom parser
def getResultLotteryADay(filename):
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        print ("Root element : %s" % collection.getAttribute("shelf"))

    # Get all the movies in the collection
    movies = collection.getElementsByTagName("movie")

    # Print detail of each movie.
    for movie in movies:
        print ("*****Kết quả quay thưởng*****")
        if movie.hasAttribute("title"):
            print ("Title: %s" % movie.getAttribute("title"))

        type = movie.getElementsByTagName('type')[0]
        print ("Type: %s" % type.childNodes[0].data)
        format = movie.getElementsByTagName('format')[0]
        print ("Format: %s" % format.childNodes[0].data)
        rating = movie.getElementsByTagName('rating')[0]
        print ("Rating: %s" % rating.childNodes[0].data)
        description = movie.getElementsByTagName('description')[0]
        print ("Description: %s" % description.childNodes[0].data)

def parseLine(content):
    print("Input", content)
    values = content.split("|")
    if len(values) != 4:
        print("the value is miss something")
    else:
        ngayquay=values[0]
        kyquay=values[1]
        ketqua=values[2]
        bonus=values[3]
        print("ngay quay {} co ket qua: {} va bonus: {}".format(ngayquay,ketqua, bonus))

def main():  
    filepath = sys.argv[1]
    #filepath = 'data/power655_all.csv'

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath) as fp:  
        line = fp.readline()
        cnt = 1
        while line:
            if line.strip() == "":
                print("Line {} is blank".format(cnt))
            else:
                print("Line {}: {}".format(cnt, line.strip()))
                parseLine(line)
            
            line = fp.readline()
            cnt += 1
            if cnt > 10:
                print("stop print")
                break
    print("stop")

if __name__ == '__main__':  
   main()
