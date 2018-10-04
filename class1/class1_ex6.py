#!/usr/bin/env python

from __future__ import unicode_literals, print_function
import yaml
import json

def main():
    yaml_file = 'my_test_e6.yml'
    json_file = 'my_test_e6.json'

    my_dict = {
        'ip_addr': '192.168.1.2',
        'platform': 'cisco_ios',
        'vendor': 'cisco',
        'model': '1921',
    } 

    my_list = [
        'la la la',
        99,
        24,
        my_dict,
        'do do do',
        'de de de'
    ]

    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open(json_file, "w") as f:
        json.dump(my_list, f)

if __name__ == "__main__":
    main()  
