import telebot
import scapy.all as scapy
from colorama import Fore, Style

token = ""
id = ""
tb = ""

def sniff(packet):
    if packet.haslayer("TCP") and packet.haslayer("Raw"):
        data = packet.getlayer("Raw").load

        if b"GET /texture" in data or b"/skin" in data: # я знаю
            if token != "":
                tb.send_message(id, "Player detected!")
            print(" [+] Player detected")

        if "mc." in data.decode("utf-8", "ignore") or "play." in data.decode("utf-8", "ignore") and not "{" in data.decode("utf-8", "ignore"):
            print(" [+] Server detected: " + data.decode("utf-8", "ignore")[:-2])


def main():
    print(Fore.BLUE + "    _  __     ____")
    print("   / |/ /_ __/ / /")
    print("  /    / // / / / ")
    print(" /_/|_/\_,_/_/_/  ")
    print("  by bush1root")

    print(Style.RESET_ALL)

    global tb, id, token
    token = input(" Enter token if you have > ")
    id = input(" Enter ID if you have > ")

    if token != "":
        tb = telebot.TeleBot(token)
        tb.send_message(id, "Done, the setup was successful!")

    print()

    scapy.sniff(filter='', prn=sniff)


main()
