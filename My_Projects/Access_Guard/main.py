# Phase 1 -- Company Setup & Welcome Banner
tools = ["GitHub", "AWS", "Slack", "Jira", "Production Server", "HR Portal" ,"Figma","docker" ]

valid_roles = ("inter", "developer", "tester", "manager", "admin")

company_info =("PythonGurukhool", "Pune", 2018, "ISO 27001 Certified")

role_permissions = {
    "intern": ["Slack","Jira"],
    "developer":["GitHub","Slack","Jira", "AWS"],
    "tester": ["Slack", "Jira", "GotHub", "Docker"],
    "manager": ["GitHub","Slack","Jira", "AWS", "HR Portal"],
    "admin": ["GitHub","Slack","Jira", "AWS", "HR Portal", "Production Server", "Figma","Docker"],

}
employees = {
    "E101": {"name": "Aarav Sharma", "role": "developer",
             "access":["GitHub","Slack","Jira","AWS"]},
    "E102": {"name": "Sneha Patil", "role": "intern",
             "access":["Slack","Jira",]}
}
access_log = [
    ("E101", "GitHub", "GRANTED", "2025-01-15"),
    ("E102", "AWS","DENIED", "2025-02-10")
]


# Welcome Banner
print("=" * 60)
print(f"   {company_info[0]} | HQ: {company_info[1]} | Est: {company_info[2]} ")
print(f"   Security Standard: {company_info[3]}")
print("=" * 60)
print(f"   Total tools availble : {len(tools)}")
print(f"   Valid roles: {len(valid_roles)}")
print(f"   Employees registered: {len(employees)}")
print("=" * 60)

print(f"\nAvailble Tools: {tools}")
print(f"\nValid Roles: {valid_roles}")

print(f"\nRole Permission:")
print(f"   intern    --> {role_permissions['intern']}")
print(f"   developer --> {role_permissions['developer']}")
print(f"   tester    --> {role_permissions['tester']}")
print(f"   manager   --> {role_permissions['manager']}")
print(f"   admin     --> {role_permissions['admin']}")

print(f"\nExisting Employees:")
print(f"   E101 | {employees['E101']['name']} | {employees['E101']['role']}")
print(f"   E102 | {employees['E102']['name']}  | {employees['E102']['role']}")

print(f"\nAccess Log:")
print(f"   {access_log[0]}")
print(f"   {access_log[1]}")


#Phase 2 -- onboard a New Employee
#Collect & Validate Name
print("\n--- NEW EMPLOYEE ONBOARDING ---\n")

full_name = input("Enter full name: (First Last):").strip().title()

first_name = full_name.strip() [0]
last_name = full_name.strip() [-1]

name_check = full_name.replace(" ","")
if not name_check.isalpha():
  print("Name should contain only letters.")
else:
  print(f"Name accepted: {full_name}")

# Collect and validate Employee ID
emp_id = input("Enter Employee ID (e.g., E103):").strip().upper()

if not emp_id.startswith("E"):
  print("Employee ID must start with 'E'")
elif not emp_id[1:].isdigit():
  print("After 'E', only numbers should are allowed")
elif len(emp_id) != 4:
  print("Employee ID must be exactly 4 character (e.g., E103)")
else:
  print(f"ID accepted: {emp_id}")

#collect and validate role
print(f"\nAvailble roles: {valid_roles}")
role = input("Enter role:").strip().lower()

if role not in valid_roles:
  print(f"Invalid role. Choose from: {valid_roles}")
else:
  print(f"Role accepted: {role.title()}")



#Auto-generatre email amd passsword
email = first_name.lower() + "-" + last_name.lower() + "@pythongurukhool.com"
print(f"Auto-generated email: {email}")
temp_password = first_name[:3].lower() + emp_id[-3:] + "@TN"
print(f"Temporary password: {temp_password}")

#classify exprience
experience = int(input("years of experience:").strip())

if experience < 0:
  print("Experience cannot be negative.")
elif experience == 0:
  print("Fresher detected. Mentor will be assigned.")

elif experience <= 3:
  print("Junior level.")

elif experience <= 7:
  print("Mid level.")

else:
  print("Senior level.")


#Assign Access and store Employee
#Everyone starts with minimum access (intern-level)
# Access should be based on the assigned role, not always 'intern'
access = role_permissions[role].copy()

employees[emp_id] = {
    "name": full_name,
    "role": role,
    "access": access,
    "email": email
}
#permanant onboarding record (tuple)
onboard_record = (emp_id,full_name, role, "2025-08-08")


#ONboarding Summary
print(f"\n{'=' * 60}")
print(f"  ONBOARDING COMPLETE")
print(f"  Name     : {full_name}")
print(f"  Role     : {role}")
print(f"  Email    : {email}")
print(f"  password : {temp_password}") # Corrected typo
print(f"  access   : {', '.join(access)}") # Corrected string join syntax
print(f"  Note     : Default minimum access granted.")
print(f"{'=' * 60}")
print(f"  Permanant Record: {onboard_record}")
print(f"  record type: {type(onboard_record)}")
print(f"{'=' * 60}")


 # Phase 3-- Access Request Portal
print("\n--- ACCESS REQUEST PORTAL ---")
print(f"Registered Employee IDs: {employees.keys()}")
requestor_id = input ("Enter your Employee ID:").strip().upper()
# Safe lookup using .get()
emp = employees.get(requestor_id)
if emp is None:
  print(f"No employee found with ID: {requestor_id}")
else:
  print(f"\nWelcome {emp['name']}!")
  print(f"Current role: {emp['role'].title()}")
  print(f"Current access: {emp['access']}")


  print(f"\nAll company tools: {tools}")
  requested_tool = input("\nWhich tools do you need?").strip()

  #check 1: Does the tool exist?
  if requested_tool not in tools:
    print(f"Tool doesn't exist. Available: {tools}")


  #check 2: Already has the access?
  elif requested_tool in emp["access"]:
    position = emp["access"].index(requested_tool)
    print(f"You already have {requested_tool} "
          f"(position: {position + 1})")

  #check 3: Role permits it?
  elif requested_tool not in role_permissions.get(
      emp["role"], []):
    print(f"Access Denied. {emp['role'].title()} "
          f"not permitted to use {requested_tool}.")
    denial_log = (requestor_id, requested_tool,
                  "DENIED", "2025-08-08")
    access_log.append(denial_log)

  # All checks passed -- grant access
  else:
    emp["access"].append(requested_tool)
    grant_log = (requestor_id, requested_tool,
                 "GRANTED", "2025-08-08")
    access_log.append(grant_log)
    print(f"Access to {requested_tool} granted!")
    print(f"Updated access: {emp['access']}")


    # Phase 4 -- tool audit and comparion (sets)
aarav_access = set(employees['E101']["access"])
sneha_access = set(employees['E102']["access"])

# 1. common tools (intersection)
common = aarav_access & sneha_access
print(f"tools BOTH have: {common}")

# 2. only Aarav has (differrence)
aarav_extra = aarav_access - sneha_access
print(f" Only Aarav has: {aarav_extra}")

# 3. only Sneha has (differrence)
sneha_extra = sneha_access - aarav_access
print(f" Only Sneha has: {sneha_extra}")

# 4. Combined access (union)
combined = aarav_access | sneha_access
print(f"Combined access: {combined}")

#5 . Exclusive tools (symmetric diffrence)
exclusive = aarav_access ^ sneha_access
print(f"Exclusive tools: {exclusive}")

# 6. Unused tools
all_tools = set(tools) # Define all_tools to be used below
unused_tools = all_tools - combined
print(f"UNUSED tools: {unused_tools}")
print(f"Company paying for {len(unused_tools)} unused tool(s)!")


if sneha_access.issubset(aarav_access):
  print("Sneha's access is a subset of Aarav's access.")
if aarav_access.issuperset(sneha_access):
  print("Aarav's access is a SUPERSET of Sneha's access.")
if not aarav_access.isdisjoint(sneha_access):
  print("Their access overlaps(not disjoint)")


tools_set = set(tools)

# .add()
tools_set.add("Kubernetes")

# .add() duplicate -- ignored silently
tools_set.add("Slack") #NO error , no duplicate

# .discard() -- safe removal
tools_set.discard("Figma")

# .discard() on non-existent -- no error
tools_set.discard("RandomTool") #safe!

# .remove() would crash if item missing
# tools_set.remove("RandomTool") #KeyError - commented out to avoid crashing

# .pop() -- removes a random element
poped = tools_set.pop()

# .clear()
temp_set = {"a", "b", "c"}
temp_set.clear() #Now empty set()


#DEduplication demo
buggy_list = ["Slack", "Jira", "Slack", "GitHub", "Jira"]
print(f"Buggy list: {buggy_list} (length: {len(buggy_list)})")

clean_list = list(set(buggy_list))
print(f"Cleaned: {clean_list} (length: {len(clean_list)})")


# Phase 5-- Revoke Access & Log Analysis
#Revoke access

emp_id = input("Enter Employee ID:").strip().upper()
emp = employees.get(emp_id)

if emp is None:
  print("Employees not found.")
else:
  print(f"Current access: {emp['access']}")
  tool = input("Tools to revoke: ").strip()

  if tool not in emp["access"]:
    print(f"{emp['name']} doesn't have {tool}.")
  else:
    pos = emp["access"].index(tool)
    print(f"found '{tool}' at position {pos}")

    emp['access'].remove(tool)
    print(f"{tool} access revoked.")
    print(f"Updated access: {emp['access']}")

    revoke_log = (emp_id, tool, "REVOKRD", "2025-08-08")
    access_log.append(revoke_log)


#Log Analysis
# Total entries
print(f"Total log entries: {len(access_log)}")

#First and last entry
print(f"First entry: {access_log[0]}")
print(f"Last entry: {access_log[-1]}")

#Last 3 entries (slicing)
print(f"Recent 3 entries: {access_log[-3:]}")

# Sorted copy (does NOT modify original)
sorted_log = sorted(access_log)

# Reversed copy -- .copy() fisrt, then .reverse()
reversed_log = access_log.copy()
reversed_log.reverse()

#pop last entry from reverswd copy
popped_entry = reversed_log.pop()

# Insert audit marker at position 0
audit_marker = ("SYSTEM", "AUDIT", "STAETED", "2025-08-08")
access_log.insert(0, audit_marker)



# Phase 6--update Employees record
emp_id = input("Employee ID to update: ").strip().upper()
emp = employees.get(emp_id)

if emp is None:
  print("Employee not found.")
else:
  print(f"Fields: {list(emp.items())}")
  print(f"Availble fields: {list(emp.keys())}")

  #--- ROLE UPDATE ---
  new_role = input(f"Enter new role (or Enter to skip): ").strip().lower()
  if new_role != "":
    if new_role not in valid_roles:
      print(f"Invalid role. Choose from: {valid_roles}")
    else:
      emp.update({
          "role": new_role,
          "access": role_permissions[new_role].copy()

      })
      print(f"Role updated to: {new_role.title()}")


# --- ADD PHONE ---
emp.setdefault("phone", "Not provided")
phone = input("Enter Phone (or Enter to skip):").strip()
if phone != "":
  if len(phone) != 10 or not phone.isdigit():
    print("Phone must be exactly 10 digits.")

  else:
    emp["phone"] = phone
# --- REMOVE A FIELD ---
remove_field = input("Remove a field? ").strip()
if remove_field != "":
  removed = emp.pop(remove_field, "Field not found")
  print(f"Removed '{remove_field}': was '{removed}'")

# --- FINAL DISPLAY ---
print(f"Keys   : {emp.keys()}")
print(f"Values : {emp.values()}")



# Phase 7 -- clone an employee record
#list copy using .copy()

aarav_access = employees["E101"]["access"]

# copy using .copy()
riya_access = aarav_access.copy()

# add to riya ONLY
riya_access.append("Production Server")

print(f"Riya's access : {riya_access}")
print(f"Aarav's access: {aarav_access}")
print("Aarav's list is unaffected!")

#prove they are independent
print(f"same objects? {riya_access is aarav_access}") #false


#Alternative copy Methods

original = ["GitHub", "Slack", "Jira"]

copy_1 = original.copy()
copy_2 = list(original)
copy_3 = original[:]

# All three are indepent copy 
print(f"copy_1 is original? {copy_1 is original}")
print(f"copy_2 is original? {copy_2 is original}")
print(f"copy_3 is original? {copy_3 is original}")


#dict copy with inner list
#Safe backup -- .copy() dict AND .copy() inner list
aarav_backup = employees["E101"].copy() # Shallow copy of the dictionary
aarav_backup["access"] = employees ["E101"] ["access"].copy() # Deep copy of the 'access' list

#modify
aarav_backup["access"].append("Figma")

print(f"Backup access  : {aarav_backup['access']}")
print(f"Original access: {employees['E101']['access']}")
print(f" Original is unafffected! Both independent.")


# Phase 8 -- Final Dashboard and Report

title = "ACCESS GUARD - FINAL REPORT"
print(title.center(60, "="))

#Employee Table
print(f"\n{'ID': <8}{'Name':<20}{'Role':<12}{'Tools':<50}") 
print("-" * 90) 


emp = employees["E101"]
print(f"{'E101':<8}{emp['name']:<20}"
      f"{emp['role'].upper():<12}"
      f"{len(emp['access']):<3} {' \\ '.join(emp['access'])}")

# --- repeat for E102, E103 ---

print("Total Employees", len(employees), sep="=", end=" | ")
print("Total Tools",len(tools), sep=": ",end=" | " )
print("Log Entries", len(access_log), sep=": ")

# Access Log Table
print(f"\n{'ACCESS LOG' .center(55, '-')}")
print(f"{'Emp ID': <10}{'Tool':<30}{'Status':<12}{'Date'}")
print("-" * 55)

log = access_log [0]
print(f"{log[0]:<10}{log[1]:30}{log[2]:<12}{log[3]}")
# --- repaet for more entries ---

# Footer
print(f"\n{'Report generated by AccessGuard v1.0'.center(60)}")
print(f"{'Confidential - Internal Use Only'.center(60)}")