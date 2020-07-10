import rpi_dc_lib as hw
import time
import cv2
import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    model = tf.keras.keras.models.load_model('.h5')

    start_flag = False

    c = cv2.VideoCapture(0)
    c.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    c.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    while(True):
    
        _,full_image = c.read()
        full_image = cv2.resize(full_image, (150,150))

        cv2.imshow("view of AI", cv2.cvtColor(full_image, cv2.COLOR_RGB2BGR))

        np_image_data = np.asarray(full_image)/255
        np_image_data = np_image_data.reshape((1, 150, 150, 3))

        wheel = model.predict(np_image_data)
        wheel_cls = np.argmax(wheel, axis=1)
        
        print('wheel value:', wheel_cls)
    
        k = cv2.waitKey(5)
        if k == ord('q'):  #'q' key to stop program
            break

        """ Toggle Start/Stop motor movement """
        if k == ord('a'): 
            if start_flag == False: 
                start_flag = True
            else:
                start_flag = False
            print('start flag:',start_flag)
        
        if start_flag:
        
            if wheel_cls == 0:
                hw.motor_two_speed(0)
                hw.motor_one_speed(0)
            if wheel_cls == 1: # Foward
                hw.motor_two_speed(60)
                hw.motor_one_speed(60)
            
            if wheel_cls == 2: # Left Turn
                hw.motor_one_speed(90)
                hw.motor_two_speed(0)

            if wheel_cls == 3: # Right turn
                hw.motor_one_speed(0)
                hw.motor_two_speed(90)
            
            if wheel_cls == 4: # Slow
                hw.motor_two_speed(0)
                hw.motor_one_speed(0)
        else:
            hw.motor_one_speed(0)
            hw.motor_two_speed(0)
            wheel_cls = 0

        
hw.motor_clean()
cv2.destroyAllWindows()

