header=''
str=''
file1=open("test_seq.txt","a+")#Input your fasta sequence here
file1.write("\n>DUMMY_FASTA_DUMMY\nAATTGGCC\n")#This line is added as the last line of the FASTA file
file1.close()#The file is closed
with open("test_seq.txt","r") as file1:#The file is opened again.This can be avoided but makes the code look simple
    reading=file1.read()#The file is read in this line
    data=reading.split("\n")#All the lines in the FASTA are stored as LIST that have been separated by new-line
    header=data[0]#First 
    for i in range(1,len(data)):
        if(">" not in data[i]):
            str+=data[i]
        else:
            with open("output_seq.txt","a")as file2:#Input the name of the output file you want
                file2.write(header)
                file2.write("\n"+str+"\n")
                str=''
                header=data[i]