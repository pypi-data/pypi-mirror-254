#import pylibQFM_SDK
from .pylibQFM_SDK import *
import ctypes

class Module:
    def __init__(self):
        pass

    def QF_GetCtypesString(self, arg, len):
        return ctypes.string_at(arg, len)

    # SDK version
    def QF_GetSDKVersion(self):
        major = ctypes.c_int()
        miner = ctypes.c_int()
        revision = ctypes.c_int()
        QF_GetSDKVersion(major, miner, revision)

        return major.value, miner.value, revision.value

    def QF_GetSDKVersionString(self):
        versionString = QF_GetSDKVersionString()
        return versionString.decode('utf-8')

    # Serial communication API and Socket API
    def QF_InitCommPort(self, commPort="/dev/ttyUSB0", baudrate="115200", asciiMode=0): # const char *commPort, int baudrate, BOOL asciiMode
        return QF_InitCommPort(str(commPort), int(baudrate), asciiMode)
        
    def QF_CloseCommPort(self):
        return QF_CloseCommPort()

    def QF_Reconnect(self):
        return QF_Reconnect()

    def QF_SetBaudrate(self, baudrate): # int baudrate
        return QF_SetBaudrate(int(baudrate))
    
    def QF_SetAsciiMode(self, asciiMode): # BOOL asciiMode
        return QF_SetAsciiMode(asciiMode)

    def QF_InitSocket(self, inetAddr="172.16.110.6", port="12120", asciiMode=0): # const char *inetAddr, int port, BOOL asciiMode
        return QF_InitSocket(str(inetAddr), int(port), asciiMode)

    def QF_CloseSocket(self):
        return QF_CloseSocket()

    def QF_SetInitSocketTimeout(self, timeout): # int timeout
        return QF_SetInitSocketTimeout(timeout)


    # Callback functions for the user-defined UART handler (for Android)

    # Set baudrate to the host handler of the user-defined UART handler
    def QF_SetSetupSerialCallback(self, callback): # void (*Callback)(int)
        SetupFunc = ctypes.CFUNCTYPE(None, ctypes.c_int)
        self.setupFunc = SetupFunc(callback)
        QF_SetSetupSerialCallback(self.setupFunc)

    # Read serial data by the host handler of the user-defined UART handler
    def QF_SetReadSerialCallback(self, callback): # int (*Callback)(BYTE *, int, int)
        ReadFunc = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int, ctypes.c_int)
        self.readFunc = ReadFunc(callback)
        QF_SetReadSerialCallback(self.readFunc)

    # Write serial data by the host handler of the user-defined UART handler
    def QF_SetWriteSerialCallback(self, callback): # int (*Callback)(BYTE *, int, int)
        WriteFunc = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int, ctypes.c_int)
        self.writeFunc = WriteFunc(callback)    
        QF_SetWriteSerialCallback(self.writeFunc)

    # Basic packet interface (Low-ef Level Packet API)
    def QF_SendPacket(self, command, param, size, flag, timeout): # BYTE command, UINT32 param, UINT32 size, BYTE flag, int timeout
        command = ctypes.c_ubyte(command)
        param = ctypes.c_uint32(param)
        size = ctypes.c_uint32(size)
        flag = ctypes.c_ubyte(flag)
        timeout = int(timeout)

        return QF_SendPacket(command, param, size, flag, timeout)

    def QF_ReceivePacket(self, timeout): # BYTE *packet, int timeout
        packet = (ctypes.c_ubyte * QF_PACKET_LEN)()
        timeout = int(timeout)

        return QF_ReceivePacket(packet, timeout), ctypes.string_at(packet,QF_PACKET_LEN)

    def QF_SendRawData(self, buf, size, timeout): # BYTE *buf, UINT32 size, int timeout
        buf =  (ctypes.c_ubyte * size)(*buf)
        size = ctypes.c_uint32(size)
        timeout = int(timeout)

        return QF_SendRawData(buf, size, timeout)
        
    def QF_ReceiveRawData(self, size, timeout, checkEndCode): # BYTE *buf, UINT32 size, int timeout, BOOL checkEndCode
        buf =  (ctypes.c_ubyte * size)()
        size = ctypes.c_uint32(size)
        timeout = int(timeout)
        checkEndCode = ctypes.c_bool(checkEndCode)

        return QF_ReceiveRawData(buf, size, timeout, checkEndCode), ctypes.string_at(buf,size.value)

    def QF_SendDataPacket(self, command, buf, dataSize, dataPacketSize): # BYTE command, BYTE *buf, UINT32 dataSize, UINT32 dataPacketSize
        command = ctypes.c_ubyte(command)
        buf = (ctypes.c_ubyte * dataSize)(*buf)
        dataSize = ctypes.c_uint32(dataSize)
        dataPacketSize = ctypes.c_uint32(dataPacketSize)

        return QF_SendDataPacket(command, buf, dataSize, dataPacketSize)

    def QF_ReceiveDataPacket(self, command, dataSize): # BYTE command, BYTE *buf, UINT32 dataSize
        command = ctypes.c_ubyte(command)
        buf = (ctypes.c_ubyte * dataSize)(*buf)
        dataSize = ctypes.c_uint32(dataSize)

        return QF_SendDataPacket(command, buf, dataSize), buf

    def QF_SetSendPacketCallback(self, callback): # void (*Callback)(BYTE *)
        SendPacketFunc = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_ubyte))
        self.sendPacketFunc = SendPacketFunc(callback)
        QF_SetSendPacketCallback(self.sendPacketFunc)

    def QF_SetReceivePacketCallback(self, callback): # void (*Callback)(BYTE *)
        ReceivePacketFunc = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_ubyte))
        self.receivePacketFunc = ReceivePacketFunc(callback)    
        QF_SetReceivePacketCallback(self.receivePacketFunc)

    def QF_SetSendDataPacketCallback(self, callback): # void (*Callback)(int index, int numOfPacket)
        SendDataPacketFunc = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
        self.sendDataPacketFunc = SendDataPacketFunc(callback)    
        QF_SetSendDataPacketCallback(self.sendDataPacketFunc)

    def QF_SetReceiveDataPacketCallback(self, callback): # void (*Callback)(int index, int numOfPacket)
        ReceiveDataPacketFunc = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
        self.receiveDataPacketFunc = ReceiveDataPacketFunc(callback)    
        QF_SetReceiveDataPacketCallback(self.receiveDataPacketFunc)

    def QF_SetSendRawDataCallback(self, callback): # void (*Callback)(int writtenLen, int totalSize)
        SendRawDataPacketFunc = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
        self.sendRawDataPacketFunc = SendRawDataPacketFunc(callback)    
        QF_SetSendRawDataCallback(self.sendRawDataPacketFunc)

    def QF_SetReceiveRawDataCallback(self, callback): # void (*Callback)(int readLen, int totalSize)
        ReceiveRawDataPacketFunc = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
        self.receiveRawDataPacketFunc = ReceiveRawDataPacketFunc(callback)    
        QF_SetReceiveRawDataCallback(self.receiveRawDataPacketFunc)

    def QF_SetDefaultPacketSize(self, defaultSize): #int defaultSize
        return QF_SetDefaultPacketSize(int(defaultSize))
    
    def QF_GetDefaultPacketSize(self):
        return QF_GetDefaultPacketSize()


    # Generic command interface API
    def QF_Command(self, command, param, size, flag): # BYTE command, UINT32 *param, UINT32 *size, BYTE *flag
        command = ctypes.c_ubyte(command)
        param = ctypes.c_uint32(param)
        size = ctypes.c_uint32(size)
        flag = ctypes.c_ubyte(flag)
        
        return QF_Command(command, param, size, flag)

    def QF_CommandEx(self, command, param, size, flag, msgCallback): # BYTE command, UINT32 *param, UINT32 *size, BYTE *flag, BOOL (*msgCallback)(BYTE)
        command = ctypes.c_ubyte(command)
        param = ctypes.c_uint32(param)
        size = ctypes.c_uint32(size)
        flag = ctypes.c_ubyte(flag)

        CommandExFunc = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_ubyte)
        self.commandExFunc = CommandExFunc(msgCallback)

        return QF_CommandEx(command, param, size, flag, self.commandExFunc)
        
    def QF_CommandSendData(self, command, param, size, data, dataSize): # BYTE command, UINT32 *param, UINT32 *size, BYTE *flag, BYTE *data, UINT32 dataSize
        command = ctypes.c_ubyte(command)
        param = ctypes.c_uint32(param)
        size = ctypes.c_uint32(size)
        flag = ctypes.c_ubyte()
        data = (ctypes.c_ubyte * dataSize)(*data)
        dataSize = ctypes.c_uint32(dataSize)
    
        return QF_CommandSendData(command, param, size, flag, data, dataSize), param, size, flag

    def QF_CommandSendDataEx(self, command, param, size, data, dataSize, msgCallback, waitUserInput): # BYTE command, UINT32 *param, UINT32 *size, BYTE *flag, BYTE *data, UINT32 dataSize, BOOL (*msgCallback)(BYTE), BOOL waitUserInput
        command = ctypes.c_ubyte(command)
        param = ctypes.c_uint32(param)
        size = ctypes.c_uint32(size)
        flag = ctypes.c_ubyte()
        data = (ctypes.c_ubyte * dataSize)(*data)
        dataSize = ctypes.c_uint32(dataSize)
        waitUserInput = ctypes.c_bool(waitUserInput)

        CommandSendDataExFunc = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_ubyte)
        self.commandSendDataExFunc = CommandSendDataExFunc(msgCallback)

        return QF_CommandSendDataEx(command, param, size, flag, data, dataSize, self.commandSendDataExFunc, waitUserInput), param, size, flag
    
    def QF_Cancel(self, receivePacket): # BOOL receivePacket
        receivePacket = ctypes.c_bool(receivePacket)

        return QF_Cancel(receivePacket)

    def QF_SetGenericCommandTimeout(self, timeout): # int timeout
        timeout = int(timeout)

        return QF_SetGenericCommandTimeout(timeout)
    
    def QF_SetInputCommandTimeout(self, timeout): # int timeout
        timeout = int(timeout)

        return QF_SetInputCommandTimeout(timeout)

    def QF_GetGenericCommandTimeout(self):
        return QF_GetGenericCommandTimeout()

    def QF_GetInputCommandTimeout(self):
        return QF_GetInputCommandTimeout()

    def QF_GetErrorCode(self, retCode): # QF_PROTOCOL_RET_CODE retCode
        #retCode = getattr(pylibQFM_SDK, retCode)

        return QF_GetErrorCode(retCode)

    # Module API
    def QF_GetModuleInfo(self): # QF_MODULE_TYPE *type, QF_MODULE_VERSION *version, QF_HARDWARE_REVISION *hardware_revision
        type = ctypes.c_int()
        version = ctypes.c_int()
        hardware_revision = ctypes.c_int()

        return QF_GetModuleInfo(type, version, hardware_revision), type.value, version.value, hardware_revision.value
    
    def QF_GetModuleString(self, type, version, hardware_revision): # QF_MODULE_TYPE type, QF_MODULE_VERSION version, QF_HARDWARE_REVISION hardware_revision
        type = ctypes.c_int(type)
        version = ctypes.c_int(version)
        hardware_revision = ctypes.c_int(hardware_revision)
        moduleString = QF_GetModuleString(type, version, hardware_revision)

        return moduleString.decode('utf-8')
    
    def QF_GetModuleString2(self):
        moduleString = QF_GetModuleString2()
        return moduleString.decode('utf-8')

    def QF_SearchModule(self, port, baudrate, asciiMode, protocol, moduleID, callback): # const char *port, int *baudrate, BOOL *asciiMode, QF_PROTOCOL *protocol, UINT32 *moduleID, void (*callback)(const char *comPort, int baudrate)
        return QF_SearchModule(port, baudrate, asciiMode, protocol, moduleID, callback)

    def QF_SearchModuleBySocket(self, inetAddr, tcpPort, asciiMode, protocol, moduleID, callback): # const char *inetAddr, int tcpPort, BOOL *asciiMode, QF_PROTOCOL *protocol, UINT32 *moduleID
        return QF_SearchModuleBySocket(inetAddr, tcpPort, asciiMode, protocol, moduleID, callback)

    def QF_Upgrade(self, firmwareFilename, dataPacketSize): # const char *firmwareFilename, int dataPacketSize
        return QF_Upgrade(firmwareFilename, int(dataPacketSize))

    def QF_UpdatePatch(self, filename, dataPacketSize): # const char *filename, int dataPacketSize
        return QF_UpdatePatch(filename, int(dataPacketSize))

    def QF_Reset(self):
        return QF_Reset()
    
    def QF_GetFirmwareVersion (self): # int *major, int *minor, int *revision
        major = ctypes.c_int()
        minor = ctypes.c_int()
        revision = ctypes.c_int()

        return QF_GetFirmwareVersion(major, minor, revision), major.value, minor.value, revision.value

    def QF_GetPatchVersion (self): # int *patchVersion
        patchVersion = ctypes.c_int()

        return QF_GetPatchVersion(patchVersion), patchVersion.value
    
    def QF_EnterDFUMode(self):
        return QF_EnterDFUMode()

    # System parameter API
    def QF_InitSysParameter(self):
        return QF_InitSysParameter()

    def QF_GetSysParameter(self, parameter): # QF_SYS_PARAM parameter, UINT32 *value
        #parameter = getattr(pylibQFM_SDK, parameter)
        value = ctypes.c_uint32()

        return QF_GetSysParameter(parameter, value), value.value
    
    def QF_SetSysParameter(self, parameter, value): # QF_SYS_PARAM parameter, UINT32 value
        #parameter = getattr(pylibQFM_SDK, parameter)
        value = ctypes.c_uint32(value)

        return QF_SetSysParameter(parameter, value)
    
    def QF_GetMultiSysParameter(self, parameters): # int parameterCount, QF_SYS_PARAM *parameters, UINT32 *values
        paramBuffer = []
        #for item in parameters:
            #sysParam = getattr(pylibQFM_SDK, item)
            #paramBuffer.append(item)
        parameters = (QF_SYS_PARAM * len(parameters))(*parameters)
        values = (ctypes.c_uint32 * len(parameters))()

        return QF_GetMultiSysParameter(len(parameters), parameters, values), list(parameters), list(values)
    
    def QF_SetMultiSysParameter(self, parameters, values): # int parameterCount, QF_SYS_PARAM *parameters, UINT32 *values
        paramBuffer = []
        #for item in parameters:
            #sysParam = getattr(pylibQFM_SDK, item)
            #paramBuffer.append(item)
        parameters = (QF_SYS_PARAM * len(parameters))(*parameters)
        valueBuffer = (ctypes.c_uint32 * len(values))()
        for i, value in enumerate(values):
            valueBuffer[i] = value

        return QF_SetMultiSysParameter(len(parameters), parameters, valueBuffer)

    def QF_Save(self):
        return QF_Save()

    def QF_ResetSysParameters(self):
        return QF_ResetSysParameters()

    # Template management API
    def QF_GetNumOfTemplate(self): # UINT32 *numOfTemplate
        numOfTemplate = ctypes.c_uint32()

        return QF_GetNumOfTemplate(numOfTemplate), numOfTemplate.value
    
    def QF_GetMaxNumOfTemplate(self): # UINT32 *maxNumOfTemplate
        maxNumOfTemplate = ctypes.c_uint32()

        return QF_GetMaxNumOfTemplate(maxNumOfTemplate), maxNumOfTemplate.value
    
    def QF_GetAllUserInfo(self): # QFUserInfo *userInfo, UINT32 *numOfUser, UINT32 *numOfTemplate
        # Excessive Memory Allocation Prevention through Preliminary Query of numOfUser
        res, usernum = self.QF_GetNumOfUser()

        numOfUser = ctypes.c_uint32()
        numOfTemplate = ctypes.c_uint32()
        userInfo = (QFUserInfo * (usernum))()
        res = QF_GetAllUserInfo(userInfo, numOfUser, numOfTemplate)

        if not res == 0: 
            userInfo = None

        return res, userInfo, numOfUser.value, numOfTemplate.value

    def QF_GetAllUserInfoEx(self): # QFUserInfoEx *userInfo, UINT32 *numOfUser, UINT32 *numOfTemplate
        userInfo = QFUserInfoEx()
        numOfUser = ctypes.c_uint32()
        numOfTemplate = ctypes.c_uint32()

        return QF_GetAllUserInfoEx(userInfo, numOfUser, numOfTemplate), userInfo, numOfUser.value, numOfTemplate.value
    
    def QF_SortUserInfo(self, userInfo, numOfUser): # QFUserInfo *userInfo, int numOfUser
        QF_SortUserInfo(userInfo, int(numOfUser))

    def QF_SetUserInfoCallback(self, callback): # void (*callback)(int index, int numOfTemplate)
        SetUserInfoCallbackFunc = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
        self.setUserInfoCallbackFunc = SetUserInfoCallbackFunc(callback)    
        QF_SetUserInfoCallback(self.setUserInfoCallbackFunc)
    
    def QF_CheckTemplate(self, userID): # UINT32 userID, UINT32 *numOfTemplate
        userID = ctypes.c_uint32(userID)
        numOfTemplate = ctypes.c_uint32()

        return QF_CheckTemplate(userID, numOfTemplate), numOfTemplate.value

    def QF_CheckTemplate2(self, templateData): # BYTE* templateData, UINT32 *userID
        templateBuffer = (ctypes.c_ubyte * (MAXIMUM_TEMPLATE_SIZE))
        templateData = templateBuffer(*templateData)
        userID = ctypes.c_uint32()

        return QF_CheckTemplate2(templateData, userID), userID.value
    
    def QF_ReadTemplate(self, userID): # UINT32 userID, UINT32 *numOfTemplate, BYTE *templateData
        res, num = self.QF_CheckTemplate(userID)
        numTemp = num 

        userID = ctypes.c_uint32(userID)
        numOfTemplate = ctypes.c_uint32()
        templateData = (ctypes.c_ubyte * (MAXIMUM_TEMPLATE_SIZE * numTemp))()
        res = QF_ReadTemplate(userID, numOfTemplate, templateData)

        if not res == 0: 
            #templateData = bytes(templateBuffer[:MAXIMUM_TEMPLATE_SIZE * numOfTemplate.value])
        #else:
            templateData = None
        
        return res, numOfTemplate.value, templateData
    
    def QF_ReadOneTemplate(self, userID, subID): # UINT32 userID, int subID, BYTE *templateData
        userID = ctypes.c_uint32(userID)
        templateBuffer = (ctypes.c_ubyte * MAXIMUM_TEMPLATE_SIZE)()
        res = QF_ReadOneTemplate(userID, int(subID), templateBuffer)

        if res == 0: 
            templateData = bytes(templateBuffer)
        else:
            templateData = None
    
        return res, templateData
    
    def QF_SetScanCallback(self, Callback): # void (*Callback)(BYTE)
        SetScanCallbackFunc = ctypes.CFUNCTYPE(None, ctypes.c_ubyte)
        self.setScanCallbackFunc = SetScanCallbackFunc(Callback)    
        QF_SetScanCallback(self.setScanCallbackFunc)
    
    def QF_ScanTemplate(self): # BYTE *templateData, UINT32 *templateSize, UINT32 *imageQuality
        templateBuffer = (ctypes.c_ubyte * MAXIMUM_TEMPLATE_SIZE)()
        templateSize = ctypes.c_uint32()
        imageQuality = ctypes.c_uint32()
        res = QF_ScanTemplate(templateBuffer, templateSize, imageQuality)

        if res == 0: 
            templateData = bytes(templateBuffer)
        else:
            templateData = None

        return res, templateData, templateSize.value, imageQuality.value
    
    def QF_SaveDB(self, fileName): # const char *fileName
        return QF_SaveDB(fileName)
    
    def QF_LoadDB(self, fileName): # const char *fileName
        return QF_LoadDB(fileName)
    
    def QF_ResetDB(self):
        return QF_ResetDB()
    
    def QF_GetNumOfUser(self): # UINT32 *numOfUser
        numOfUser = ctypes.c_uint32()

        return QF_GetNumOfUser(numOfUser), numOfUser.value

    # Image Manipulation API
    def QF_ReadImage(self): # QFImage *image
        image = QFImage()
        res = QF_ReadImage(image)

        if res == 0: 
            pass
        else:
            image = None

        return res, image
    
    def QF_ScanImage(self): # QFImage *image
        image = QFImage()
        res = QF_ScanImage(image)

        if res == 0: 
            pass
        else:
            image = None

        return res, image
    
    def QF_SaveImage(self, fileName, image): # const char *fileName, QFImage *image
        return QF_SaveImage(fileName, image), image
    
    def QF_ReleaseImage(self, image): # QFImage *image
        return QF_ReleaseImage(image)
    
    #ifdef _WIN32, Todo

    def QF_ConvertToBitmap(self, image): # QFImage *image
        return QF_ERR_UNSUPPORTED
    
    # User Feedback API
    def QF_SetUserFeedbackCallback(self, Callback): # void (*Callback)(UINT32 feedback)
        SetUserFeedbackFunc = ctypes.CFUNCTYPE(None, ctypes.c_uint32)
        self.setUserFeedbackFunc = SetUserFeedbackFunc(Callback)    
        QF_SetUserFeedbackCallback(self.setUserFeedbackFunc)
    

    def QF_SetUserFeedbackDataCallback(self, Callback): # void (*Callback)(const UserFeedbackData *feedbackData, void *userData), void *userData
        SetUserFeedbackDataFunc = ctypes.CFUNCTYPE(None, UserFeedbackData, ctypes.c_void_p)
        self.setUserFeedbackDataFunc = SetUserFeedbackDataFunc(Callback)
        userData = ctypes.c_void_p()
        QF_SetUserFeedbackDataCallback(self.setUserFeedbackDataFunc, userData)

    # Identify API
    def QF_Identify(self): # UINT32 *userID, BYTE *subID
        userID = ctypes.c_uint32()
        subID = ctypes.c_ubyte()

        return QF_Identify(userID, subID), userID.value, subID.value
    
    def QF_IdentifyTemplate(self, templateSize, templateData): # UINT32 templateSize, BYTE *templateData, UINT32 *userID, BYTE *subID
        tempBuffer = (ctypes.c_ubyte * templateSize)
        templateData = tempBuffer(*templateData)
        templateSize = ctypes.c_uint32(templateSize)
        userID = ctypes.c_uint32()
        subID = ctypes.c_ubyte()

        return QF_IdentifyTemplate(templateSize, templateData, userID, subID), userID.value, subID.value
    
    def QF_IdentifyImage(self, imageSize, imageData): # UINT32 imageSize, BYTE *imageData, UINT32 *userID, BYTE *subID
        imageBuffer = (ctypes.c_ubyte * imageSize)
        imageData = imageBuffer(*imageData)
        imageSize = ctypes.c_uint32(imageSize)
        userID = ctypes.c_uint32()
        subID = ctypes.c_ubyte()

        return QF_IdentifyImage(imageSize, imageData, userID, subID), userID.value, subID.value
    
    def QF_SetIdentifyCallback(self, Callback): # void (*Callback)(BYTE)
        SetIdentifyFunc = ctypes.CFUNCTYPE(None, ctypes.c_ubyte)
        self.setIdentifyFunc = SetIdentifyFunc(Callback)    
        QF_SetIdentifyCallback(self.setIdentifyFunc)

    # Verify API
    def QF_Verify(self, userID): # UINT32 userID, BYTE *subID
        userID = ctypes.c_uint32(userID)
        subID = ctypes.c_ubyte()

        return QF_Verify(userID, subID), subID.value
    
    def QF_VerifyTemplate(self, templateSize, templateData, userID): # UINT32 templateSize, BYTE *templateData, UINT32 userID, BYTE *subID
        tempBuffer = (ctypes.c_ubyte * templateSize)
        templateData = tempBuffer(*templateData)
        templateSize = ctypes.c_uint32(templateSize)
        userID = ctypes.c_uint32(userID)
        subID = ctypes.c_ubyte()

        return QF_VerifyTemplate(templateSize, templateData, userID, subID), subID.value

    def QF_VerifyHostTemplate(self, numOfTemplate, templateSize, templateData): # UINT32 numOfTemplate, UINT32 templateSize, BYTE *templateData
        numOfTemplate = ctypes.c_uint32()
        tempBuffer = (ctypes.c_ubyte * templateSize)
        templateData = tempBuffer(*templateData)
        templateSize = ctypes.c_uint32(templateSize)

        return QF_VerifyHostTemplate(numOfTemplate, templateSize, templateData)
    
    def QF_VerifyImage(self, imageSize, imageData, userID): # UINT32 imageSize, BYTE *imageData, UINT32 userID, BYTE *subID
        imageBuffer = (ctypes.c_ubyte * imageSize)
        imageData = imageBuffer(*imageData)
        imageSize = ctypes.c_uint32(imageSize)
        userID = ctypes.c_uint32(userID)
        subID = ctypes.c_ubyte()

        return QF_VerifyImage(imageSize, imageData, userID, subID), subID.value
    
    def QF_SetVerifyCallback(self, Callback): # void (*Callback)(BYTE)
        SetVerifyFunc = ctypes.CFUNCTYPE(None, ctypes.c_ubyte)
        self.setVerifyCallbackFunc = SetVerifyFunc(Callback)    
        QF_SetIdentifyCallback(self.setVerifyFunc)

    # Enroll API
    def QF_Enroll(self, userID, option): # UINT32 userID, QF_ENROLL_OPTION option, UINT32 *enrollID, UINT32 *imageQuality
        userID = ctypes.c_uint32(userID)
        #option = getattr(pylibQFM_SDK, option)
        enrollID = ctypes.c_uint32()
        imageQuality = ctypes.c_uint32()

        return QF_Enroll(userID, option, enrollID, imageQuality), enrollID.value, imageQuality.value

    def QF_EnrollTemplate(self, userID, option, templateSize, templateData): # UINT32 userID, QF_ENROLL_OPTION option, UINT32 templateSize, BYTE *templateData, UINT32 *enrollID
        userID = ctypes.c_uint32(userID)
        #option = getattr(pylibQFM_SDK, option)
        tempBuffer = (ctypes.c_ubyte * templateSize)
        templateData = tempBuffer(*templateData)
        templateSize = ctypes.c_uint32(templateSize)
        enrollID = ctypes.c_uint32()

        return QF_EnrollTemplate(userID, option, templateSize, templateData, enrollID), enrollID.value
    
    def QF_EnrollMultipleTemplates(self, userID, option, numOfTemplate, templateSize, templateData): # UINT32 userID, QF_ENROLL_OPTION option, int numOfTemplate, UINT32 templateSize, BYTE *templateData, UINT32 *enrollID
        userID = ctypes.c_uint32(userID)
        #option = getattr(pylibQFM_SDK, option)
        tempBuffer = (ctypes.c_ubyte * templateSize)
        templateData = tempBuffer(*templateData)
        templateSize = ctypes.c_uint32(templateSize)
        enrollID = ctypes.c_uint32()

        return QF_EnrollMultipleTemplates(userID, option, int(numOfTemplate), templateSize, templateData, enrollID), enrollID.value
    
    def QF_EnrollImage(self, userID, option, imageSize, imageData): # UINT32 userID, QF_ENROLL_OPTION option, UINT32 imageSize, BYTE *imageData, UINT32 *enrollID, UINT32 *imageQuality
        userID = ctypes.c_uint32(userID)
        #option = getattr(pylibQFM_SDK, option)
        imgbuf = (ctypes.c_ubyte * imageSize)
        imageData = imgbuf(*imageData)
        imageSize = ctypes.c_uint32(imageSize)
        enrollID = ctypes.c_uint32()
        imageQuality = ctypes.c_uint32()
        res = QF_EnrollImage(userID, option, imageSize, imageData, enrollID, imageQuality)
        
        return res, enrollID.value, imageQuality.value
    
    def QF_SetEnrollCallback(self, Callback): # void (*Callback)(BYTE errCode, QF_ENROLL_MODE enrollMode, int numOfSuccess)
        SetEnrollFunc = ctypes.CFUNCTYPE(None, ctypes.c_ubyte, QF_ENROLL_MODE, ctypes.c_int)
        self.setEnrollFunc = SetEnrollFunc(Callback)    
        QF_SetEnrollCallback(self.setEnrollFunc)
        
    # Delete API
    def QF_Delete(self, userID): # UINT32 userID
        userID = ctypes.c_uint32(userID)
        
        return QF_Delete(userID)
    
    def QF_DeleteOneTemplate(self, userID, subID): # UINT32 userID, int subID
        userID = ctypes.c_uint32(userID)

        return QF_DeleteOneTemplate(userID, int(subID))
    
    def QF_DeleteMultipleTemplates(self, startUserID, lastUserID): # UINT32 startUserID, UINT32 lastUserID, int *deletedUserID
        startUserID = ctypes.c_uint32(startUserID)
        lastUserID = ctypes.c_uint32(lastUserID)
        deletedUserID = ctypes.c_int()

        return QF_DeleteMultipleTemplates(startUserID, lastUserID, deletedUserID), deletedUserID.value
    
    def QF_DeleteAll(self):
        return QF_DeleteAll()
    
    def QF_SetDeleteCallback(self, Callback): # void (*Callback)(BYTE)
        SetDeleteFunc = ctypes.CFUNCTYPE(None, ctypes.c_ubyte)
        self.setDeleteFunc = SetDeleteFunc(Callback)    
        QF_SetDeleteCallback(self.setDeleteFunc)

    # Misc API
    def QF_ReadQRCode(self): # char* decodedText, int *decodedTextLength
        decodedText = ctypes.create_string_buffer(QF_QRCODE_DECODED_TEXT_SIZE)
        decodedTextLength = ctypes.c_int()

        return QF_ReadQRCode(decodedText, decodedTextLength), decodedText.value, decodedTextLength.value

    # Key management API
    
    def QF_ChangeKey(self, option, currentKey, newKey): # QF_KEY_OPTION option, BYTE *currentKey, BYTE *newKey
        #option = getattr(pylibQFM_SDK, option)
        currentBuf = (ctypes.c_ubyte * len(currentKey))
        neuBuf = (ctypes.c_ubyte * len(newKey))
        currentKey = currentBuf(*currentKey)
        newKey = neuBuf(*newKey)

        return QF_ChangeKey(option, currentKey, newKey)

    def QF_ResetKey(self, option): # QF_KEY_OPTION option
        #option = getattr(pylibQFM_SDK, option)
        return QF_ResetKey(option)

    # Secure Packet Protocol
    def QF_GetSecurePacketProtocolMode(self):
        return QF_GetSecurePacketProtocolMode()
    
    def QF_SetSecurePacketProtocolMode(self, securePacketProtocolMode, secureKey): # BOOL securePacketProtocolMode, BYTE *secureKey
        securePacketProtocolMode = ctypes.c_bool(securePacketProtocolMode)
        if not secureKey == None:
            buf = (ctypes.c_ubyte * len(secureKey))
            secureKey = buf(*secureKey)
            
        return QF_SetSecurePacketProtocolMode(securePacketProtocolMode, secureKey)
    
    def QF_SetSecureCode(self, secureCode): # BYTE *secureCode):
        buf = (ctypes.c_ubyte * len(secureCode))
        secureCode = buf(*secureCode)

        return QF_SetSecureCode(secureCode)

    def QF_CreateRandomSecureKey(self):
        return QF_CreateRandomSecureKey()
    
    def QF_CreateKeyPair(self, publicKey_host, privateKey_host): # BYTE *publicKey_host, BYTE *privateKey_host
        publicKey_host = ctypes.c_ubyte(publicKey_host)
        privateKey_host = ctypes.c_ubyte(privateKey_host)

        return QF_CreateKeyPair(publicKey_host, privateKey_host)
    
    def QF_GetSecureKey(self): # BYTE *secureKey, BYTE *publicKey_module, BYTE *privateKey_host
        secureKey = (ctypes.c_ubyte * 32)
        publicKey_module = ctypes.c_ubyte()
        privateKey_host = ctypes.c_ubyte()

        return QF_GetSecureKey(secureKey, publicKey_module, privateKey_host), secureKey.value, publicKey_module.value, privateKey_host.value
    
    def QF_PublicKeyExchange(self, privateKey_host, publicKey_module): # BYTE *publicKey_host, BYTE *publicKey_module
        privateKey_host = ctypes.c_ubyte()
        publicKey_module = ctypes.c_ubyte()

        return QF_PublicKeyExchange(privateKey_host, publicKey_module)

    # Deprecated API (Deprecated since v0.1.5. But still available for backward compatibility.)
    def QF_ResetSystemConfiguration(self):
        return QF_ResetSystemConfiguration()
    
    def QF_FormatUserDatabase(self):
        return QF_FormatUserDatabase()

    # Deprecated API (Deprecated since v0.3.3. But still available for backward compatibility.)
    def QF_ResetSystemParameter(self):
        return QF_ResetSystemParameter()

    # QF_Packet.h
    def QF_GetPacketValue(self, component, packet):
        packet = (ctypes.c_ubyte * QF_PACKET_LEN)(*packet)

        return QF_GetPacketValue(component, packet)

    def QF_ReadData(self, buf, size, timeout):
        buf = ctypes.c_ubyte()
        size = ctypes.c_int()
        timeout = ctypes.c_int()

        return QF_ReadData(buf, size, timeout)

    # QF_Packet.h: 58
    def QF_WriteData(self, buf, size, timeout):
        buf = ctypes.c_ubyte()
        size = ctypes.c_int()
        timeout = ctypes.c_int()

        return QF_WriteData(buf, size, timeout)
        
    # QF_Packet.h: 60
    def QF_ClearReadBuffer(self):
        return QF_ClearReadBuffer()


    # QF_Packet.h: 61
    def QF_ClearWriteBuffer(self):
        return QF_ClearWriteBuffer()
