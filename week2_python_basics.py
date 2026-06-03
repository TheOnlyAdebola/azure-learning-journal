name = "Adebola"
week = 2
is_student = True
score = 87.5

def greet_student(name):
    print(f"Welcome to CloudOps, {name}!")

print(name)
print(week)
print(is_student)
print(score)
students = ["Adebola", "Chidi", "Fatima", "Emeka", "Ngozi"]
for student in students:
    greet_student(student)
count = 1
while count < 6:
    print(count)
    count = count + 1
beauty = "girl"
if beauty == "girl":
    print("A beautiful girl")
elif beauty == "boy":
    print("A beautiful boy")
print(f"My name is {name} and I am in Week {week}.")
def greet_student(name):
    print(f"Welcome to CloudOps, {name}!")

greet_student("Adebola")
greet_student("Chidi")
greet_student("Fatima")
def check_vm(vm_name):
    print(f"Checking Azure VM: {vm_name}")
check_vm("my-azure-vm-01")
# ── LAB 5: Cloud Cost Calculator Function ──
def calculate_cost(vm_name, hourly_rate):
    daily_cost = hourly_rate * 24
    monthly_cost = daily_cost * 30
    print(f"{vm_name} daily cost: ${daily_cost}")
    print(f"{vm_name} monthly cost: ${monthly_cost}")

calculate_cost("my-azure-vm-01", 2)
calculate_cost("my-azure-storage-01", 5)