# Port Scan Python

A program developed to scan ports, designed to be a quick and practical option.

## ⚙️ Running the tests
To run the script in the terminal, use the following syntax:
**python Main.py (-d, -p, -c, -f)**

To start the scans, we need to specify which DNS we will scan using **-d**.
Example: **-d [www.google.com](http://www.google.com)**

In the same command line, use the optional arguments:   


-p (to specify which port to check if it's open),  

-c (to scan the most common ports),  

-f (to scan the first 10,000 ports).  


## 📦 Deployment

Use in simple situations where more complex programs like Nmap aren't necessarily required. Situations where you need quick results.

## 🛠️ Built with

* [Socket](https://docs.python.org/3/library/socket.html) 
* [Argparse](https://docs.python.org/3/library/argparse.html) 

