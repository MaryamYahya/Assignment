list=['ali','atefeh','reza','homa','amir','fatemeh']
print(list)

for i in range(3):
    person_number=int(input("\n Please select your preferred location:"))
    person_name=input("please enter the your name:")
    list.insert(person_number,person_name)

print(list)