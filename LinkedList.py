#creating node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating the linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    #check if the list is empty
    def is_empty(self):
        return self.head is None

    #append new element in list
    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    #prepend in the list
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    #deleting node
    def delete_node(self,key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None
    
    #displaying the linked list
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data,end='->')
            current_node = current_node.next
        print("None")         

#menu
def menu():
    print("\nMenu:")
    print("1. Append to the linked list")
    print("2. Prepend to the linked list")
    print("3. Delete a node from the linked list")
    print("4. Display the linked list")
    print("5. Exit")


linked_list = LinkedList()

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        data = int(input("Enter the data to append: "))
        linked_list.append(data)
    elif choice == "2":
        data = int(input("Enter the data to prepend: "))
        linked_list.prepend(data)
    elif choice == "3":
        data = int(input("Enter the data to delete: "))
        linked_list.delete_node(data)
    elif choice == "4":
        linked_list.display()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    