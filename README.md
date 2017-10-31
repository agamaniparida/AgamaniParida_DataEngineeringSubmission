# AgamaniParida_DataEngineeringSubmission

# Project Title

The project have two core goals,first to find median contribution to any recipiant in two ways first by date and second by zip.
The function which calculates by zip will have  the running median of contributions, total number of transactions and total amount of contributions streaming in so far for that recipient and zip code. The fiunction which will findout for any specififc date will have list every unique combination of date and recipient from the input file.

## Getting Started
The code is written in Python 3.6. 
As described in the challenge the repository contains all the required files to run the program. 

### Prerequisites

So before excuting the code we need to make sure we have Python 3 installed and verify all the depndencies for Python are met. 
There are only two external libraries are used here, "datetime" and "SYS". Both the libraries which comes out of box in Python installations. To run the shell script user might not need SUdo access but not a requirement for the program. 

### Executing

1.To validate the code, first download or clone the repository to your local syestem.

2.Then unzip the repository[Optional]

3.Open the terminal and go tthe repository.

4.Once we are in the repository try running the shell script within the root Folder.[./run.sh]

5.If there is no error the terminal should diplay the below message:

    Input File - ./input/TESTDATA.txt
    Out File Path For Calculating By ZIP - ./output/medianvals_by_zip.txt
    Out File Path For Calculating By Date - ./output/medianvals_by_date.txt
    Succsfully Completed for median values by date
    Succsfully Completed for median values by ZIP
    
6.Two files will be created within the output folder named as medianvals_by_zip.txt and medianvals_by_date.txt
    
7.If there is any approppriate error messgae will be displayed.

8.If we want to excute with a differnt input file or output file we need to update the command from the shell script in the root folder names=d(run.sh)

    python ./src/find_political_donors.py ./input/TESTDATA.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

    **** ./input/TESTDATA.txt: Input file, 
    ./output/medianvals_by_zip.txt: Output file for finding by ZIP ,          
    ./output/medianvals_by_date.txt: Output file for finding by DATE.****
    
9. To test from the Test Suite we need to go the insight_testsuite directory.

10. Within the insight_testsuite there the run_test.sh script file can be excuted and if succesfully excutes then Two files will be created within the output folder named as medianvals_by_zip.txt and medianvals_by_date.txt

## Author

AGAMANI PARIDA
Master In Computer Science,Santa Clara University
