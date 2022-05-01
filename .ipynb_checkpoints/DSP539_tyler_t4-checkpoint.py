#!/usr/bin/env python3

#this is the official dump for smashing together stuff to create the final submission
# string='ATTTGGATT'
# k=1
# #counter=1
# flag=0
# for i in range(len(string)):
#     if string[i] != 'A' and string[i] != 'G' and string[i] != 'T' and string[i] != 'C':
#         flag = 1
#         break
#     #else:
#         #counter=counter+1
# if k%1 != 0 or k<=0:
#     print('Invalid k value. Must be a whole number greater than zero')
#     #break
# elif flag==1 or len(string)==0:
#     print('Invalid string. Must consist of at least one of and only of characters [A, C, G, T]')
#     #break
# elif k>len(string):
#     print('k cannot be greater than the string length')
# else:
#     #function to find possible kmers
#     print('good')
        
def possible_kmer(k,string):
    flag=0
    for i in range(len(string)):
        if string[i] != 'A' and string[i] != 'G' and string[i] != 'T' and string[i] != 'C':
            flag = 1
            break
        #else:
            #counter=counter+1

    if k%1 != 0 or k<=0:
        print('Invalid k value. Must be a whole number greater than zero')
        #break

    elif flag==1 or len(string)==0:
        print('Invalid string. Must consist of at least one of and only of characters [A, C, G, T]')
        #break

    else:
        poskmer=min(len(string)-k+1, 4**k)
        return(poskmer)

#function to find observed kmers
def observed_kmer(k,string):
    flag=0
    for i in range(len(string)):
        if string[i] != 'A' and string[i] != 'G' and string[i] != 'T' and string[i] != 'C':
            flag = 1
            break
        #else:
            #counter=counter+1

    if k%1 != 0 or k<=0:
        print('Invalid k value. Must be a whole number greater than zero')
        #break

    elif flag==1 or len(string)==0:
        print('Invalid string. Must consist of at least one of and only of characters [A, C, G, T]')
        #break

    else:
        dictionary={}
        for start in range(len(string)+1-k):
            dictionary[string[start:start+k]]=[]
            return(len(dictionary))
        
#function to create that panda table
def panda_table(k,string):
    flag=0
    for i in range(len(string)):
        if string[i] != 'A' and string[i] != 'G' and string[i] != 'T' and string[i] != 'C':
            flag = 1
            break
        #else:
            #counter=counter+1

    if k%1 != 0 or k<=0:
        print('Invalid k value. Must be a whole number greater than zero')
        #break

    elif flag==1 or len(string)==0:
        print('Invalid string. Must consist of at least one of and only of characters [A, C, G, T]')
        #break
        
    else:
    
        k_list=[]
        observed_list=[]
        possible_list=[]

        for i in range(1,k+1):
            #add the meat of finding possible and observed kmers, and then do something with making a running list and appending shit to each other
            k_list.append(i)

            plist=min(len(string)-i+1, 4**(i))
            #print(plist)
            possible_list.append(plist)

            dictionary={}
            #print(i)
            for start in range(0,len(string)-i+1):
                dictionary[string[start:start+i]]=[]
                #print(dictionary)
            olist=(len(dictionary))
            #print(olist)
            observed_list.append(olist)

        import pandas as pd

        content={'K value' : k_list, 'Observed kmers' : observed_list, 'Possible kmers' : possible_list}
        df=pd.DataFrame(data=content)
        blankIndex=[''] * len(df)
        df.index=blankIndex
        return(df)

def complexity(k,string):
    flag=0
    for i in range(len(string)):
        if string[i] != 'A' and string[i] != 'G' and string[i] != 'T' and string[i] != 'C':
            flag = 1
            break
        #else:
            #counter=counter+1

    if k%1 != 0 or k<=0:
        print('Invalid k value. Must be a whole number greater than zero')
        #break

    elif flag==1 or len(string)==0:
        print('Invalid string. Must consist of at least one of and only of characters [A, C, G, T]')
        #break
        
    else:
        k_list=[]
        observed_list=[]
        possible_list=[]

        for i in range(1,k+1):
            #add the meat of finding possible and observed kmers, and then do something with making a running list and appending shit to each other
            k_list.append(i)

            plist=min(len(string)-i+1, 4**(i))
            #print(plist)
            possible_list.append(plist)

            dictionary={}
            #print(i)
            for start in range(0,len(string)-i+1):
                dictionary[string[start:start+i]]=[]
                #print(dictionary)
            olist=(len(dictionary))
            #print(olist)
            observed_list.append(olist)

        ols=sum(observed_list)
        pls=sum(possible_list)
        return(ols/pls)