"""Úkol 1 - Singleton

Pomocí vzoru Singleton vytvořte jednoduchou třídu loggeru,
která do souboru zapíše řetězce a datum a čas.
Použijte vnořenou třídu, která shromažďuje funkce instance
a přetížení metody new."""



import os
from datetime import datetime

class Logger:
    # Vnořená třída pro uchování instance
    class __Logger:
        def __init__(self):
            self.filename = "log.txt"

        def log(self, message):
            with open(self.filename, "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp} - {message}\n")

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = cls.__Logger()
        return cls.instance

# Příklad použití
if __name__ == "__main__":
    logger = Logger()
    logger.log("Toto je prvá správa.")
    logger.log("Toto je druhá správa.")