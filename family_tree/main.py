

class Nodes:
    def __init__(self):
        self.parents_list = []
        self.children_list = []
        self.sibling_list = []
        self.current_spouse = None


    def add_parent(self,parent):
        if len(self.parents_list) >= 2:
            print("too many parents")
        else:
            self.parents_list.append(parent)


    def add_child(self,child):
        for i in child:
            self.children_list.append(i)
            i.add_parent(self)


    def add_spouse(self,spouse):
        self.current_spouse = spouse


    def add_sibling(self,sibling):
        for i in sibling:
            self.sibling_list.append(i)


    def return_parent(self):
        if len(self.parents_list) == 0:
            return "no parents"
        else:
            temp_list = []
            for parent in self.parents_list:
                temp_list.append(parent)
            return temp_list


    def return_child(self):
        if len(self.children_list) == 0:
            return "no children"
        else:
            temp_list = []
            for child in self.children_list:
                temp_list.append(child)
            return temp_list


    def return_grandchild(self):
        if not self.children_list:
            return "no grandchildren"

        temp_list = []
        for child in self.children_list:
            if not child.children_list:
                continue
            for grand_child in child.children_list:
                temp_list.append(grand_child)

        if not temp_list:
            return "no grandchildren"

        return temp_list


    def return_sibling(self):
        if len(self.sibling_list) == 0:
            return "no siblings"
        else:
            temp_list = []
            for sibling in self.sibling_list:
                temp_list.append(sibling)
            return temp_list


    def return_spouse(self):
        if self.current_spouse is None:
            return "no spouse"
        else:
            return self.current_spouse


    def return_all_related(self):
        related_members = []

        # Recursion used to go through every family member
        def collect_relations(f_member):
            if f_member not in related_members:
                if f_member != self:
                    related_members.append(f_member)

                for parent in f_member.parents_list:
                    collect_relations(parent)
                for child in f_member.children_list:
                    collect_relations(child)
                for sibling in f_member.sibling_list:
                    collect_relations(sibling)


        collect_relations(self)

        return related_members



class FamilyMember(Nodes):
    def __init__(self, name, age, dob, gender):
        super().__init__()
        self.name = name
        self.age = age
        self.dob = dob
        self.gender = gender



F1_1 = FamilyMember("1_1",25, "1/1/1999", "female")
F1_2 = FamilyMember("1_2",24, "1/1/2000", "male")
F1_3 = FamilyMember("1_3",50, "1/1/1974","female")
F1_4 = FamilyMember("1_4",49, "1/1/1975", "male")
F1_5 = FamilyMember("1_5",5, "1/1/2019", "female")
F1_6 = FamilyMember("1_6",4, "1/1/2020", "male")
F1_7 = FamilyMember("1_7",6, "1/1/2018", "female")
F1_8 = FamilyMember("1_8",8, "1/1/2017", "male")
F1_9 = FamilyMember("1_9",26, "1/1/1998", "male")
F1_10 = FamilyMember("1_10",27, "1/1/1997", "female")

F1_1.add_spouse(F1_2)
F1_3.add_spouse(F1_4)
F1_9.add_spouse(F1_10)

F1_1.add_child((F1_5,F1_6))
F1_2.add_child((F1_5,F1_6))
F1_3.add_child((F1_1,F1_10))
F1_4.add_child((F1_1,F1_10))
F1_9.add_child((F1_7,F1_8))
F1_10.add_child((F1_7,F1_8))

F1_1.add_sibling((F1_10,))
F1_5.add_sibling((F1_6,))
F1_6.add_sibling((F1_5,))
F1_7.add_sibling((F1_8,))
F1_8.add_sibling((F1_7,))

family_members = {
    "1_1": F1_1,
    "1_2": F1_2,
    "1_3": F1_3,
    "1_4": F1_4,
    "1_5": F1_5,
    "1_6": F1_6,
    "1_7": F1_7,
    "1_8": F1_8,
    "1_9": F1_9,
    "1_10": F1_10,
}



Running = True
while Running:
    option = input("""
    Enter what you would like to do:
    1) Print all children of a member
    2) Print all parents of a member
    3) Print all grandchildren of a member
    4) Print immediate family
    5) Print extended family
    6) Exit the program
    """)


    if option == "1":
        member_name = input("Enter a name:")
        member = family_members.get(member_name)
        if member:
            children = member.return_child()
            if children != "no children":
                print(f"Children of {member_name}:")
                for c in children:
                    print(c.name)
            else:
                print(children)  # Print "no children"
        else:
            print("No person found with that name.")


    elif option == "2":
        member_name = input("Enter a name:")
        member = family_members.get(member_name)
        if member:
            parents = member.return_parent()
            if parents != "no parents":
                print(f"Parents of {member_name}:")
                for p in parents:
                    print(p.name)
            else:
                print(parents)
        else:
            print("No person found with that name.")


    elif option == "3":
        member_name = input("Enter a name:")
        member = family_members.get(member_name)
        if member:
            g_children = member.return_grandchild()
            if g_children != "no grandchildren":
                print(f"Grandchildren of {member_name}:")
                for g_c in g_children:
                    print(g_c.name)
            else:
                print(g_children)
        else:
            print("No person found with that name.")


    elif option == "4":
        member_name = input("Enter a name:")
        member = family_members.get(member_name)
        if member:

            # Get children
            children = member.return_child()
            if children != "no children":
                print(f"Children of {member_name}:")
                for c in children:
                    print(c.name)
            else:
                print(children)

            # Get parents
            parents = member.return_parent()
            if parents != "no parents":
                print(f"Parents of {member_name}:")
                for p in parents:
                    print(p.name)
            else:
                print(parents)

            # Get siblings
            siblings = member.return_sibling()
            if siblings != "no siblings":
                print(f"Siblings of {member_name}:")
                for s in siblings:
                    print(s.name)
            else:
                print(siblings)

    elif option == "5":
        member_name = input("Enter a name:")
        member = family_members.get(member_name)
        if member:
            related_members = member.return_all_related()
            if related_members:
                print(f"Extended family of {member_name}:")
                for rm in related_members:
                    print(rm.name)
            else:
                print(f"No family members found for {member_name}.")
            spouse = member.return_spouse()
            if spouse != "no spouse" and spouse not in related_members:
                print("Spouse is:",spouse.name)
            elif spouse == "no spouse":
                print("No spouse")


        else:
            print("No person found with that name.")



    elif option == "6":
        Running = False
        print("Exiting the program")


