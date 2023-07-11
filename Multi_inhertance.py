#Multi-level Inrehitance

class manager():

    def __init__(self, Team_lead, developer):
        self.lead = Team_lead
        self.dev = developer

    def Task(self):
        print(self.lead)
        print(self.dev)

class Testing(manager):
    def __init__(self, Team_lead, developer, Tester):
        self.test = Tester

        manager.__init__(self,Team_lead, developer)

    def bug_test(self):
        print(self.test)

class production(Testing):
    def __init__(self, Team_lead, developer, Tester, client):
        self.cl = client

        Testing.__init__(self, Team_lead, developer, Tester)

    def issue(self):
        print( self.cl )

project = production('lead operatation', 'devlope project', 'bug identify', 'projecrt issued by client')
project.Task()
project.bug_test()
project.issue()