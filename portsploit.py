import nmap
import os
from pathlib import Path
from rich import print as rich_print

ADDRESSES: list = []

file_ptr = open("report.csv", "w")

HEADER = "host,hostname,hostname_type,protocol,port,name,state,product,extrainfo,reason,version,conf,cpe\r\n"

file_ptr.write(HEADER)
file_ptr.close()

for i in range(1, 255):
    for j in range(1, 255):
        ADDRESSES += [f"172.16.{i}.{j}"]

file_ptr = open("report.csv", "a")

for i in ADDRESSES:
    print(f"Scanning address {i}...")
    nm = nmap.PortScanner()
    nm.scan(i, "1000-65535")
    output = nm.csv()

    output = output.replace(";", ",")
    output = output[output.index("\r\n") + 2 :]

    file_ptr.write(output)


class ScannerSession:
    def __init__(self, dir="", save_to="report.csv", *args, **kwargs):
        self.HEADER: str = "host,hostname,hostname_type,protocol,port,name,state,product,extrainfo,reason,version,conf,cpe\r\n"
        self.ADDRESSES: list = []
        self.TARGET_FILE: str = save_to

    async def load_from_file(self, src="", *args, **kwargs):
        try:
            self.ADDRESSES = sorted([x.strip() for x in open(src, "r").readlines()])
        except FileNotFoundError:
            rich_print(f"[bold red]Session with path {src} not found.[/bold red]")

    async def create_session(self, name: str = "./.session", *args, **kwargs):
        if os.path.isfile(name):
            rich_print(
                f"[bold red]File with the same name as {name} already exists.[/bold red]"
            )
            raise FileExistsError
        else:
            loc = open(name, "w")
            loc.close()

    async def resume(self, session: str = ".session", *args, **kwargs):
        last_scanned: list = open(session, "r").readlines()
        if last_scanned in self.ADDRESSES:
            self.ADDRESSES = self.ADDRESSES[self.ADDRESSES.index(last_scanned) + 1 :]

    async def scan(self, target: Dict={}, *args, **kwargs):
        nm = nmap.PortScanner()
        nm.scan()

    async def bulk_scan(self, targets: List[str] = [], *args, **kwargs):
        pass

    async def serialize(self, data, format="json"):
        pass
    
    async def save_session(self):
        pass