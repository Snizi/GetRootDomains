#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('subdomains', help='File containing a list of subdomains')
parser.add_argument('output_file', help='Name of the file to output the result')
args = parser.parse_args()

with open(args.subdomains) as f:
    stripped_subdomains = []
    duplicated_domains = []

    subdomains = f.readlines()
    
    for subd in subdomains:
        stripped_subdomains.append(subd.strip('\n'))
    
    for I in stripped_subdomains:
        string = I.split('.')
        duplicated_domains.append(string[-2] + '.' + string[-1])

root_domains = list(dict.fromkeys(duplicated_domains))

with open(args.output_file, 'w') as f:
    for domain in root_domains:
        f.write(domain + '\n')
