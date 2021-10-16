## Radosław Sajdak

from os import PRIO_USER
import xml.etree.ElementTree as ET

tree = ET.parse("file.xml")

root = tree.getroot()

def getSalary(name = "alex"):
    for employee in root.findall('staff'):
        nickname = employee.find('nickname')
        if nickname.text == name:
            salary = employee.find('salary')
            return salary
def setSalary(salary_obj, salary):
    salary_obj.text = salary

alex = getSalary('alex')
setSalary(alex, "997")

with open('editedXML.xml', 'wb') as f:
    tree.write(f)