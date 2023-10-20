import helper


participants = []
while True:
    user_input = input("insert 'reg' o enroll,'info' to get your information,'admin' enter admin control panel: ").lower()
    if user_input == "reg":
        while True:
            lec_check = input("Are you a lecturer ? (Yes or No)").lower()
            if lec_check == "yes":
                lec = helper.get_lecturer_info()
                participants.append(lec)
                break
            else:
                std = helper.get_student_info()
                participants.append(std)
                break
            
                
                     
    elif user_input == "info":
        while True:
            participant = int(input("Please Enter your code:"))
            for participant in participants:
                if participant.code:
                    print(f"Code = {participant.code} , Name = {participant.name} , Family = {participant.family}")
            
            
                    
    elif user_input == "admin":
        check = int(input("Enter your password : "))
        if check == 0000:
            
            helper.creat_json(participants)
            
            helper.creat_csv(participants)
        
                          
                    
    else:
        print("Wrong Option!")          
