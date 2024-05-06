from generateTemps import generateTemps

# initiating optimization variables
steady_state = False
on_count = 0
off_count = 0
timer_th = 2 #hours
curr_hour = 24
oa_t, oa_t_pred = generateTemps()

def machine_command(curr_temp,future_temp):
    if curr_temp < 5:
        if steady_state == True:
            return 0
        else:
            return 1
    else:
        if steady_state == True:
            return 1
        else: 
            return 0
        
epoch = 0

while True:
    opstat = int(input("enter machine status: "))
    future_hour = curr_hour + 1

    if curr_hour > 23:
        curr_hour = curr_hour%24
    
    if future_hour > 23:
        future_hour = future_hour%24

    curr_temp = oa_t[curr_hour]
    future_temp = oa_t_pred[future_hour] 
    try:
        if opstat == 1:
            on_count += 1
            off_count = 0
        elif opstat == 0:
            off_count += 1
            on_count = 0
        else:
            print("invalid opstat input")
            break

        if off_count or on_count >= timer_th:
            steady_state = True
        else:
            steady_state = False

        print("")
        print("curr_hour: " + str(curr_hour))
        print("curr_temp: " + str(curr_temp))
        print("future_temp: " + str(future_temp))
        print("")
        print("opstat: " + str(opstat))
        print("on_count: " + str(on_count))
        print("off_count: " + str(off_count))
        print("steady_state: " + str(steady_state))
        print("")
        print("sending machine status: " + str(machine_command(curr_temp,future_temp)))

        if machine_command != None:
            epoch += 1
            curr_hour += 1
        
        print("epoch: " + str(epoch))
        print("##########################################################")

    except:
        break

