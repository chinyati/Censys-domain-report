#!/usr/bin/env python3

import configparser
from random import shuffle

import censys.certificates
import json
import censys.ipv4
import censys
import sys
import cli
import time

# Configuration file with Secret & API Id KEYS
config = configparser.ConfigParser()
config.read("config.ini")

# Defining constants and getting feeder values from config file
censys_apiID = config.get("DEFAULT", 'CENSYS_API_ID')
censys_secret = config.get("DEFAULT", 'CENSYS_API_SECRET')


# Main Menu function, this is where the main activities are selected
def mainMenu(domain):
    print("\n--------------------------------------------------------------------------------")
    print("1. Find the Subdomains associated with domain:")
    print("2. See the IP address(es) associated with domain:")
    print("3. Quit")
    print("--------------------------------------------------------------------------------")
    while True:
        try:
            selection = int(input("Enter choice: \n"))
            if selection == 1:
                sub(domain)
                continue
            elif selection == 2:
                ip(domain)
                continue
            elif selection == 3:
                break
            else:
                print("Invalid choice. Enter 1-3\n")
        except ValueError:
            print("Something went wrong. Enter 1-3\n")
    exit


# Used code snippets from the Censys API official documentation
def subdomain_query(domain, subdomain_fields):
    cert = censys.certificates.CensysCertificates(censys_apiID, censys_secret)
    domain_search = cert.search(domain, fields=subdomain_fields)

    subdomains = []
    for search_results in domain_search:
        subdomains.extend(search_results['parsed.names'])
    return list(set(subdomains))  # Used this to remove duplicates in subdomain list


# Prints the list of found subdomains to console
def output_subdomains(domain, subdomains):
    if len(subdomains) == 0:
        print('[--] Did not find any subdomain')
        return

    print('[##] Found %d unique subdomain%s for %s\n' % (
        len(subdomains), 's' if len(subdomains) > 1 else '', domain))
    for subdomain in subdomains:
        print('  - ' + subdomain)
    print('')

    # Saves the list of found subdomains to an output file
    json_object = json.dumps(subdomains, indent=4)
    with open("Subdomains_Report.json", "w") as outfile:
        outfile.write(json_object)
        print('[#####] WROTE %d SUBDOMAINS to Subdomains_Report.json in source folder\n' % (len(subdomains)))


def ipv4_query(domain, ipv4_fields):
    protocol = censys.ipv4.CensysIPv4(censys_apiID, censys_secret)
    ip_search = protocol.search(domain, fields=ipv4_fields)
    ipv4_list = list(ip_search)

    res_list = []
    for i in range(len(ipv4_list)):  # Remove duplicate domains and append in new list
        if ipv4_list[i] not in ipv4_list[i + 1:]:
            res_list.append(ipv4_list[i])
            print(res_list)

    # Writing console output to Json file
    json_object = json.dumps(res_list, indent=4)
    with open("IP_Report.json", "w") as outfile:
        outfile.write(json_object)
        print('\n[#####] Wrote %d IP Addresses to IP_Report.json in source folder\n' % (len(res_list)))


# Prints the list of found ip addresses to console
def print_ip(domain, ip):
    if len(ip) == 0:
        print('[--] Did not find any subdomain')
        return

    print('[##] Found %d unique subdomain%s for %s\n' % (
        len(ip), 's' if len(ip) > 1 else '', domain))
    for protocol in ip:
        print('  - ' + protocol)
    print('')


# Main class for the execution of the subdomain query
# Used code snippets from https://github.com/christophetd/censys-subdomain-finder
def sub(domain):
    print('[###] Querying Censys for subdomains associated with %s\n' % domain)
    subdomain_fields = ['parsed.names']
    subdomains = subdomain_query(domain, subdomain_fields)
    output_subdomains(domain, subdomains)


# Main class for execution of IP address Query
def ip(domain):
    print('[###] Querying Censys for IP addresses associated with %s\n' % domain)
    ipv4_fields = [
        "ip",
        "location.city",
        "location.country",
        "location.country_code",
        "location.postal_code",
        "autonomous_system.name",
        "autonomous_system.organization"
    ]
    ipv4_query(domain, ipv4_fields)


args = cli.parser.parse_args()
mainMenu(args.domain)
