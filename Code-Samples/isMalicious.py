#!/usr/bin/python3
import sys
from rich import print
from os import path
import hashlib
from random import sample
from datetime import datetime
from virus_total_apis import PublicApi as VirusTotalPublicApi
"""
Python: 3.6.0
OS: Linux
Written For: https://github.com/Mili-NT/BinBot/

Purpose: Scans files using the VirusTotal API to check for malware
"""



api_key = "" # Insert API Key here, although in practice this should be kept in an environment variable or in an excluded file

class Scan:
    def __init__(self, filepath):
        self.filepath = filepath
        self.api = VirusTotalPublicApi(api_key)

    def get_file_hash(self):
        with open(self.filepath, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    def check_file_size(self):
        if path.getsize(self.filepath) > 32000000:
            print(self.format("error", "VT filesize limit of 32mb exceeded."))
            exit()

    def format(self, str_type, *str):
        if str_type == "item":
            return f"[bold blue]{str[0]}[/bold blue]: [green]{', '.join(str[1:])}[/green]\n"
        elif str_type == "item_percent":
            item_color = "bold red" if str[1] > 0 else "green"
            return f"[bold blue]{str[0]}[/bold blue]: [{item_color}]{str[1]}%[/{item_color}]\n"
        elif str_type == "line":
            return f"[bold blue]{str[0]}[/bold blue]]\n"
        elif str_type == "error":
            return f"[bold red]{str[0]}[/bold red]\n"
        else:
            return str

    def display(self, results):
        isQueued = True if 'queued' in results['verbose_msg'] else False
        display_str = self.format('line', """"[----- Results -----]""")
        display_str += self.format("item", "Link to Scan", results['permalink'])
        if isQueued:
            display_str += self.format("line", results['verbose_msg'])
        else:
            display_str += self.format("item", "[Total Results]", f"{results['total']}")
            display_str += self.format("item_percent", "Percentage Flagged", 100 * float(results['positives']) // float(results['total']))
            display_str += self.format("item", "[Known as]", *sample(results['names'], 10))
        display_str += self.format('line', "[-------------------]")
        print(display_str)

    def get_scan_info(self):
        response = self.api.get_file_report(self.get_file_hash())
        if response['response_code'] != 200:
            print(f"[bold red]Non-200 Response Code: {response['response_code']}. Check connection and site status.[/bold red]")
            exit()
        if response['results']['response_code'] != 0:
            results = response['results']
            scan_list = results['scans']
            results['names'] = [scan_list[scan]['result'] for scan in scan_list if scan_list[scan]['result']]
        else:
            results = self.api.scan_file(self.filepath, from_disk=False)['results']
        return results

    def scan(self):
        scan_results = self.get_scan_info()
        self.display(scan_results)

def main(filepath):
    Scan(filepath).scan()


if __name__ == "__main__":
    try:
        start = datetime.now()
        main(sys.argv[1])
        finish = datetime.now()
        print(f"Runtime: {finish - start}")
    except IndexError:
        print(f"Usage: {sys.argv[0]} <filepath>")