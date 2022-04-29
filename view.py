from itertools import count
import controller
from models.LinkedList import LinkedList
from models.Node import Node

def main():
    countryList = LinkedList()

    while True:
        commands = input().split()

        if commands[0] == "RPI":
            country = commands[1]
            
            if (countryList.get_count() == 0):
                countryList.insert_at_start(country)
            
            else: countryList.insert_at_start(country)

            countryList.traverse_list()

        if commands[0] == "RPF":
            country = commands[1]

            if (countryList.get_count() > 0):
                countryList.insert_at_end(country)
            
            else: countryList.insert_at_start(country)

            countryList.traverse_list()
        
        if commands[0] == "RPDE":
            country_new = commands[1]
            country_old = commands[2]

            if (countryList.get_count() > 0):
                countryList.insert_after_item(country_old, country_new)

            else: countryList.insert_at_start(country_new)

            countryList.traverse_list()
        
        if commands[0] == "RPAE":
            country_new = commands[1]
            country_old = commands[2]

            if (countryList.get_count() > 0):
                countryList.insert_before_item(country_old, country_new)

            else: countryList.insert_at_start(country_old)

            countryList.traverse_list()
        
        if commands[0] == "RPII":
            country = commands[1]
            index = int(commands[2])

            if (countryList.get_count() > 0):
                countryList.insert_at_index(index, country)
            
            else: countryList.insert_at_start(country)

            countryList.traverse_list()

        if commands[0] == "VNE":

            número_elementos = countryList.get_count()
            print(f"O número de elementos são {número_elementos}.")
        
        if commands[0] == "VP":
            nome_país = commands[1]

            if (countryList.get_count() > 0):
                if (countryList.search_item(nome_país) == True):
                    print(f"O país {nome_país} encontra-se na lista.")
                else:
                    print(f"O país {nome_país} não se encontra na lista.")
            else: print("A Lista está vazia!")
        
        if commands[0] == "EPE":
            first_node = countryList.start_node.get_item()
            
            if (countryList.get_count() > 0):
                countryList.delete_at_start()
                print(f"O país {first_node} foi eliminado da lista.")
            else: print(f"O país  não se encontra na lista.")

        if commands[0] == "EUE":
            last_node = countryList.get_last_node()

            if (countryList.get_count() > 0):
                countryList.delete_at_end()
                print(f"O país {last_node} foi eliminado da lista.")
            else: print(f"O país  não se encontra na lista.")

        if commands[0] == "EP":
            nome_país = commands[1]

            if (countryList.search_item(nome_país) == True):
                countryList.delete_element_by_value(nome_país)
                print(f"O país {nome_país} foi eliminado da lista.")
            else: print(f"O país {nome_país} não se encontra na lista")