import time
from directkeys import right_pressed,left_pressed
from directkeys import PressKey, ReleaseKey                 



break_key_pressed=left_pressed
accelerato_key_pressed=right_pressed

time.sleep(2.0)
current_key_pressed = set()



keyPressed = False
break_pressed=False
accelerator_pressed=False
key_count=0
key_pressed=0
                
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                PressKey(break_key_pressed)
                break_pressed=True
                current_key_pressed.add(break_key_pressed)
                key_pressed=break_key_pressed
                keyPressed = True
                key_count=key_count+1



                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "  GAS", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                PressKey(accelerato_key_pressed)
                key_pressed=accelerato_key_pressed
                accelerator_pressed=True
                keyPressed = True
                current_key_pressed.add(accelerato_key_pressed)
                key_count=key_count+1




        if not keyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()
        elif key_count==1 and len(current_key_pressed)==2:    
            for key in current_key_pressed:             
                if key_pressed!=key:
                    ReleaseKey(key)
            current_key_pressed = set()
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()

