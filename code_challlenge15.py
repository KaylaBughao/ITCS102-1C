import os 
import json

os.system('cls')
print('DLL STUDENT INFORMATION SYSTEM')
print('================================================')

stud_record = {} #empty dictionary

while True:

    print("SELECT FROM THE FOLLOWING OPTIONS ")
    print("A = Adding Student Record ")
    print('B - Search Student ')
    print('C - Edit Student Record')
    print('D - Delete Student Record')
    print('E - Print All Record')
    print('F - Export Data')
    print('G - Exit System')

    choice = input("Input your choice --- , ").lower().strip()

    if choice == 'a':
        os.system('cls')
        print("ADD STUDENT RECORD")

        student_id = input("Input student ID number")
        first_name = input("Input student First Name ").upper()
        last_name = input("Input student last name").upper()
        course = input("Input student Course").upper
        section = input("Input Student Course").upper
        email = input("Input Student Email")
        #transferring input to a dictionary
        
        stud_record[student_id] = [first_name, last_name, course, section, email ]
        print("DATA SAVED SUCCESSFULLY")

        continue
    elif choice == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD")
        print("======================================== ")

        for id, info in stud_record.items():
            print(f"STUDENT ID {id} - RECORD - {info}")

    elif choice == 'c':
        os.system('cls')
        print("SEARCH STDENT RECORD")

        search_id = input("INPUT STUDENT ID ----- > ").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():

                print("NO RECORD FOUND")
 
         
    elif choice == 'd':
        os.system('cls')
        print("DELETE STUDENT RECORD")

        search_id = input("INPUT STUDENT ID ---- >   ").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"\n\nRECORD FOUND for {search_id}")
                print(" =============================   ")
                for id in stud_record[search_id]:
                    print(f" --{id}  ")

                print(" =======================================  ")

                stud_record.pop(search_id)
                print("RECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue


    elif choice == 'e':
        os.system
        print("EDIT / MODIFY STDENT RECORD")

        search_id = input("INPUT STUDENT ID ---- >").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"\n\nRECORD FOUND for {search_id}")
                print(" ==============================  ")
                for id in stud_record[search_id]:
                    print(f" --{id} ")
                print(" =============================== ")  

                #ask new values
                first_name = input("Input NEW student First Name -->").upper()
                last_name = input("Input NEW student last name -->").upper()
                course = input("Input NEWStudent Course --> ").upper()
                section = input("Input NEW Student section -->")


                stud_record[search_id][0] = first_name
                stud_record[search_id][1] = last_name
                stud_record[search_id][2] = course
                stud_record[search_id][3] = section
                stud_record[search_id][4] = email
                print("DATA UPDATED SUCCESSFULLY")

            else:
                print("NO RECORD FOUND")
            break
        continue

    elif choice == 'f':
        print("EXPORT DATA ")

        with open('crush_record.json','w') as new_file:
            json.dump(stud_record, new_file, indent=4)
            
        print("DATA EXPORTED SUCCESSFULLY")
        continue

    elif choice == 'g':
        print("EXIT SYSTEM")
        break
    else:
        print("Invalid Choice, Re-enter code ")
        continue