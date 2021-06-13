# A CLI for Kenna Platform

Command line interface for Kenna Platform that help security engineers to get results quickly.  

## The Kenna Modules Implemented with The API

 - [x] Vulnerabilities
 - [x] Assets
 - [x] Asset Tagging
 - [x] Asset Groups
 - [ ] Asset group reporting
 - [ ] Connectors
 - [ ] Connector Runs
 - [ ] Users
 - [ ] Roles
 - [x] Fixes
 - [ ] Applications
 - [ ] Application Reporting
 - [ ] Dashboard Groups
 - [ ] Data export
 - [x] CVEs 
 - [ ] Kenna VI+
 - [ ] Inference

## Installation

Installing this tool is very easy. You just need to run the install.sh from the command line. 

```sh
~$ bash install.sh
```

## Usage

Show a brief information based on a search pattern
```sh
python3 kenna.py summary <kenna-search pattern>
```

Show vulnerabilities based on a search pattern
```sh
python3 kenna.py assets <kenna-search pattern>
```

Show vulnerabilities based on a search pattern
```sh
python3 kenna.py assets <kenna-search pattern>
```

Get vulnerability score history: 
```sh
python3 kenna.py cvehistory cve-2020-1472
```

## Kenna Library 


