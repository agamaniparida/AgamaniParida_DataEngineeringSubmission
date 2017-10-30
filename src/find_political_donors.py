# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 12:14:45 2017
@author: Agamani Parida
"""
"""Date Time library and SYS has been used"""
import datetime
import sys

"""GLOBAL VARIABLES"""
inputPATH=""
destinationPathZIP=""
destinationPathDate=""


def medianvals_by_zip(ilist):
    """The block of code will calculate all the details for aggregating the value by ZIP"""
    try:
        firstMedianlst=[]
        secondMedianlst=[]
        thirdMedianlst=[]
        fourthMedianlst=[]
        fifthMedianList=[]
        for l in ilist:
            if len(l[1]) >=5:
                thirdMedianlst=[l[0],l[1][:5],l[3]]
                firstMedianlst=[l[0],l[1][:5]]
                secondMedianlst.append(firstMedianlst)
                fourthMedianlst.append(thirdMedianlst)
                if secondMedianlst.count(firstMedianlst)==1:
                    #print(l[0],l[1][:5],median([l[3]]),secondMedianlst.count(firstMedianlst),l[3])
                    fifthMedianList.append([l[0],l[1][:5],median([l[3]]),secondMedianlst.count(firstMedianlst),l[3]])
                    continue
                else:
                    ls= getMultiList(fourthMedianlst,firstMedianlst)
                    fifthMedianList.append([l[0],l[1][:5],round(median(ls)),secondMedianlst.count(firstMedianlst),sum(ls)])
                    #print(l[0],l[1][:5],round(median(ls)),secondMedianlst.count(firstMedianlst),sum(ls))
        #print(fifthMedianList)
        print("Succsfully Completed for median values by ZIP" )
        writeToTextFile(fifthMedianList,1)
    except Exception as e:
            print("Error Occured in the function - medianvals_by_zip" +str(e))
                                
def median(lst):
    """The block of code will calculate the median of list of values"""
    try:
        sortedLst = sorted(lst)
        lstLen = len(lst)
        index = (lstLen - 1) // 2
    
        if (lstLen % 2):
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1])/2.0
    except Exception as e:
            print("Error Occured in the function - median" +str(e))

def getMultiList(lst1,lst2):
    """The block of code will help us finding the total number of value with the combination of DATE and Contributor and 
    secondly total values when considering Contributor and ZIP """
    try:
        thirdlist=[]
        for l in lst1:
            if l[0] == lst2[0] and l[1]==lst2[1]:
                thirdlist.append(int(l[2]))
        return(thirdlist)
    except Exception as e:
            print("Error Occured in the function - getMultiList" +str(e))

def validateDate(val): 
    """The block of code will veriify the dates are in proper format or not"""
    try:
        datetime_object = datetime.datetime.strptime(val, '%m%d%Y')
        #print(datetime_object)
        return True
    except Exception as e:
        #print("Error Occured in the function - validateDate" +str(e))
        return False        
def writeToTextFile(list1,op):
    try:
        if op==1:
            """The file will be written for zip"""
            text_file = open(destinationPathZIP, "w")
            for l in list1:
                text_file.write(str(l[0]) +"|"+ str(l[1]) +"|"+ str(l[2]) +"|"+ str(l[3]) +"|"+ str(l[4])+"\n")
            text_file.close()    
        elif op==2:
            """The file will be written for Date"""
            text_file = open(destinationPathDate, "w")
            for l in list1:
                text_file.write(str(l[0]) +"|"+ str(l[1]) +"|"+ str(l[2]) +"|"+ str(l[3]) +"|"+ str(l[4])+"\n")
            text_file.close()
    except Exception as e:
            print("Error Occured in the function - writeToTextFile" +str(e))
        
def medianvals_by_date(ilist):
    """The block of code will calculate all the details for aggregating the value by Date"""
    try:
        firstMedianlst=[]
        secondMedianlst=[]
        thirdMedianlst=[]
        fouthMedianlst=[]
        for l in ilist:
            #print(validateDate(l[2]))
            if len(l[2])==8 and validateDate(l[2]):
                firstMedianlst=[l[0],l[2]]
                if secondMedianlst.count(firstMedianlst)!= 1:
                    secondMedianlst.append(firstMedianlst)
                    thirdMedianlst= getTotalAmount(firstMedianlst,ilist)
                    sumT = sum(thirdMedianlst)
                    count= len(thirdMedianlst)
                    medianVal= round(median(thirdMedianlst))
                    #print(l[0],l[2],medianVal,count,sumT)
                    fouthMedianlst.append([l[0],l[2],medianVal,count,sumT])
        fouthMedianlst.sort(key=lambda x: x[0])
        #fouthMedianlst.sort(key=lambda x: x[1])
        #print(fouthMedianlst)
        print("Succsfully Completed for median values by date" )
        writeToTextFile(fouthMedianlst,2)
    except Exception as f:
            print("Error Occured in the function - medianvals_by_date" +str(f))

def getTotalAmount(lst1,lst2):
    """The block of is a helper fuction to calculate the getTotal Amount by making that in to list by verifying the contributor and zip"""
    try:
        thirdlist=[]
        for l in lst2:
            if l[0] == lst1[0] and l[2]==lst1[1]:
               thirdlist.append(int(l[3]))
        return(thirdlist)
    except Exception as e:
            print("Error Occured in the functions- getTotalAmount" +str(e))
            
def main_func():
    try:
        from datetime import datetime
        inputList=[]
        medianlst=[]
        fourlist=[]
        """The block of code will parse the actual date from the pipe delimetaed file to a list of list"""
        try:
            import csv
            with open(inputPATH) as f:
                reader = csv.reader(f, delimiter="|")
                d = list(reader)
        except Exception as e:
            print("Error Occured in Input file Read" +str(e))
        if len(d)== 0:
             print("There is no value in the input value of values could not be extracted")
        else:
            for i in d:
                if i[15]=='':
                    #print(i[0],i[10],i[13],i[14])
                    localLst=[i[0],i[10],i[13],i[14]]
                    inputList.append(localLst)  
        try:
            medianvals_by_date(inputList)          
            medianvals_by_zip(inputList)
        except Exception as f:
            print("Error Occured in Invoking the functions" +str(f))
    except:
        print("Error Occured In Running the main function")
    

if sys.argv[0] and sys.argv[1] and sys.argv[2] and sys.argv[3]:
    print ("Input File -",str(sys.argv[1]))
    print ("Out File Path For Calculating By ZIP -",str(sys.argv[2]))
    print ("Out File Path For Calculating By Date -",str(sys.argv[3]))
    inputPATH= sys.argv[1]
    destinationPathZIP= sys.argv[2]
    destinationPathDate= sys.argv[3]
    main_func()
else:
    print("The correct format of the input_file_path.txt is python executable_file inputfile .outfile_path_by_zip.txt output_file_path_by_date.txt")
    print("For example python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt")

