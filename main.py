#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

#TODO: Curses interface erstellen

from ui import ui

def main() :

    print("Starte PI-Smarthome CLI...")

    ui.Interface.init()
    ui.Interface.start()

if __name__ == "__main__":

    main()