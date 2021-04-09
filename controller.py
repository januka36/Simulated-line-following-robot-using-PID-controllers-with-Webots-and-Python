"""Tread O Quest - Team JAMAGA"""

from controller import Robot
from controller import LED

robot = Robot()
timestep = int(robot.getBasicTimeStep())

motor_list=['front_right_wheel','rear_right_wheel',
            'front_left_wheel','rear_left_wheel']
            
sensor_list=['ir_ext_right','ir_right','ir_ext_left','ir_left',
            'ir_cent_left','ir_cent_right','ir_left_2','ir_right_2',
            'wall_front','wall_right','wall_left',
            'wall_r_front','wall_l_front']

led_list=['led_0r','led_1c','led_2l']

motor=dict()
sensor=dict()
led=dict()

for m in motor_list:
    motor[m] = robot.getDevice(m)
    motor[m].setPosition(float('inf'))
    motor[m].setVelocity(0.0)
    
for s in sensor_list:
    sensor[s] = robot.getDevice(s)
    sensor[s].enable(timestep)
    
for l in led_list:
    led[l] = robot.getDevice(l)

last_error=prop=intg=diff=waitCounter=0
kp=0.025
ki=0.00001
kd=0.08

def pid(b,error):
    global last_error, intg, diff, prop, kp, ki, kd
    prop = error
    intg = error + intg
    diff = error - last_error
    last_error = error
    balance = (kp*prop) + (ki*intg) + (kd*diff)
    rectify = balance
    print(balance)
    rectl=rectify
    rectr=rectify
    max=int("20")
    
    if b+rectify>max:
        print("L>max")
        rectl=max-b
    if b-rectify>max:
        print("R>max")
        rectr=b-max
    if b+rectify<-1*max:
        print("L<max")
        rectl=-b-max
    if b-rectify<-1*max:
        print("R<max")
        rectr=b+max
          
    set_motor_speed(b+rectl,b-rectr)
    return balance
        
def set_motor_speed(left_speed, right_speed):
    print(left_speed,right_speed)
    motor['front_right_wheel'].setVelocity(right_speed)
    motor['rear_right_wheel'].setVelocity(right_speed)
    motor['front_left_wheel'].setVelocity(left_speed)
    motor['rear_left_wheel'].setVelocity(left_speed)

def cross_junct(ir_r_val,ir_l_val):
    while (robot.step(timestep) != -1) and (ir_r_val<950 and ir_l_val<950):
        ir_r_val = sensor['ir_right'].getValue()
        ir_l_val = sensor['ir_left'].getValue()
        print("while")
        set_motor_speed(10,10)

def line_90_l(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2):
    print("line 90 left")
    set_motor_speed(-5,5)
    while (robot.step(timestep) != -1) and (ir_r_2<950 and ir_l_2<950):
        print("while")
        ir_r_val = int(sensor['ir_right'].getValue())
        ir_l_val = int(sensor['ir_left'].getValue())
        ir_r_ext_val = int(sensor['ir_ext_right'].getValue())
        ir_l_ext_val = int(sensor['ir_ext_left'].getValue())
        ir_r_c = int(sensor['ir_cent_right'].getValue())
        ir_l_c = int(sensor['ir_cent_left'].getValue())
        ir_r_2 = int(sensor['ir_right_2'].getValue())
        ir_l_2 = int(sensor['ir_left_2'].getValue())
        
        if ir_r_ext_val<850 and ir_l_ext_val>850:
            set_motor_speed(5,-5)
        elif ir_r_ext_val>850 and ir_l_ext_val<850:
            set_motor_speed(-5,5)
        elif (ir_r_val<350 or ir_l_val<350) and ir_r_ext_val<850:
            set_motor_speed(10,-5)
        elif (ir_r_val<350 or ir_l_val<350) and ir_l_ext_val<850:
            set_motor_speed(-5,10)
        elif ir_r_val<350 and ir_l_2<350 and ir_l_val>950:
            set_motor_speed(-5,5)
        elif ir_r_2<350 and ir_l_val<350 and ir_r_val>950:
            set_motor_speed(-5,5)
        elif ir_r_c<850 and ir_l_c<850 and ir_r_val<850 and ir_l_val<850:
            print("gooo")
            set_motor_speed(3,3)
        elif ir_r_c<950 and ir_l_c<950:
            print("gooo")
            set_motor_speed(20,20)
        else:
            pass

def line_90_r(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2):
    print("line 90 right")
    set_motor_speed(5,-5)
    while (robot.step(timestep) != -1) and (ir_r_2<950 and ir_l_2<950):
        print("while")
        ir_r_val = int(sensor['ir_right'].getValue())
        ir_l_val = int(sensor['ir_left'].getValue())
        ir_r_ext_val = int(sensor['ir_ext_right'].getValue())
        ir_l_ext_val = int(sensor['ir_ext_left'].getValue())
        ir_r_c = int(sensor['ir_cent_right'].getValue())
        ir_l_c = int(sensor['ir_cent_left'].getValue())
        ir_r_2 = int(sensor['ir_right_2'].getValue())
        ir_l_2 = int(sensor['ir_left_2'].getValue())
        
        if ir_r_ext_val<850 and ir_l_ext_val>850:
            set_motor_speed(5,-5)
        elif ir_r_ext_val>850 and ir_l_ext_val<850:
            set_motor_speed(-5,5)
        elif (ir_r_val<350 or ir_l_val<350) and ir_r_ext_val<850:
            set_motor_speed(10,-5)
        elif (ir_r_val<350 or ir_l_val<350) and ir_l_ext_val<850:
            set_motor_speed(-5,10)
        elif ir_r_val<350 and ir_l_2<350 and ir_l_val>950:
            set_motor_speed(5,-5)
        elif ir_r_2<350 and ir_l_val<350 and ir_r_val>950:
            set_motor_speed(5,-5)
        elif ir_r_c<850 and ir_l_c<850 and ir_r_val<850 and ir_l_val<850:
            print("gooo")
            set_motor_speed(3,3)
        elif ir_r_c<950 and ir_l_c<950:
            print("gooo")
            set_motor_speed(20,20)
        else:
            pass       

def line_follow(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2,wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr):
    global j_count,ob_count,ob_l,ob_r
    led_glow(0,0,0)
    
    if wall_r<1000:
        led_glow(0,0,1)
        if ob_r==0:
            ob_count=ob_count+1
            ob_r=1
    else:
        ob_r=0
    
    if wall_l<1000:
        led_glow(1,0,0)
        if ob_l==0:
            ob_count=ob_count+1
            ob_l=1
    else:
        ob_l=0
    
    if wall_l<1000 and wall_r<1000:
        led_glow(1,0,1)
    
    if ir_r_2<950 and ir_l_2<950:
        if ir_r_val<350 and ir_l_val<350 and ir_r_ext_val<850 and ir_l_ext_val<850:
            print("JJJJJJJunction")
            j_count=j_count+1
            led_glow(2,2,2)
            cross_junct(ir_r_ext_val,ir_l_ext_val)
            
        elif ir_r_ext_val<850 and ir_l_ext_val>850:
            line_90_r(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2)
        elif ir_r_ext_val>850 and ir_l_ext_val<850:
            line_90_l(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2)
        
        elif (ir_r_val<350 or ir_l_val<350) and ir_r_ext_val<850:
            set_motor_speed(10,-5)
        elif (ir_r_val<350 or ir_l_val<350) and ir_l_ext_val<850:
            set_motor_speed(-5,10)
        elif ir_r_val<350 and ir_l_2<350 and ir_l_val>950:
            set_motor_speed(-5,5)
        elif ir_r_2<350 and ir_l_val<350 and ir_r_val>950:
            set_motor_speed(-5,5)
        elif ir_r_c<850 and ir_l_c<850 and ir_r_val<850 and ir_l_val<850:
            print("gooo")
            set_motor_speed(3,3)
        elif ir_r_c<950 and ir_l_c<950:
            print("gooo")
            set_motor_speed(20,20)
        else:
            pass
    
    #right senser out of white line    
    elif ir_r_2>950 and ir_l_2<950:
        if ir_r_c<950:
            set_motor_speed(5,15)
        elif ir_r_c>950:
            set_motor_speed(0,10)
        else:
            pass
    
    #left senser out of white line      
    elif ir_r_2<950 and ir_l_2>950:
        if ir_r_c<950 and ir_l_c<950:
            set_motor_speed(15,5)
        elif ir_l_c>950:
            set_motor_speed(10,0)
        else:
            pass
    else:
        print("elseee")

def edge_follow_rw(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2,wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr):
    if ir_r_c<950 and ir_l_c>950:
        set_motor_speed(20,20)
        
    #drifting towards right   
    elif ir_l_c<950:
        if ir_l_2>950:
            set_motor_speed(15,20)
        elif ir_l_2<950:
            set_motor_speed(-3,5)
        else:
            pass
    
    #drift left      
    elif ir_r_c>950:
        if ir_r_2<950:
            set_motor_speed(20,15)
        elif ir_r_2>950:
            set_motor_speed(5,-3)
        else:
            pass
    else:
        print("elseee")
    
def edge_follow_lw(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2,wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr):
    if ir_r_c>950 and ir_l_c<950:
        set_motor_speed(20,20)
    
    #drifting towards right   
    elif ir_l_c>950:
        if ir_l_2<950:
            set_motor_speed(15,20)
        elif ir_l_2>950:
            set_motor_speed(-3,5)
        else:
            pass
    
    #drift left      
    elif ir_r_c<950:
        if ir_r_2>950:
            set_motor_speed(20,15)
        elif ir_r_2<950:
            set_motor_speed(5,-3)
        else:
            pass
    else:
        print("elseee")   

def obst_nav(wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr):
    b=int("10")
    error=int("0")
    
    if wall_f<100:
        print("Fstop")
        set_motor_speed(0,0)
   
    elif (wall_l<1000 or wall_l_fr<1000) and (wall_r<1000 or wall_r_fr<1000):
        print("2_walls")
        if wall_l_fr<1000 and wall_r_fr<1000:
            error=(0.002*abs(1000-wall_f)+1)*(wall_r_fr-wall_l_fr)
        elif wall_l<1000 and wall_r<1000:
            error=(0.002*abs(1000-wall_f)+1)*(wall_r-wall_l)
        else:
            error=0
        pid(b+10,error)  
    
    elif (wall_l<1000 or wall_l_fr<1000)and (wall_r==1000 and wall_r_fr==1000):
        print("L_wall")
        error=abs(1000-wall_f)*0.7 + 450-((wall_l+3*wall_l_fr)/4)
        pid(b+5,error)
            
    elif (wall_r<1000 or wall_r_fr<1000)and(wall_l==1000 and wall_l_fr==1000):
        print("R_wall")
        error=-abs(1000-wall_f)*0.7 + ((wall_r+3*wall_r_fr)/4) - 450
        pid(b+5,error)
    else:
        print("else go")
        set_motor_speed(20,20) 

def led_glow(l,c,r):
    # 1=red, 2=green, 3=blue, 4=yellow, 5=white
    led['led_2l'].set(int(l))
    led['led_1c'].set(int(c))
    led['led_0r'].set(int(r))

def led_num(n):
    if n%2==1:
        led['led_0r'].set(1)
    if n>=2 and(n!=5 and n!=4):
        led['led_1c'].set(1)
    if n>=4:
        led['led_2l'].set(1)
    if n>=8:
        led['led_2l'].set(4)
        led['led_1c'].set(4)
        led['led_0r'].set(4)

phase=mode=mode_1=prev_mode=j_count=ob_count=ob_l=ob_r=int("0")
# Main loop:
while robot.step(timestep) != -1:
    ir_r_val = int(sensor['ir_right'].getValue())
    ir_l_val = int(sensor['ir_left'].getValue())
    ir_r_ext_val = int(sensor['ir_ext_right'].getValue())
    ir_l_ext_val = int(sensor['ir_ext_left'].getValue())
    ir_r_c = int(sensor['ir_cent_right'].getValue())
    ir_l_c = int(sensor['ir_cent_left'].getValue())
    ir_r_2 = int(sensor['ir_right_2'].getValue())
    ir_l_2 = int(sensor['ir_left_2'].getValue())
    wall_f = int(sensor['wall_front'].getValue())
    wall_l = int(sensor['wall_left'].getValue())
    wall_r = int(sensor['wall_right'].getValue())
    wall_l_fr = int(sensor['wall_l_front'].getValue())
    wall_r_fr = int(sensor['wall_r_front'].getValue())
    
    # led_num(int("10"))
    # global phase,mode,prev_mode 
    # if mode_1!=mode:
    prev_mode=mode
    
    if(wall_f==wall_l==wall_r==wall_l_fr==wall_r_fr==1000):
        obst=int("0")
    else:
        obst=int("1")
    
    if prev_mode==0 and ir_l_ext_val<950 and ir_r_ext_val<950:
        mode=int("0")
        set_motor_speed(10,10)
        print("START")
    
    elif prev_mode<=1 and obst==0 and (ir_l_c<950 or ir_r_c<950) and (abs(ir_l_ext_val-ir_r_ext_val)<200 or abs(ir_l_ext_val-ir_r_c)<300 or abs(ir_l_c-ir_r_ext_val)<300):
        print("LLLLLINE FOLLOW")
        mode=int("1")
        line_follow(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2,wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr)    

    elif prev_mode<=2 and obst==0 and (ir_l_ext_val!=ir_r_ext_val):
        mode=int("2")
        print("EDGGGEE FOLLOW")
        if ir_r_val==ir_l_val:
            print("pass")
            pass
        if (ir_l_ext_val<950 and ir_r_ext_val>950):
            edge_follow_lw(ir_r_val,ir_l_val,ir_r_ext_val,ir_l_ext_val,ir_r_c,ir_l_c,ir_r_2,ir_l_2, wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr)    
        
        elif (ir_l_ext_val>950 and ir_r_ext_val<950):
            edge_follow_rw(ir_r_val,ir_l_val,ir_r_ext_val,ir_l_ext_val,ir_r_c,ir_l_c,ir_r_2,ir_l_2, wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr)    
    
    elif prev_mode<=3 and obst==0 and (ir_l_c<950 or ir_r_c<950) and (abs(ir_l_ext_val-ir_r_ext_val)<200 or abs(ir_l_ext_val-ir_r_c)<300 or abs(ir_l_c-ir_r_ext_val)<300):
        print("Junction counttt")
        mode=int("3")
        line_follow(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2,wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr)    

    elif((prev_mode<5 and obst==1)or(prev_mode==4 and obst==0)) and (ir_l_ext_val>950 and ir_r_ext_val>950) and (ir_l_c<950 or ir_r_c<950):
        if prev_mode!=4:
            ob_count=0
        mode=int("4")
        print("COUNT OBSTttt")
        line_follow(ir_r_val,ir_l_val,ir_r_ext_val, ir_l_ext_val, ir_r_c,ir_l_c,ir_r_2,ir_l_2,wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr)    

    elif(prev_mode<6 and prev_mode>=4 and obst==0):
        mode=int("5")
        led_num(j_count+ob_count)
        set_motor_speed(10,10)
        
    elif(obst==1):
        if(prev_mode<=5 and (ir_r_val>750 or ir_l_val>750)):
            mode=int("5")
            led_num(j_count+ob_count)    
        else:
            mode=int("6")
            led_glow(0,0,0)
        print("OBSTACCCCLLE")
        obst_nav(wall_f,wall_l,wall_r,wall_l_fr,wall_r_fr)
    
    elif(prev_mode==6 and obst==0 and ir_l_ext_val>950 and ir_r_ext_val>950):
        mode=int("7")
        print("ENDDDDDDDDDDDDD")
        while ir_l_ext_val>950 and ir_r_ext_val>950 and robot.step(timestep) != -1:
            ir_r_ext_val = int(sensor['ir_ext_right'].getValue())
            ir_l_ext_val = int(sensor['ir_ext_left'].getValue())
            set_motor_speed(20,20)
        print("stop")
        led_glow(5,5,5)
        set_motor_speed(0,0)
        
    else:
        pass
        print("Thank you!")
