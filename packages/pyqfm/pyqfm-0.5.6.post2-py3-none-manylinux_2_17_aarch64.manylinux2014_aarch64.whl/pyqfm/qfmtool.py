import argparse
import sys, signal
import time
import pyqfm


global QF_freescan, QF_secure
QF_freescan = False
QF_secure = False

module = pyqfm.Module()
parser = argparse.ArgumentParser(prog='QFM SDK')


# command
parser.add_argument('command', nargs=1, help="main command, enroll, identify, verify, freescan, qr, param, upgrade, patch, dfu")
parser.add_argument("--read", nargs=1, help="save prameter")
parser.add_argument("--save", nargs=2, help="save prameter")
parser.add_argument("--write",nargs=2, help="write prameter")
parser.add_argument("--path",nargs=1, help="write prameter")

parser.add_argument("--packet", help="packet trace Enable",
                    action="store_true")
parser.add_argument("--secure", help="secure packet Enable",
                    action="store_true")
parser.add_argument("--userfeedback", help="userfeedback data Enable",
                    action="store_true")
# connection values
parser.add_argument("--socket", help="socket",
                    action="store_true")
parser.add_argument("--serial", help="serial",
                    action="store_true")

parser.add_argument("--ip", "-i", help="ip address",
                    default="172.16.110.6", type=str)
parser.add_argument("--port", "-p", help="port",
                    default=12120, type=int)
parser.add_argument("--baud", "-b", help="buadrate",
                    default=115200, type=int)
parser.add_argument("--serialport", "-s", help="serialport",
                    default="/dev/ttyUSB0", type=str)

parser.add_argument("--option", "-O", help="option")
parser.add_argument("--userid", "-U", help="user id")
parser.add_argument("--subid", "-S", help="sub id")

# version
parser.add_argument('--version', action='version',
                    version='%(prog)s v' + module.QF_GetSDKVersionString())


def exitHandler(signum, frame):
    try:
        global QF_freescan, QF_secure
        QF_freescan = False

        if QF_freescan:
            res = input("Ctrl-c was pressed. do you really want to exit? y/n ")
        else:
            res = 'y'

        if res == 'y':
            QF_freeScanDisable()
            module.QF_SetInitSocketTimeout(35)
            ret = module.QF_SetSecurePacketProtocolMode(0, None)
            if not ret:
                print(f"Disable {ret}")
                module.QF_CloseSocket()
                module.QF_CloseCommPort()
            sys.exit("Exit")
        else:
            QF_freescan = True
            pass
    except:
        QF_freeScanDisable()
        module.QF_SetInitSocketTimeout(35)
        ret = module.QF_SetSecurePacketProtocolMode(0, None)
        if not ret:
            module.QF_CloseSocket()
            module.QF_CloseCommPort()
        sys.exit()

def convert_to_decimal(value):
    try:
        # 우선 10진수로 시도
        decimal_value = int(value)
        return decimal_value
    except ValueError:
        # 10진수로 변환이 실패하면 16진수로 시도
        try:
            hex_string = str(value)
            decimal_value = int(hex_string, 16)
            return decimal_value
        except ValueError:
            # 둘 다 실패하면 예외 처리
            raise ValueError("Invalid input value")

def SendPacketCallback(arg):
    if not QF_secure:
            print(f"SEND:{module.QF_GetCtypesString(arg,pyqfm.QF_PACKET_LEN).hex().upper()}")
    else:
        print(f"SEND:{module.QF_GetCtypesString(arg,pyqfm.QF_SECURE_PACKET_LEN).hex().upper()}")


def ReceivePacketCallback(arg):
    if not QF_secure:
            print(f"RECV:{module.QF_GetCtypesString(arg,pyqfm.QF_PACKET_LEN).hex().upper()}")
    else:
        print(f"RECV:{module.QF_GetCtypesString(arg,pyqfm.QF_SECURE_PACKET_LEN).hex().upper()}")


def UserFeedbackDataCallback(feedbackData, userdata):
    if QF_freescan:
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
            print(f"{feedbackData.headPosition.topLeftX,feedbackData.headPosition.topLeftY, feedbackData.headPosition.bottomRightX,feedbackData.headPosition.bottomRightY}")


def QF_freeScanEnable():
    module.QF_SetUserFeedbackDataCallback(UserFeedbackDataCallback)
    ret = module.QF_SetSysParameter(pyqfm.QF_SYS_USER_FEEDBACK, 0x31)
    ret, value = module.QF_GetSysParameter(pyqfm.QF_SYS_USER_FEEDBACK)


def QF_freeScanDisable():
    ret = module.QF_InitSysParameter()
    ret = module.QF_SetSysParameter(pyqfm.QF_SYS_FREESCAN_DELAY, 0x32)
    ret = module.QF_SetSysParameter(pyqfm.QF_SYS_FREE_SCAN, 0x30)
    ret = module.QF_SetSysParameter(pyqfm.QF_SYS_USER_FEEDBACK, 0x30)
    ret, value = module.QF_GetSysParameter(pyqfm.QF_SYS_USER_FEEDBACK)


def QF_printModuleinfo():
    ret, major, miner, revision = module.QF_GetFirmwareVersion()
    ret, patchVersion = module.QF_GetPatchVersion()
    ret, serialNum = module.QF_GetSysParameter(pyqfm.QF_SYS_SERIAL_NUMBER)
    ret, fwVersion = module.QF_GetSysParameter(pyqfm.QF_SYS_FIRMWARE_VERSION)

    fwChar = chr(fwVersion >> 24 & 0xff)
    fwChar = fwChar + chr(fwVersion >> 16 & 0xff)
    fwChar = fwChar + chr(fwVersion >> 8 & 0xff)
    fwChar = fwChar + chr(fwVersion & 0xff)

    ret, buildNum = module.QF_GetSysParameter(pyqfm.QF_SYS_BUILD_NUMBER)
    buildHex = str(hex(buildNum))[2:10]

    print(f"Product is {module.QF_GetModuleString2()}")
    print(f"Firmware Version: {fwChar}, {major}.{miner}.{revision}")
    print(f"Patch Version: {patchVersion}")
    print(f"Serial Number: {serialNum}")
    print(f"Build Number: {buildHex}")
    
def QF_printGetAllParam():
    paramList = ["TIMEOUT", "TEMPLATE_SIZE", "ENROLL_MODE",
                "SECURITY_LEVEL", "ENCRYPTION_MODE", "FIRMWARE_VERSION",
                "SERIAL_NUMBER", "BAUDRATE", "ENROLLED_TEMPLATES",
                "AVAILABLE_TEMPLATES", "SEND_SCAN_SUCCESS", "ASCII_PACKET",
                "ROTATE_IMAGE", "SENSITIVITY", "HORIZONTAL_SENSITIVITY",
                "IMAGE_QUALITY", "AUTO_RESPONSE", "FREE_SCAN",
                "PROVISIONAL_ENROLL", "RESPONSE_DELAY", "MATCHING_TIMEOUT",
                "BUILD_NUMBER", "LIGHTING_CONDITION", "FREESCAN_DELAY",
                "TEMPLATE_TYPE", "FAKE_DETECTION", "PROTOCOL_INTERFACE",
                "KERNEL_VERSION", "PACKET_SECURITY", "MASK_CHECK_LEVEL",
                "USER_FEEDBACK", "VERTICAL_SENSITIVITY", "QFACE_ENGINE_VERSION",
                "PATCH_VERSION", "ENROLLMENT_RESTRICTION", "NUMBER_OF_USER",
                "USER_DETECTION", "SCREEN_ORIENTATION"]

    param_array = [pyqfm.QF_SYS_TIMEOUT, pyqfm.QF_SYS_TEMPLATE_SIZE, pyqfm.QF_SYS_ENROLL_MODE, pyqfm.QF_SYS_SECURITY_LEVEL,
                    pyqfm.QF_SYS_ENCRYPTION_MODE, pyqfm.QF_SYS_FIRMWARE_VERSION, pyqfm.QF_SYS_SERIAL_NUMBER,
                    pyqfm.QF_SYS_BAUDRATE, pyqfm.QF_SYS_ENROLLED_TEMPLATES, pyqfm.QF_SYS_AVAILABLE_TEMPLATES,
                    pyqfm.QF_SYS_SEND_SCAN_SUCCESS, pyqfm.QF_SYS_ASCII_PACKET, pyqfm.QF_SYS_ROTATE_IMAGE,
                    pyqfm.QF_SYS_SENSITIVITY, pyqfm.QF_SYS_HORIZONTAL_SENSITIVITY, pyqfm.QF_SYS_IMAGE_QUALITY,
                    pyqfm.QF_SYS_AUTO_RESPONSE, pyqfm.QF_SYS_FREE_SCAN, pyqfm.QF_SYS_PROVISIONAL_ENROLL,
                    pyqfm.QF_SYS_RESPONSE_DELAY, pyqfm.QF_SYS_MATCHING_TIMEOUT, pyqfm.QF_SYS_BUILD_NUMBER,
                    pyqfm.QF_SYS_LIGHTING_CONDITION, pyqfm.QF_SYS_FREESCAN_DELAY, pyqfm.QF_SYS_TEMPLATE_TYPE,
                    pyqfm.QF_SYS_FAKE_DETECTION, pyqfm.QF_SYS_PROTOCOL_INTERFACE, pyqfm.QF_SYS_KERNEL_VERSION,
                    pyqfm.QF_SYS_PACKET_SECURITY, pyqfm.QF_SYS_MASK_CHECK_LEVEL, pyqfm.QF_SYS_USER_FEEDBACK,
                    pyqfm.QF_SYS_VERTICAL_SENSITIVITY, pyqfm.QF_SYS_QFACE_ENGINE_VERSION, pyqfm.QF_SYS_PATCH_VERSION,
                    pyqfm.QF_SYS_ENROLLMENT_RESTRICTION, pyqfm.QF_SYS_NUMBER_OF_USER, pyqfm.QF_SYS_USER_DETECTION,
                    pyqfm.QF_SYS_SCREEN_ORIENTATION]

    module.QF_InitSysParameter()
    ret, parameters, values = module.QF_GetMultiSysParameter(param_array)

    if ret == 0:
       for idx, (element, paramhex, value) in enumerate(zip(paramList, parameters, values)):
            hex_value = hex(value)[2:].zfill(8)
            _element = f"{element}({hex(paramhex)})"
            print(f"{_element.ljust(30)} : 0x{hex_value}({value})")
    else:
        return 1

def main():
    global QF_freescan, QF_secure
    
    signal.signal(signal.SIGINT, exitHandler)

    args = parser.parse_args()

    print(f"qfmtool v{module.QF_GetSDKVersionString()}")

    if args.socket and not args.serial:
        if args.ip and args.port:
            print(f"Socket {args.ip} {args.port}")
            print("Connecting...")
            module.QF_SetInitSocketTimeout(1)
            if not module.QF_InitSocket(args.ip, args.port) == 0:
                sys.exit("Connetion Error!")
    elif args.serial and not args.socket:
        if args.serialport and args.baud:
            print(f"Serial port {args.serialport} {args.baud}")
            print("Connecting...")
            if not module.QF_InitCommPort(args.serialport, args.baud) == 0:
                sys.exit("Connetion Error!") 
    else:
        sys.exit("Check Connection arguments! if you need help, check the command with -h")

    QF_printModuleinfo()

    if args.secure:
        QF_secure = True
        print("Secure packet mode")
        ret = module.QF_SetSecurePacketProtocolMode(1, None)
        if not ret:
            print(ret)
            if module.QF_SetSecurePacketProtocolMode(0, None):
                if module.QF_SetSecurePacketProtocolMode(1, None):
                    pass
            else:
                sys.exit("Error!")

    if args.packet:
        print("Packet trace mode")
        module.QF_SetSendPacketCallback(SendPacketCallback)
        module.QF_SetReceivePacketCallback(ReceivePacketCallback)

    if args.command[0] == 'param':
        parameter = ""
        if args.read:
            try:
                parameter = getattr(pyqfm, args.read[0])
            except:
                print("Input System parameter Error!")
                return 
            ret, currentValue = module.QF_GetSysParameter(parameter)
            if ret == 0:
                hex_value = hex(currentValue)[2:].zfill(8)
                _element = f"{args.read[0][7:]}({hex(parameter)})"
                print(f"{_element.ljust(30)} : 0x{hex_value}({currentValue})")
        elif args.save and not args.write:
            try:
                parameter = getattr(pyqfm, args.save[0])
            except:
                print("Input System parameter Error!")
                return
            ret = module.QF_SetSysParameter(parameter, convert_to_decimal(args.save[1]))
            if ret == 0:
                module.QF_Save()
                print(f"Saved.")
        elif args.write and not args.save:
            try:
                parameter = getattr(pyqfm, args.write[0])
            except:
                print("Input System parameter Error!")
                return
            ret = module.QF_SetSysParameter(parameter, convert_to_decimal(args.write[1]))
            if ret == 0:
                print(f"Writed.")
        else:
            print("Get All Parameter")
            QF_printGetAllParam()
    elif args.command[0] == "enroll":
        print("Enroll...")
        
        userid = 0
        option = pyqfm.QF_ENROLL_OPTION_ADD_NEW

        if args.userid:
            userid = int(args.userid)
        if args.option:
            option = getattr(pyqfm, args.option)

        ret, enrollID, imageQuality = module.QF_Enroll(userid, option)
        if ret == 0:
            print(f"ID: {enrollID} imageQuality: {imageQuality}")
        else:
            print(f"Error: {ret}")
    elif args.command[0] == "identify":
        print("Identify...")

        ret, userID, subID = module.QF_Identify()
        if ret == 0:
            print(f"ID: {userID} subID: {subID}")
        else:
            print(f"Error: {ret}")
    elif args.command[0] == "verify":
        print("Verify...")

        if not args.userid:
            print("Required userID.")
            return
        
        ret, subID = module.QF_Verify(int(args.userid))
        if ret == 0:
            print(f"ID: {args.userid} subID: {subID}")
        else:
            print(f"Error: {ret}")
    elif args.command[0] == "freescan":
        print("Freescan Mode")
        ret = module.QF_InitSysParameter()
        ret = module.QF_SetSysParameter(pyqfm.QF_SYS_FREESCAN_DELAY, 0x30)
        ret = module.QF_SetSysParameter(pyqfm.QF_SYS_FREE_SCAN, 0x31)
        if args.userfeedback:
            QF_freeScanEnable()
            print("userfeedbackdata ON")
        QF_freescan = True
        while QF_freescan:
            try:
                ret, packet = module.QF_ReceivePacket(1000) # BYTE *packet, int timeout
                
                if module.QF_GetPacketValue(pyqfm.QF_PACKET_COMMAND, packet) == pyqfm.QF_COM_IS and \
                module.QF_GetPacketValue(pyqfm.QF_PACKET_FLAG, packet) == pyqfm.QF_PROTO_RET_SUCCESS:
                    userID = module.QF_GetPacketValue(pyqfm.QF_PACKET_PARAM, packet)
                    subID = module.QF_GetPacketValue(pyqfm.QF_PACKET_SIZE, packet)
                    
                    print(f"User ID : {userID}, Sub ID : {subID}")
                elif module.QF_GetPacketValue(pyqfm.QF_PACKET_COMMAND, packet) == pyqfm.QF_COM_IS and \
                module.QF_GetPacketValue(pyqfm.QF_PACKET_FLAG, packet) == pyqfm.QF_PROTO_RET_TIMEOUT_MATCH:
                    print("matching timeout")
                    
                    time.sleep(2)
            except:
                QF_freescan = False
                sys.exit("Exit!")
    elif args.command[0] == "qr":
        print("QR Scan...")
        ret, string, length = module.QF_ReadQRCode()
        if ret == 0:
            print(f"Result length: {length}")
            print(string.decode('UTF-8')) 
        else:
            print(f"[Read QR Code] Error: {ret}")   
    elif args.command[0] == "delete":
        if args.userid and args.subid:
            ret = module.QF_DeleteOneTemplate(int(args.userid), int(args.subid))
            if  ret == 0:
                print(f"Deleted.")
            else:    
                print(f"Error: {ret}")
        else:
            res = input("not set userid or subid, do you really want delete all template? y/n ")
            if res == 'y':
                ret = module.QF_DeleteAll()
                if  ret == 0:
                    print(f"Deleted.")
                else:    
                    print(f"Error: {ret}")
            else:
                print("Cancel.")

    elif args.command[0] == "upgrade":
        print("Upgrade...")
        ret = module.QF_Upgrade(args.path[0], 4096 * 4)
        if ret == 0:
            print(f"Done.")
        else:
            print(f"Upgrade Error: {ret}")

    elif args.command[0] == "patch":
        print("Patch...")
        ret = module.QF_UpdatePatch(args.path[0], 4096 * 4)
        if ret == 0:
            print(f"Done.")
        else:
            print(f"Patch Error: {ret}")

    elif args.command[0] == "dfu":
        print("Enter DFU Mode...")
        ret = module.QF_EnterDFUMode()
        if ret == 0:
            print(f"Done.")
        else:
            print(f"Error: {ret}")
    else:
        print(f"Command is Wrong")
        return

if __name__ == "__main__":
    main()