#!/usr/bin/python3

import os
import sys
import requests
import re

baseurl='https://unboundtest.com/caaproblem/checkhost'
#postdata={'fqdn':'cpcontacts.eayp.or.ke'}
f = open("scanresult.txt", "w")
#filepath = sys.argv[1]

def main():
    userop=input("What scan do you want to run?\nEnter 1 if you wish to scan a single domain: \nEnter 2 if you wish"
                 " to scan multiple domains from a file: ")
    if userop == "1":
        userdomain=input("Enter the domain to be checked in FQDN format:\n")
        postdata = {'fqdn': userdomain.strip()}
        checkvuln(postdata,userdomain)
    elif userop == "2":
        filepath_zz=input("Enter the file path with the list of domain to be checked:\n")
        autoscan(filepath_zz)
    else:
        print("Some error broke this code")
    return

def checkloop():
    userop=input("Do you wish to run another check? If Yes, Enter 1 else press any other key: ")

    if userop =="1":
        main();
    else:
        sys.exit()


def autoscan (filepath):

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
    else:
        with open(filepath) as fp:
            url=fp.readline()
            while url:
                postdata={'fqdn':url.strip()}
                #print(postdata)
                checkvuln(postdata,url)
                url=fp.readline()
            f.close()
            cleanfile()
    return

def cleanfile():
    with open("scanresult.txt", 'r') as inp, open('cleanedscanresult.txt', 'w') as out:
        for line in inp:
            if re.search('\S', line):
                out.write(line)
        print("Check Completed and .txt output files saved in current working directory")
    return

def checkvuln(postdata,url):
    r = requests.post(baseurl, postdata)
    response=r.text
    if r.status_code ==200 and "unknown: dial tcp" in response:
        print("{} cant be reached. Site might be down or domain cant be resolved".format(url.strip()))
        f.write("{} cant be reached. Site might be down Site might be down or domain cant be resolved.\n".format(url.strip()))
    elif r.status_code ==200 and "unknown: x509: certificate" in response:
        print("{} check is unknown. Might be requiring basic auth".format(url.strip()))
        f.write("{} check is unknown. Might be requiring basic auth\n".format(url.strip()))
    elif r.status_code ==200 and "needs renewal" in response:
        print("{} is Vulnerable".format(url.strip()))
        f.write("{} is Vulnerable\n".format(url.strip()))
    elif r.status_code ==200 and "It is not one of the certificates affected by the Let's Encrypt CAA rechecking problem" in response:
        print("{} is Not vulnerable".format(url.strip()))
        f.write("{} is Not Vulnerable\n".format(url.strip()))
    else:
        print("{} state cant not be defined.Unhandled exception".format(url.strip()))
        f.write("{} state cant be defined. Unhandled Exception {}\n".format(url.strip(),response))
        #   f.close()
    return


#urlinput('')
if __name__ == '__main__':
   main()
   checkloop()

