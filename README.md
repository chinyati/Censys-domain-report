# IP & Subdomain query script using CENSYS

A python script to search for subdomains and IP addresses associated to a specific domain. It searches Certificate logs using Censys returning results on console screen whilst also saving the Subdomain and IP address query to JSON files in project source.

## Getting Started

* Register an account (free) on https://censys.io/register
* Browse to https://censys.io/account, and copy two environment variables with your API ID and API secret
* Clone/Download the repository
* The copied Secret and API keys need to be added to config.ini file in source folder as below:
 ```
  [DEFAULT]
  CENSYS_API_ID = ####
  CENSYS_API_SECRET = ####

  Note the above keys are samples and do not work. Add your own.
  ```
* Install the dependencies only in project source folder using pip:
  
 ```
  $ cd censys-domain-report
  $ pip install -r requirements.txt
 ```

## Usage
This script is executed with domain name input entered. Currently if a non existent domain is entered excpetion errors are caught or   null values are swhon. A clear Try-Except will be used in future work and also allow for domain name to be entered within the display menu. However for the requirement of the exercise the code can query subdomains and IP Addresses for the domain "thoughtmachine.net".
```
usage: $ python domain_query.py domain

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
