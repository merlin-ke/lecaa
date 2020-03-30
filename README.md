# lecaa
Code to Test Lets Encrypt CAA Bug.https://medium.com/@muchilwa/all-you-need-to-know-about-lets-encrypt-caa-bugs-part-1-aa93e51ec0b1 <br>
The script is a hack written in python 3
It allows you to run the check against a single domain or from a text file containing a list of domain.
Main purpose is to allow the community identify affected sites and do something about it. I also needed to learn how to python 3.
<br>run</br> 
```
./vulncheck.py
```
Once executed, the scripts will generate a txt file with your results. <br>
You can find data to kick you off from https://github.com/ScottHelme/le-scan by Scott Helme.
Another useful links:
* https://github.com/hannob/lecaa
* https://www.cyberciti.biz/security/letsencrypt-is-revoking-certificates-on-march-4/
