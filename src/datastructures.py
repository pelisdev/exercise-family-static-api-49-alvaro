from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "first_name":"John",
            "id":self._generateId(),
            "age":33,
            "lucky_numbers":[7,13,22]
        },
        {
            "first_name":"Jane",
            "id":self._generateId(),
            "age":35,
            "lucky_numbers":[10,14,3]
        },{
            "first_name":"Jimmy",
            "id":self._generateId(),
            "age":5,
            "lucky_numbers":[1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member_id = {
            'id':member.get('id', self._generateId()),
            'last_name':self.last_name
        }
        member.update(member_id)
        self._members.append(member)
        return member

    def delete_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                self._members.remove(member)
                return {"done": True}
        return None, 404

    def get_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                return member
        return None, 404

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        if not self._members:
            return [], 200
        return self._members