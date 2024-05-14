
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

    def get_member(self, id):
        for member in self._members:
            if member['id'] == int(id):
                return member
        return {"Error!": f"Could not retrieve. No such member: {id}"}
    
    def add_member(self, member):
        id = self._generateId()
        member['id'] = id
        self._members.append(member)
        return member

    def delete_member(self, id):
        for member in self._members:
            if member['id'] == int(id):
                self._members.remove(member)
        return {"Error!": f"Could not delete. No such member: {id}"}