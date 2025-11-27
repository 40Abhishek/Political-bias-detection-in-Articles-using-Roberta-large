
bad=['our app', 'download', 'latestupdates', 'latest updates','subscribing to our channels',' For more news and updates']


f=open("article_data_v3.txt", 'r', encoding="utf-8")

new=[]

f2=open("test.txt",'w', encoding="utf-8")
lines=f.readlines()



def remove_n(lines):    
    cline=0 #current line
    temp=''
    for i in range(1,9095):
        # print("temp: ",temp[:50])
        new.append(temp)
        # print(new)
        # count=2
        temp=''
        if lines[cline][:len(str(i))]==str(i):
            print(lines[cline][:len(str(i))])
            temp+=lines[cline]
            cline+=1
            # print(lines[cline])

        else:
            for j in range(100):
                # print(j, " ",lines[cline][:len(str(i))]," ",i, " ", cline, " ",temp)
                if lines[cline][:len(str(i))]==str(i):
                    print(lines[cline][:len(str(i))])
                    temp+=lines[cline]
                    cline+=1
                    break
                else:
                    new[len(new)-1]=new[len(new)-1].rstrip('\n')+lines[cline]
                cline+=1

    new.append(temp)
    # for i in new:
    #     print(i[:50], end="\n\n")
    f2.writelines(new)
    return
        



# remove_n(lines) #removes all the \n

def remove_at(lines):
    for i in range(9094):
        count=2
        temp=''
        for j in lines[i]:
            if j=='@':
                if count>0:
                    count-=1
                    temp+=j
                else:
                    print("found")
                    temp+=' '
            else:
                temp+=j
            # print(j)
        lines[i]=temp
        # print(temp)
        # break
    f2.writelines(lines)

# remove_at(lines) #removes extra @ for seprator use


def remove_http(lines):
    print(len(lines))
    for i in lines:
        lis=i.split()
        # print(lis)
        temp=''
        for j in lis:
            # print(j)
            if 'twitter.com' in j or '#' in j  or 'https' in j:
                pass
            else:
                temp=temp+j+' '
        # print(temp)
        new.append(temp+'\n')
        
    print(len(new))

    f2.writelines(new)


remove_http(lines)  #removes links starting with https://....