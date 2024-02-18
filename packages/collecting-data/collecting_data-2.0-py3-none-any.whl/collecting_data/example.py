import json
import os

def node():
    while True:
        Username = input("Enter Username: ")
        Password = input("Enter Password: ")
        if Username == "Ectron" and Password == "Ectron@123":
            with open("flow1.json", "r") as file:
                read = json.load(file)
                print(read)
            with open("ports1.json", "r") as file1:
                read1 = json.load(file1)
                print(read1)

            dir = os.getcwd()
            file_name = 'flow.json'
            file_name1 = "ports.json"
            file_path = os.path.join(dir, file_name)
            file_path1 = os.path.join(dir, file_name1)

            with open(file_path, 'w') as file:
                json.dump(read, file, indent=2)

            with open(file_path1, 'w') as file1:
                json.dump(read1, file1, indent=2) 

            print(f"Data written to {file_path}")
            print(f"Data written to {file_path1}")
            break
        else:
            print("Incorrect username or password")