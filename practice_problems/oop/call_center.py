# Call Center: Imagine you have a call center with 
# three levels of employees: respondent, manager, and director. 
# An incoming telephone call must be first allocated to a respondent who is free. 
# If the respondent can't handle the call, he or she must escalate the call to a manager. 
# If the manager is not free or not able to handle it, then the call should be escalated to a director. 
# Design the classes and data structures for this problem. 
# Implement a method dispatchCall() which assigns a call to the first available employee.

# CallCenter class => Has Employees in it
# Employee Class => Call Center Employee
# Respondent -> Subclass of Employee
# Manager -> SubClass of Employee, Manager manages Respondents
# Director -> SubClass of Employee, Director manages Managers
# CallCenter has 5 directors
# Each Director manages 20 Managers
# Each Manager manages 30 Respondents
import names, uuid, time, random


class CallCenter(object):
    def __init__(self):
        self.director = 5
        self.director_list = []
        self.manager = 20
        self.all_manager_list = []
        self.respondents = 30
        self.all_respondent_list = []
        self.organize_employee_structure()

    def organize_employee_structure(self):
        for i in range(self.director):
            d = Director(names.get_full_name(), uuid.uuid4())
            self.director_list.append(d)
        for i in range(self.director):
            manager_list = [Manager(names.get_full_name(), uuid.uuid4()) for x in range(self.manager)]
            director = self.director_list[i]
            director.add_manager_team(manager_list)
            director.set_director_level()
            self.all_manager_list += manager_list
        for i in range(self.manager):
            respondent_list = [Respondent(names.get_full_name(), uuid.uuid4()) for x in range(self.respondents)]
            manager = self.all_manager_list[i]
            manager.add_respondent_team(respondent_list)
            manager.set_manager_level()
            self.all_respondent_list += respondent_list

    def get_employee_count(self):
        return len(self.all_manager_list) + len(self.director_list) + len(self.all_respondent_list)

    def handle_call(self):
        respondent = random.choice(self.all_respondent_list)
        respondent.take_call(uuid.uuid4())

class Employee(object):
    def __init__(self, name=None, employee_id=None):
        self.name = name
        self.employee_id = employee_id
        self.boss = None
        self.team_limit = None
        self.team = []
        self.on_call = False
    
    def is_busy(self):
        return self.on_call
    
    def take_call(self, uuid):
        if not self.on_call:
            self.on_call = True
            print("{} has taken the call id: {}".format(self.name, uuid))
        else:
            print("{} cannot take the call now, busy with another call".format(self.name))
            self.send_to_boss(self, uuid)

    def manage_call(self, uuid):
        for employee in self.team:
            if not employee.on_call:
                employee.take_call(uuid)
                print("{} is Assigning call to Employee {}".format(self.boss.name, employee.name))
                break
        #self.boss.manage_call(uuid)

    def send_to_boss(self, employee, uuid):
        if employee.boss:
            print("{} is Sending Call to Boss {}".format(employee.name, employee.boss.name))
            employee.boss.manage_call(uuid)
        else:
            print("All Lines are Busy, We apologize")

class Respondent(Employee):
    def assign_manager(self, manager):
        if not self.boss:
            self.boss = manager

class Manager(Employee):
    def add_respondent_team(self, respondent_list):
        self.team_limit = 30
        if len(self.team) < self.team_limit:
            self.team = respondent_list
    
    def set_manager_level(self):
        for x in self.team:
            x.boss = self

class Director(Employee):
    def add_manager_team(self, manager_list):
        self.team_limit = 20
        if len(self.team) <= self.team_limit:
            self.team = manager_list

    def set_director_level(self):
        for x in self.team:
            x.boss = self

call_center = CallCenter()
#print(call_center.get_employee_count())
for i in range(400):
    call_center.handle_call()
    time.sleep(1)
