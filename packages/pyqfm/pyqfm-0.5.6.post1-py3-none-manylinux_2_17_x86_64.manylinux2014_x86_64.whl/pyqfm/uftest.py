import threading
import time
import pyqfm
module = pyqfm.Module()


def UserFeedbackDataCallback(feedbackData, userdata):
    #print(f"Callback : s_SetUserFeedbackDataCallback / arg:{feedbackData}")
    print(feedbackData.fields)
    if feedbackData.fields & pyqfm.USER_FEEDBACK_TYPE_MESSAGE_CODE:
        feedback = feedbackData.messageCode
        if feedback == pyqfm.QF_USER_FEEDBACK_LOOK_AT_THE_CAMERA_CORRECTLY:
            print("Look at the camera correctly")
        elif feedback == pyqfm.QF_USER_FEEDBACK_TURN_YOUR_HEAD_RIGHT:
            # turn your head right
            print("Turn your head right")
        elif feedback == pyqfm.QF_USER_FEEDBACK_TURN_YOUR_HEAD_LEFT:
            # turn your head left
            print("Turn your head left")
        elif feedback == pyqfm.QF_USER_FEEDBACK_TURN_YOUR_HEAD_UP:
            # turn your head up
            print("Turn your head up")
        elif feedback == pyqfm.QF_USER_FEEDBACK_TURN_YOUR_HEAD_DOWN:
            # turn your head down
            print("Turn your head down")
        elif feedback == pyqfm.QF_USER_FEEDBACK_MOVE_FORWARD:
            # move forward
            print("Move forward")
        elif feedback == pyqfm.QF_USER_FEEDBACK_MOVE_BACKWARD:
            # move backward
            print("Move backward")
        elif feedback == pyqfm.QF_USER_FEEDBACK_OUT_OF_ENROLLMENT_AREA:
            # out of enrollment area
            print("Out of enrollment area")
        elif feedback == pyqfm.QF_USER_FEEDBACK_FACE_NOT_DETECTED:
            print("Face not detected")
    elif feedbackData.fields & pyqfm.USER_FEEDBACK_TYPE_HEAD_POSITION:
        print(feedbackData.headPosition.topLeftX,
              feedbackData.headPosition.topLeftY,
              feedbackData.headPosition.bottomRightX,
              feedbackData.headPosition.bottomRightY)
    
class EventLoop:
    def __init__(self):
        self.is_running = True
        self.lock = threading.Lock()

    def process_events(self):

        while self.is_running:
            
            res, packet = module.QF_ReceivePacket(1000) # BYTE *packet, int timeout

            if module.QF_GetPacketValue(pyqfm.QF_PACKET_COMMAND, packet) == pyqfm.QF_COM_IS and \
            module.QF_GetPacketValue(pyqfm.QF_PACKET_FLAG, packet) == pyqfm.QF_PROTO_RET_SUCCESS:
                
                userID = module.QF_GetPacketValue(pyqfm.QF_PACKET_PARAM, packet)

                subID = module.QF_GetPacketValue(pyqfm.QF_PACKET_SIZE, packet)

                print(f"User ID : {userID}, Sub ID : {subID}")

            elif module.QF_GetPacketValue(pyqfm.QF_PACKET_COMMAND, packet) == pyqfm.QF_COM_IS and \
            module.QF_GetPacketValue(pyqfm.QF_PACKET_FLAG, packet) == pyqfm.QF_PROTO_RET_TIMEOUT_MATCH:
                
                print("matching timeout")

                time.sleep(2)

            time.sleep(0.1)

    def stop(self):
        # Stop the event loop
        with self.lock:
            self.is_running = False

def setup():
    # Init socket and clean
    res = module.QF_InitSocket()
    if res == 0: 
        print(f"Func : QF_InitSocket() / result:{res}")
    else:
        print(f"Fail : QF_InitSocket() check connect or network setup / result:{res}")
        return 1

    res = module.QF_ResetSystemParameter()
    print(f"Func : QF_ResetSystemParameter() / result:{res}")
    
    module.QF_SetUserFeedbackDataCallback(UserFeedbackDataCallback)
    
    res = module.QF_InitSysParameter()
    print(f"Func : QF_InitSysParameter() / result:{res}")
    
    res = module.QF_SetSysParameter(pyqfm.QF_SYS_FREESCAN_DELAY, 0x30)
    print(f"Func : QF_SYS_FREESCAN_DELAY() / result:{res}")

    res = module.QF_SetSysParameter(pyqfm.QF_SYS_FREE_SCAN, 0x31)
    print(f"Func : QF_SYS_FREE_SCAN() / result:{res}")

    res = module.QF_SetSysParameter(pyqfm.QF_SYS_USER_FEEDBACK, 0x31)
    print(f"Func : QF_SYS_USER_FEEDBACK() / result:{res}")

    res, value = module.QF_GetSysParameter(pyqfm.QF_SYS_USER_FEEDBACK)
    print(f"Func : QF_SYS_USER_FEEDBACK() / result:{res, value}")

    print("Ready!! Face Enroll by scan")
    # Scan template data
    res, enrollID, imageQuality = module.QF_Enroll(0, pyqfm.QF_ENROLL_OPTION_CHECK_FACE_AUTO_ID)
    if res == 0: 
        print(f"Func : QF_Enroll() / result:{res, enrollID, imageQuality}")
    else:
        print(f"Fail : QF_Enroll() / result:{res, enrollID, imageQuality}")
        print("Fail Enroll by scan!!")
        return 1

    return 0

# Example usage:
if __name__ == "__main__":
    
    event_loop = EventLoop()
    setup()
    # Start the event processing thread
    event_thread = threading.Thread(target=event_loop.process_events)
    event_thread.start()
    event_thread.join()