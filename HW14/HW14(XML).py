# Task 3 XML
# 5
import xml.etree.ElementTree as ET


def parsexml(xml_str):
    root = ET.fromstring(xml_str)
    total_cost = 0

    for child in root:
        print(child.tag, child.attrib)
        print(child[0].text)

    for product in root.findall('product'):
        price = float(product.find('price').text)
        koll = int(product.find('koll').text)
        total_cost += price * koll
        print(f"{price} => {koll}")

    return total_cost


if __name__ == "__main__":
    xml_string = """<?xml version="1.0" encoding="UTF-8"?>
        <products>
            <product name='Product1'>
               <price>22</price>
               <koll>1</koll>
            </product>
            <product name='Product2'>
               <price>33</price>
               <koll>2</koll>
            </product>
        </products>
        """
    total_cost1 = parsexml(xml_string)
    print(f"Общая стоимость всех товаров: {total_cost1}")
print()
