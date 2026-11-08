from machine import Pin, PWM
import time

# --- KHAI BÁO CHÂN TỐI ƯU CHO ESP32 DEVKIT V1 ---
# Chân điều khiển động cơ (Các chân Output an toàn)
in1 = Pin(27, Pin.OUT)
in2 = Pin(26, Pin.OUT)
in3 = Pin(25, Pin.OUT)
in4 = Pin(33, Pin.OUT)

enA = PWM(Pin(14), freq=1000)
enB = PWM(Pin(13), freq=1000)


# Tốc độ động cơ (0 - 1023)
speedPWM = 350
enA.duty(speedPWM)
enB.duty(speedPWM)

# Cảm biến hồng ngoại (Dùng cụm chân Input-only cực kỳ an toàn)
L_S = Pin(36, Pin.IN)  # Chân có chữ VP trên mạch
L_SS = Pin(39, Pin.IN) # Chân có chữ VN trên mạch
S_S = Pin(34, Pin.IN)
R_S = Pin(35, Pin.IN)
R_SS = Pin(32, Pin.IN)

def idle():
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    print("idle")

def turnDown():
    in1.value(1)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    print("DOWN")

def turnUp():
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(1)
    print("UP")

def turnRight():
    in1.value(0)
    in2.value(1)
    in3.value(1)
    in4.value(0)
    print("RIGHT")

def turnLeft():
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    print("LEFT")

idle()

# --- VÒNG LẶP CHÍNH ---
while True:
    ls_val = L_S.value()
    lss_val = L_SS.value()
    ss_val = S_S.value()
    rs_val = R_S.value()
    rss_val = R_SS.value()

    if ls_val == 0 and rs_val == 0 and ss_val == 0 and lss_val == 0 and rss_val == 0:
        turnDown()
    elif ss_val == 1:
        turnUp()
    elif ls_val == 1 or lss_val == 1 or (ls_val == 1 and lss_val == 1 and ss_val == 1) or (ls_val == 1 and lss_val == 1) or (ls_val == 1 and ss_val == 1):
        turnLeft()
    elif rs_val == 1 or rss_val == 1 or (rs_val == 1 and rss_val == 1 and ss_val == 1) or (rs_val == 1 and rss_val == 1) or (rss_val == 1 and ss_val == 1):
        turnRight()
    else:
        idle()
        
    time.sleep(0.01)

