friends=input("please enter the 3 friends name with spaces:-")
friends= friends.split(" ")
myfile_read=open("data.txt","r")
content=myfile_read.read()
myfile_read.close()
content=content.split("\n")
nearbyfriends=[]
for friend in friends:
    for new in content:
        if new==friend:
            nearbyfriends.append(friend)
nearbyfriends="\n".join(nearbyfriends)
myfile_write=open("friendsnearby.txt","w")
ncontent=myfile_write.write(nearbyfriends)
myfile_write.close()
myfile_write=open("friendsnearby.txt","r")
nscontent=myfile_write.read()
myfile_write.close()
print(nscontent)