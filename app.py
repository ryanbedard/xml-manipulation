import requests
import json
from xml.etree import ElementTree as ET


def total_ghosts():
    r = requests.get(
        'http://wwwnui.akamai.com/gnet/gnet_public.xml')

    test_file = open('test.xml', 'wb')
    test_file.write(r.content)

    tree = ET.parse('test.xml')
    root = tree.getroot()
    ghosts = 0

    for ghost in root.findall('location'):
        num = int(ghost.find('ghosts').text)
        ghosts += num

    with open('data.json', 'w') as outfile:
        json.dump({"Total Ghosts": ghosts}, outfile)


def connections_too():
    my_dictionary = {
        "total_connections": 0,
        "total_ghosts": 0
    }

    r = requests.get(
        'http://wwwnui.akamai.com/gnet/gnet_public.xml')

    test_file = open('test.xml', 'wb')
    test_file.write(r.content)

    tree = ET.parse('test.xml')
    root = tree.getroot()

    for ghost in root.findall('location'):
        num = int(ghost.find('connections').text)
        my_dictionary['total_connections'] += num
        num = int(ghost.find('ghosts').text)
        my_dictionary['total_ghosts'] += num

    with open('data.json', 'w') as outfile:
        json.dump(my_dictionary, outfile)


if __name__ == '__main__':
    #total_ghosts()
    connections_too()
