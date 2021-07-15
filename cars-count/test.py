def remove_comments(line,sep="#"):
    for s in sep:
        i = line.find(s)#find the posision of  #
        if i == 0 :
            line = None
    return line.strip()

f=open("nocom.py","r")
for line in f :
    if remove_comments(line):
        print(remove_comments(line))