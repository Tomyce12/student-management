import os.path
import csv
from csv import DictReader
from llist import sllist
from datetime import datetime
import time
sList = sllist()

def Display():
  counter = 0
  for row in sList:
    counter += 1
    print(str(counter) + "  " + row['Task'] + "  " + row['Subject'] + "  " + row['Deadline'] + "  " + row['Description'])
  
  if counter == 0:
    print("Your list is empty")

def ReadFile(file):
  with open(file, 'r') as f:
    csv_doc = DictReader(f)
    for row in csv_doc:
      task = row['Task']
      subject = row['Subject']
      deadline = row['Deadline']
      description = row['Description']

      node = {
        'Task': task,
        'Subject': subject,
        'Deadline': deadline,
        'Description': description
      }
      sList.append(node)
  f.close()

def WriteFile(file):
  with open(file, 'w', newline='') as file:
    header = [
      'Task',
      'Subject',
      'Deadline',
      'Description'
    ]
    write = csv.DictWriter(file, fieldnames=header)
    write.writeheader()
    for row in sList:
      write.writerow({
        'Task': row['Task'],
        'Subject': row['Subject'],
        'Deadline': row['Deadline'],
        'Description': row['Description']
      })

def Insertion():
  print('Please provide your desirable position for a record:')
  pos = input('->')

  if int(pos)-1 > len(sList) or int(pos) <= 0:
    print("Error: position unavailable")
  else:
    task = input("Task name:\n->")
    subject = input("Subject name:\n->")
    deadline = input("Deadline (DD/MM/YYYY):\n->")
    description = input("Description of the task:\n->")

    # to back
    if int(pos)-1 == len(sList):
      node = {
        'Task': task,
        'Subject': subject,
        'Deadline': deadline,
        'Description': description
      }
      sList.append(node)
    else:
      node_next = sList.nodeat(int(pos)-1)
      node = {
        'Task': task,
        'Subject': subject,
        'Deadline': deadline,
        'Description': description
      }
      sList.insertbefore(node, node_next)

def DeleteNode(i):
  if int(i) == len(sList):
    sList.pop()
  else:
    node = sList.nodeat(int(i))
    sList.remove(node)

def DeletePos(pos):
  if int(pos) > len(sList) or int(pos) <= 0:
    print('Error: non-existent position')
  else:
    DeleteNode(int(pos)-1)

def DeleteCr(i,text):
  inputText = input(text)
  counter = -1
  index = []
  
  for row in sList:
    counter+=1
    if inputText == row[i]:
      index.append(counter)
  counter = 0
  if len(index) > 1:
    l = len(sList)
    for row in index:
      DeletePos(int(row) - int(counter) + 1)
      if int(l) != len(sList):
        counter+=1
      l=len(sList)
  elif len(index) == 1:
    for row in index:
      DeletePos(int(row)+1)
  else:
    print("Error: please enter corrent name\n")

def Deletion():
  if len(sList) == 0:
    print("There is nothing to delete, list is already empty!\n")
  else:
    attribute = input('Please provide your selection:\n1 - Task order (position)\n2 - Other attribute (Make sure that your provided attribute name is identical to records)\n->')

    if  attribute == '1':
      print("Please provide your desirable position: (range 1-"+str(len(sList))+')'+"\n-> ")
      pos = input()
      DeletePos(pos)
    elif attribute == '2':
      c = input('Enter your selection:\n1 - Name of task\n2 - Name of subject\n3 - Deadline of task\n')

      if c == '1':
        DeleteCr('Task', 'Enter name of the task:\n')
      elif c == '2':
        DeleteCr('Subject', 'Enter name of the subject:\n')
      elif c == '3':
        DeleteCr('Deadline', 'Enter deadline of the task:\n')
      else:
        print('That kind of selection does not exist')
    else:
      print("Error: none existing option")

def SearchByAttribute(update):
  if len(sList) == 0:
    print('Your list is empty')
  else: 
    att = input("Please provide your selection attribute:\n1 - Deadline\n2 - Name of the subject\n-> ")
    if att == '1':
      SearchRecord(update, 'Deadline', 'Enter the deadline:\n->')
    else:
      SearchRecord(update, 'Subject', 'Enter the name of the subject:\n-> ')
  
def SearchRecord(update, attribute, mess):
  print(mess)
  att = input()
  check = 0
  i = -1 # number of row

  for line in sList:
    check+=1
    i+=1
    if line[attribute] == att:
      if update == 1:
        print(line['Task'] + " " + line['Subject'] + ' ' + line['Deadline'] + ' ' + line['Description'])
        Update(sList[i]) # to update record
      else:
        print(line['Task'] + " " + line['Subject'] + ' ' + line['Deadline'] + ' ' + line['Description'])
      
      check = 0
    
  if check == len(sList):
    print('Error: there is no any records')

def Update(line):
  x = input('Please enter your attribute in order to update/change in your record:\n1 - Task name\n2 - Subject name\n3 - Deadline of the record\n4 - Description of the record\n-> ')

  if x == '1':
    line['Task'] = input("Enter your changes\n-> ")
  elif x == '2':
    line['Subject'] = input("Enter your changes\n-> ")
  elif x == '3':
    line['Deadline'] = input("Enter your changes (DD/MM/YYYY)\n-> ")
  else:
    line['Description'] = input("Enter your changes\n-> ")
  
def NearestTask():
  if len(sList) <= 0:
    print('Your list is empty')
  else:
    index = 0
    i=-1

    mini = datetime.strptime(sList[0]['Deadline'], '%d/%m/%Y')

    for date in sList:
      i+=1
      if mini > datetime.strptime(date['Deadline'], '%d/%m/%Y'):
        mini = datetime.strptime(date['Deadline'], '%d/%m/%Y')
        index = i
    
    print(sList[int(index)]['Task'], sList[int(index)]['Subject'], sList[int(index)]['Deadline'], sList[int(index)]['Description'])

def Sort():
  i=0
  while i+1 < len(sList):
    if datetime.strptime(sList[i]['Deadline'], '%d/%m/%Y') > datetime.strptime(sList[i+1]['Deadline'], '%d/%m/%Y'):

      node = {
        'Task': sList[i]['Task'],
        'Subject': sList[i]['Subject'],
        'Deadline': sList[i]['Deadline'],
        'Description': sList[i]['Description']
      }

      node_next = sList.nodeat(i) # higher element
      sList.remove(node_next)

      if i + 1 == len(sList): # If it is last element append
        sList.append(node)
      else:
        node_next = sList.nodeat(i) # If not last, insert to list
        sList.insertafter(node, node_next)
      i=0
    else:
      i+=1

def main():
  FileName = input('Enter name of the database:\n-> ')
  if os.path.exists(FileName+'.csv'):
    ReadFile(FileName+'.csv')

    while True:
      print('Upcoming task:')
      NearestTask()
      print('')
      selection = input('----MENU----\nPlease select your option:\n1 - Insert new record\n2 - Delete record\n3 - Search record\n4 - Update/Change record\n5 - Display whole list\n6 - Sort list by deadline\n7 - Clear whole list\n8 - Exit\n------------\n-> ')

      if selection == '1':
        Insertion()
        input('Press enter to move on!\n')
      elif selection == '2':
        Deletion()
        input('Press enter to move on!\n')
      elif selection == '3':
        SearchByAttribute(0)
        input('Press enter to move on!\n')
      elif selection == '4':
        SearchByAttribute(1)
        input('Press enter to move on!\n')
      elif selection == '5':
        Display()
        input('Press enter to move on!\n')
      elif selection == '6':
        Sort()
        input('Press enter to move on!\n')
      elif selection == '7':
        sList.clear()
        input('Press enter to move on!\n')
      else:
        break

    WriteFile(FileName+'.csv')
    sList.clear()
  else:
    x = input('File does not exist\nDo you want to create new (y/n)?\n-> ')
    # x = input()
    if x == 'y':
      name = input('Please enter name of the database\n-> ')
      open(name+'.csv', 'w')
      main()
    else:
      time.sleep(0)

# Execute the main menu
if __name__ == '__main__':
  main()