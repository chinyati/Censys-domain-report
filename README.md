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
This is a python script hence the system/container should have python and pip installed and running. Below is a sample of how script works
```
$ python domainQuery.py thoughtmachine.net         
  --------------------------------------------------------------------------------
  1. Find the Subdomains associated with domain:
  2. See the IP address(es) associated with domain:
  3. Quit
  --------------------------------------------------------------------------------
  Enter choice:
  1
  [###] Querying Censys for subdomains associated with thoughtmachine.net
  
  [##] Found 22 unique subdomains for thoughtmachine.net
  
    - www.beingtechnologies.com
    - www.prophecy-dev.thoughtmachine.net
    - 10.3.0.1
    - 10.0.0.50
    - www.phabricator.thoughtmachine.net
    - kubernetes.default.svc.cluster.local
    - vpn.thomac.net
    - phabricator.thoughtmachine.net
    - openvpn.thomac.net
    - kubernetes
    - k8s-proto.thoughtmachine.net
    - intranet.thoughtmachine.net
    - beingtechnologies.com
    - prophecy.thoughtmachine.net
    - prophecy-dev.thoughtmachine.net
    - kubernetes.default
    - kubernetes.default.svc
    - doge.thoughtmachine.net
    - *.thoughtmachine.net
    - www.prophecy.thoughtmachine.net
    - thoughtmachine.net
    - www.thoughtmachine.net
  
  [#####] WROTE 22 SUBDOMAINS to Subdomains_Report.json in source folder
  
  Enter choice:
  2
  [###] Querying Censys for IP addresses associated with thoughtmachine.net
  
  [{'location.city': 'London', 'location.country': 'United Kingdom', 'ip': '178.128.34.63', 'location.country_code': 'GB', 'autonomous_system.name': 'DIGITALOCEAN-ASN', 'location.postal_code': 'EC2V'}]
  
  [#####] Wrote 1 IP Addresses to IP_Report.json in source folder

Above is illustration of how the script works with subdomains and IP addresses printer to screen and saved to JSON files.
```

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
