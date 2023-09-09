import re
import json
import os
import sys
import getpass
import bcrypt
from tabulate import tabulate
from rich import print
from rich.prompt import Prompt
from termcolor import colored
import pyfiglet

print('\n')
ascii_art = pyfiglet.figlet_format("Crowd Funding", font="standard")
# Add color (green) to the text art
colored_ascii_art = colored(ascii_art, "green")
# Print the colored text art
print(colored_ascii_art)

def validate_date_func(date):
    pattern = r'^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-\d{4}$'
    if re.match(pattern, date):
        return True
    else:
        return False

def valtotal(total):
    if total.isdigit():
        return True
    else:
        return False

def validate_phone_func(phone):
    pattern = r'^(011|010|012|015)\d{8}$'
    if re.match(pattern, phone):
        return True
    else:
        return False

def validate_password_func(password, confirm_password):
    if password == confirm_password:
        return True
    else:
        return False

def validate_email_func(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if  re.match(regex, email):
        return True
    else:
        return False

class Authentication :
    def __init__(self, first_name, last_name, age, phone, email, password, confirm_password):
        self.password = password
        self.confirm_password = confirm_password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id=self.email=email
        self.email = email
        self.phone = phone

    def save_to_dict(self):
            return self.__dict__

    def dump_to_json(self):
        data = []
        try:
            
            with open('ff.json', 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            pass
        # Check if the email already exists in the data
        if not any(item['email'] == self.email for item in data):
            data.append(self.save_to_dict())
            with open('ff.json', 'w') as file:
                json.dump(data, file, indent=4)
        else:
            print("Email already exists")
            print("Enter your email and password")
            emaill = input("Enter your email: ")
            passwordd = getpass.getpass("Enter your password: ")
            login = Login(emaill, passwordd)

class Create_project:
    def __init__(self,user_id, title, details, total_target, start_date, end_date):
        self.user_id=user_id
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date

    def save_to_dict(self):
        return self.__dict__

    def dump_to_json(self):
        data=[]
        try:
            with open('fff.json', 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            pass
        data.append(self.save_to_dict())
        with open('fff.json', 'w') as file:
            json.dump(data, file, indent=4)

class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate_login(self):
        data = []
        try:
            with open('ff.json', 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            pass
        for item in data:
            if item['password']==self.password and item['email']==self.email:
                return True
        return False

    def print_t(self, item):
        project_data = {
        "Title": item["title"],
        "Details": item["details"],
        "Total Target": item["total_target"],
        "Start Date": item["start_date"],
        "End Date": item["end_date"]
        }
    
        table = tabulate([project_data], headers="keys", tablefmt="pretty")
        print(f'[green]{table}[/green]')

    def show_projects(self):
            with open('fff.json', 'r') as file:
                data = json.load(file)
            for item in data:
                if item['user_id'] == self.email:  # Assuming user_id corresponds to email
                    self.print_t(item)

    def delete_project(self, title):
            with open('fff.json', 'r') as file:
                data = json.load(file)
            for item in data:
                if item['user_id'] == self.email:
                    for idx ,obj in enumerate(data):
                        if obj['title'] == title:
                            data.pop(idx)
                            break
            with open('fff.json', 'w') as file:
                json.dump(data, file, indent=4)
            print("Project deleted successfully")

    def edit_project(self,what_to_edit,name,value):
            with open('fff.json', 'r') as file:
                data = json.load(file)
            for item in data:
                if item['user_id'] == self.email:
                    for idx ,obj in enumerate(data):
                        if obj['title'] == name:
                            data[idx][what_to_edit] = value
                            break
            with open('fff.json', 'w') as file:
                json.dump(data, file, indent=4)
            print("Project edited successfully")

    def search_project(self,start_date,end_date):
            with open ('fff.json','r')as file:
                data=json.load(file)
            for item in data:
                if item['user_id']==self.email:
                    for idx,obj in enumerate(data):
                        if obj['start_date']==start_date and obj['end_date']==end_date:
                            self.print_t(item)
                            break
while True:
    options={
        "1":"Register",
        "2":"Login",
        "3":"Exit"
    }
    table_options=tabulate([options],headers="keys",tablefmt="fancy_grid")
    print(table_options)
    option = input("Enter your option: ")
    
    if option == "1":
        name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        age = int(input("Enter your age: "))
        phone = input("Enter your phone: ")

        if(validate_phone_func(phone) == False):
            print("[bold red]Invalid phone number[/bold red]")
            phone = input("Enter your phone: ")

        email = input("Enter your email: ")

        if(validate_email_func(email) == False):
            print("[bold red]Invalid email[/bold red]")
            email = input("Enter your email: ")

        password = getpass.getpass("Enter your password: ")
        confirm_password = getpass.getpass("Confirm your password: ")
        if(validate_password_func(password, confirm_password) == False):
            print("[bold red]Invalid password[/bold red]")
            password = getpass.getpass("Enter your password: ")
            confirm_password = getpass.getpass("Confirm your password: ")
        user = Authentication(name, last_name, age, phone, email, password, confirm_password)
        user.dump_to_json()
        print("[yellow]User created successfully[/yellow]")

    elif option == "2":
        print("Login to your account")
        email = input("Enter your email: ")
        password = getpass.getpass("Enter your password: ")
        login = Login(email, password)
    else:
        break
    
    options_b={
        "1":"Create project",
        "2":"Show projects",
        "3":"delete_project",
        "4":"Exit",
        "5":"edit_project",
        "6":"search_project"
    }
    table_options_b=tabulate([options_b],headers="keys",tablefmt="fancy_grid")
    print(table_options_b)
    option = input("Enter your option: ")

    if option == "1":
        title = input("Enter your title: ")
        details = input("Enter your details: ")
        total_target = input("Enter your total target: ")
        if(valtotal(total_target) == False):
            print("[bold red]Invalid total target[/bold red]")
            total_target = input("Enter your total target: ")
        start_date = input("Enter your start date (MM-DD-YYYY): ")
        end_date = input("Enter your end date (MM-DD-YYYY): ")
        if(validate_date_func(start_date) == False):
            print("[bold red]Invalid date[/bold red]")
            start_date = input("Enter your start date (MM-DD-YYYY): ")
        if(validate_date_func(end_date) == False):
            print("[bold red]Invalid date[/bold red]")
            end_date = input("Enter your end date (MM-DD-YYYY): ")
        project = Create_project(email, title, details, total_target, start_date, end_date)
        project.dump_to_json()
        print("Project created successfully")

    elif option == "2":
        login.show_projects()

    elif option == "4":
        break

    elif option == "3":
        login.delete_project(input("Enter the title of the project you want to delete: "))

    elif option == "5":
        login.edit_project(input("enter the name of the attribute you want to edit: "),input("Enter the title of the project you want to edit: "),input("Enter the name of the attribute you want to edit: "))
    elif option == "6":
        login.search_project(input("Enter the start date: "),input("Enter the end date: "))