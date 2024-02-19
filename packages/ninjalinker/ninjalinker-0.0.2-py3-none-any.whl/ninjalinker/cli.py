#!/usr/bin/python
import os
import sys
from rich import print
from rich.panel import Panel
import platform
# Action performed by the tool

ACTIONS = {
    "connect": "wgconnect",
    "disconnect": "wgdisconnect",
    "configure": "configure",
    "login": "login",
    "logout": "logout",
    "add_device": "add_device",
    "showinfo": "showinfo",
    "isinstalled":"isinstalled",
    "mypublickey":"mypublickey",
    "listdevices":"listdevices",
    "wizmode":"wizmode",
    "remove_device":"remove_device"
}
HELPMESSAGE = """
[bold red]Note: If you're using this VPN for the first time, run the following command to set up WireGuard:[/bold red]

$ [bold]ninjalinker configure[/bold]

[bold green1]NinjaLinker[/bold green1]

[bold green1]OPTIONS:[/bold green1]
        :small_blue_diamond:[bold] -h | --help[/bold]: help show the options
        :small_blue_diamond:[bold] configure[/bold]: Set up your wireguard
        :small_blue_diamond:[bold] login[/bold]: Log in to your Gitlab account
        :small_blue_diamond:[bold] add_device[/bold]: Add a new device
        :small_blue_diamond:[bold] connect[/bold]: Establish a connection
        :small_blue_diamond:[bold] disconnect[/bold]: Terminate the connection
        :small_blue_diamond:[bold] logout[/bold]: Loggedout form gitlabs
        :small_blue_diamond:[bold] remove_device[/bold]: Remove the device from labs

For detail documentation checkout here https://docs.selfmade.ninja/
"""
# Below code is to find the platform 
if platform.system().lower() == "linux":
    from ninjalinker.wglib.wg import Wireguard
elif platform.system().lower() == "windows":
    from ninjalinker.wglib.windowswg import windowswireguard as Wireguard
elif platform.system().lower() == "mac":
    print("[bold red]:small_blue_diamond: Under Development Comming soon[/bold red]")
else:
    print("[bold red]Unsupported Platform[/bold red]")

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "--help" or sys.argv[1] =="-h":
        print(HELPMESSAGE)
        return

    action = sys.argv[1]

    if action in ACTIONS:
        action_function_name = ACTIONS[action]
        wireguardobj = Wireguard()

        if hasattr(wireguardobj, action_function_name):
            action_function = getattr(wireguardobj, action_function_name)
            print(f"[bold green1]:small_blue_diamond: Performing action: [bold]{action}[/bold][/bold green1]")
            action_function()
        else:
            print(f"[red]Error:[/red] Action '{action}' not supported.")
    else:
        print(f"[red]Error:[/red] Action '{action}' not recognized. see ninja -h or --help")
if __name__ == "__main__":
    main()