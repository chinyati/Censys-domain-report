# IP & Subdomain query script using CENSYS

A python script to search for subdomains and IP addresses associated to a specific domain. It searches Certificate logs using Censys returning results on console screen whilst also saving the Subdomain and IP address query to JSON files in project source.

## Getting Started

* Register an account (free) on https://censys.io/register
* Browse to https://censys.io/account, and copy two environment variables with your API ID and API secret
* Clone/Download the repository
  
 ```
  $ git clone https://github.com/chinyati/censys-domain-report.git
 ```
* The copied Secret and API keys need to be added to config.ini file in source folder as below:
 ```
  [DEFAULT]
  CENSYS_API_ID = 0a00f434-1234-5678-910a-33cf162085e2
  CENSYS_API_SECRET = aBcDe12fghijk7PBjmRnKadOL1eULExXYZ

  Note the above keys are samples and do not work. Add your own.
  ```
* Install the dependencies only in project source folder using pip:
  
 ```
  $ cd censys-domain-report
  $ pip install -r requirements.txt
 ```

## How it works
This is a python script hence the system/container should have python and pip installed and running. Below is how the script works

![First Image](https://github.com/chinyati/Censys-domain-report/blob/master/Images/search_subdomains.jpg)]
![Second Image](https://github.com/chinyati/Censys-domain-report/blob/master/Images/search_ips.jpg)

## Usage
```
usage: censys_domain_report.py domain

positional arguments:
  domain                The domain to scan

optional arguments:
  -h, --help            show this help message and exit
```

## Improvements

1.	A More interactive interface so that user can enter domain name from menu and have its validity checked to avoid executing script on domains with errors or non-existent.
2.	Have clear Try-Catch exceptions to catch errors for a mistake in the config file or on a wrong domain name entry etc.
3.	Web Interface that outputs the JSON files in a visual report format. Could also use CSV files that can then inputted into creation of charts.
4.  Integrate the script with other Network forensics tools like Nmap so as to further analyse the IP addresses and subdomains.
