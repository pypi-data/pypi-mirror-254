from ast import Bytes
from sys import byteorder
from .constants import VERSION,XGT_PORT,XGT_COMPANYID,XGT_CMD_RD,XGT_CMD_RD_ACK,XGT_CMD_WR,XGT_CMD_WR_ACK,XGT_DATA_BIT,XGT_DATA_BYTE,XGT_DATA_WORD, \
    XGT_DATA_DWORD,XGT_DATA_LWORD,XGT_DATA_CONTINUOUS,XGT_HEADER_PLCINFO,XGT_HD_PLCINFO,XGT_HD_CPUINFO,XGT_HD_SOURCEOFFRAME,XGT_HD_INVOKEID,XGT_HD_LENGTH,\
    XGT_HD_FENETPOSITION,XGT_HD_CHECKSUM,XGT_HD_COMMAND,XGT_HD_DATATYPE,XGT_HD_BLOCKCNT,XGT_HD_VARNAMELEN,XGT_HD_DATALEN,XGT_MAX_ARRAYSIZE,XGT_MAX_BLOCK_COUNT,\
    XGT_MAX_BLOCKNAMESIZE,XGT_STATUS_TST_OK,XGT_STATUS_NOT_CONNECTED,XGT_STATUS_SIZE_OVER,XGT_STATUS_INVOKEDID,XGT_STATUS_NAK,XGT_STATUS_WRITE_DATA_UNMATCH,\
    XGT_STATUS_DATATYPE,XGT_STATUS_CONNECT_ERR,XGT_STATUS_SEND_ERR,XGT_STATUS_RECV_ERR,XGT_STATUS_TIMEOUT_ERR,XGT_STATUS_SOCK_CLOSE_ERR, STATUS_TXT, \
    XGT_DATATYPE_DIC
from .utils import byte_length, set_bit, valid_host
import socket
from socket import AF_UNSPEC, SOCK_STREAM
import struct


class XGTClient:
    class _InternalError(Exception):
        pass
    
    class _NetworkError(_InternalError):
            def __init__(self, code, message):
                self.code = code
                self.message = message
                
    class _XGTExcept(_InternalError):
            def __init__(self, code):
                self.code = code
                
    def __init__(self, host='localhost', port=XGT_PORT, timeout=30.0,debug=False, auto_open=True, auto_close=False):
            """Constructor.

            :param host: hostname or IPv4/IPv6 address server address
            :type host: str
            :param port: TCP port number
            :type port: int
            :param unit_id: unit ID
            :type unit_id: int
            :param timeout: socket timeout in seconds
            :type timeout: float
            :param debug: debug state
            :type debug: bool
            :param auto_open: auto TCP connect
            :type auto_open: bool
            :param auto_close: auto TCP close)
            :type auto_close: bool
            :return: Object ModbusClient
            :rtype: ModbusClient
            """
            # private
            # internal variables
            self._host = None
            self._port = None            
            self._timeout = None
            self._debug = None
            self._auto_open = None
            self._auto_close = None
            self._sock = socket.socket()
            self._transaction_id = 0  # MBAP transaction ID
            self._version = VERSION  # this package version number
            self._last_error = 0  # last error code                     
            self._InvokeID = 0
            # public
            # constructor arguments: validate them with property setters
            self.host = host
            self.port = port            
            self.timeout = timeout
            self.debug = debug
            self.auto_open = auto_open
            self.auto_close = auto_close
            
            def __repr__(self):
                    r_str = 'XGTClient(host=\'%s\', port=%d, timeout=%.2f, debug=%s, auto_open=%s, auto_close=%s)'
                    r_str %= (self.host, self.port, self.timeout, self.debug, self.auto_open, self.auto_close)
                    return r_str
            
            def __del__(self):
                self.close()
                
    @property
    def version(self):
        """Return the current package version as a str."""
        return self._version
            
    @property
    def last_error(self):
        """Last error code."""
        return self._last_error
            
    @property
    def last_error_as_txt(self):
        """Human-readable text that describe last error."""
        return STATUS_TXT.get(self._last_error, 'unknown error')                       
            
    @property
    def host(self):
        """Get or set the server to connect to.

        This can be any string with a valid IPv4 / IPv6 address or hostname.
        Setting host to a new value will close the current socket.
        """
        return self._host
            

    @host.setter
    def host(self, value):
        # check type
        if type(value) is not str:
            raise TypeError('host must be a str')
        # check value
        if valid_host(value):
            if self._host != value:
                self.close()
                self._host = value
            return
        # can't be set
        raise ValueError('host can\'t be set (not a valid IP address or hostname)')
            
    @property
    def port(self):
        """Get or set the current TCP port (default is 8601).

        Setting port to a new value will close the current socket.
        """
        return self._port
            
    @port.setter
    def port(self, value):
        # check type
        if type(value) is not int:
            raise TypeError('port must be an int')
        # check validity
        if 0 < value < 65536:
            if self._port != value:
                self.close()
                self._port = value
            return
        # can't be set
        raise ValueError('port can\'t be set (valid if 0 < port < 65536)')
    @property
    def timeout(self):
        """Get or set requests timeout (default is 30 seconds).

        The argument may be a floating point number for sub-second precision.
        Setting timeout to a new value will close the current socket.
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        # enforce type
        value = float(value)
        # check validity
        if 0 < value < 3600:
            if self._timeout != value:
                self.close()
                self._timeout = value
            return
        # can't be set
        raise ValueError('timeout can\'t be set (valid between 0 and 3600)')
    @property
    def debug(self):
        """Get or set the debug flag (True = turn on)."""
        return self._debug

    @debug.setter
    def debug(self, value):
        # enforce type
        self._debug = bool(value)

    @property
    def auto_open(self):
        """Get or set automatic TCP connect mode (True = turn on)."""
        return self._auto_open

    @auto_open.setter
    def auto_open(self, value):
        # enforce type
        self._auto_open = bool(value)

    @property
    def auto_close(self):
        """Get or set automatic TCP close after each request mode (True = turn on)."""
        return self._auto_close

    @auto_close.setter
    def auto_close(self, value):
        # enforce type
        self._auto_close = bool(value)

    @property
    def is_open(self):
        """Get current status of the TCP connection (True = open)."""
        return self._sock.fileno() > 0

    def open(self):
        """Connect to modbus server (open TCP connection).

        :returns: connect status (True on success)
        :rtype: bool
        """
        try:
            self._open()
            return True
        except XGTClient._NetworkError as e:
            self._req_except_handler(e)
            return False

    def _open(self):
        """Connect to modbus server (open TCP connection)."""
        # open an already open socket -> reset it
        if self.is_open:
            self.close()
        # init socket and connect
        # list available sockets on the target host/port
        # AF_xxx : AF_INET -> IPv4, AF_INET6 -> IPv6,
        #          AF_UNSPEC -> IPv6 (priority on some system) or 4
        # list available socket on target host
        for res in socket.getaddrinfo(self.host, self.port, AF_UNSPEC, SOCK_STREAM):
            af, sock_type, proto, canon_name, sa = res
            try:
                self._sock = socket.socket(af, sock_type, proto)
            except socket.error:
                continue
            try:
                self._sock.settimeout(self.timeout)
                self._sock.connect(sa)
            except socket.error:
                self._sock.close()
                continue
            break
        # check connect status
        if not self.is_open:
            raise XGTClient._NetworkError(XGT_STATUS_NOT_CONNECTED, 'connection refused')

    def close(self):
        """Close current TCP connection."""
        self._sock.close()
            
    def readData(self, addrNameList):
        """XGT Client Read individual data       
        :param addrNameList:addressName list (Max 16 )
        :type addrNameList: list of address name ex)["%MW100", "%MW200"]
        :returns: data list or None if error
        :rtype: list of int or None
        """
               
        # check params
        if len(addrNameList) > XGT_MAX_BLOCK_COUNT or len(addrNameList) == 0:
            raise ValueError('addressName list size error 1~16')
        #대문자 변환
        addrNameList = [x.upper() for x in addrNameList]
                              
        #입력 검사
        for i in range(0, len(addrNameList)):
            address = addrNameList[i]
            
            if i==0 :
                FirstDataType = address[2]
            else:
                if FirstDataType != address[2]:
                    raise ValueError('The data types in the list do not match')
                   
            if address[0] == '%':
                devicename = address[1]
                datatypename = address[2]
                                                      
                if devicename < 'A' or devicename > 'Z':
                    raise ValueError('Device name Error')
                    
                if not(datatypename =='X' or datatypename =='B' or datatypename =='W' or datatypename =='D' or datatypename =='L'):
                    raise ValueError('Data Type Error')  
                        
                if len(address) > XGT_MAX_BLOCKNAMESIZE:
                    raise ValueError('AddressName is too long')
            else:
                raise ValueError('Addr Format Error')
                                             
        BlockCount = len(addrNameList);
        # make request                    
        try:                                
            #Command                        
            tx_Frame = struct.pack('<HHHH', XGT_CMD_RD, XGT_DATATYPE_DIC.get(datatypename), 0, BlockCount)
            #Block                    
            Address = 0;
            for Address in addrNameList:
                #BlockData = bytes('%'+devicename+datatypename+str(Address), 'utf-8')                        
                BlockData = bytes(Address, 'utf-8')
                tx_Frame = tx_Frame + struct.pack('<H', len(BlockData)) + BlockData
                        
            #header LSIS-XGT~~~BCC                    
            DataLength = len(tx_Frame);
            CpuInfo = 0xa0
            SourceOfFrame = 0x33            
            Header = bytes(XGT_COMPANYID, 'utf-8') + struct.pack('I', 0x00000000)
            Header += CpuInfo.to_bytes(1, 'little') + SourceOfFrame.to_bytes(1, 'little')
                       
            Header += struct.pack('<HHB', self._InvokeID, DataLength, 0)
            
            ByteCheckSum = 0
            for singleByte in Header:
                ByteCheckSum += singleByte
            ByteCheckSum = ByteCheckSum%0x100
            Header= Header + ByteCheckSum.to_bytes(1, 'little')
                                
            tx_Frame = Header + tx_Frame
                        
            self._send(tx_Frame)
            rx_Frame = self._recv(1518)
                    
            if(len(rx_Frame) >= 20 ):                    
                rx_Command = int.from_bytes(rx_Frame[XGT_HD_COMMAND:(XGT_HD_COMMAND+2)], byteorder='little')
                rx_DataType = int.from_bytes(rx_Frame[XGT_HD_DATATYPE:(XGT_HD_DATATYPE+2)], byteorder='little')
                rx_ErrorState =  int.from_bytes(rx_Frame[XGT_HD_BLOCKCNT:(XGT_HD_BLOCKCNT+2)], byteorder='little')
                rx_InvokeID = int.from_bytes(rx_Frame[XGT_HD_INVOKEID:(XGT_HD_INVOKEID+2)], byteorder='little')
                rx_BlockCnt = int.from_bytes(rx_Frame[XGT_HD_VARNAMELEN:(XGT_HD_VARNAMELEN+2)], byteorder='little')
                rx_RdDataPos = XGT_HD_DATALEN
                rxRdDataSize = 0
                rxRdData = 0
                ret_Data = []
                if rx_Command == XGT_CMD_RD_ACK:
                        if rx_InvokeID == self._InvokeID:
                            if rx_ErrorState == 0:
                                for i in range(0, rx_BlockCnt):
                                    rxRdDataSize =  int.from_bytes(rx_Frame[rx_RdDataPos:(rx_RdDataPos+2)], byteorder='little')
                                    rx_RdDataPos = rx_RdDataPos + 2
                                    rx_RdData = int.from_bytes(rx_Frame[rx_RdDataPos:(rx_RdDataPos+rxRdDataSize)], byteorder='little')
                                    rx_RdDataPos = rx_RdDataPos + rxRdDataSize
                                       
                                    ret_Data.append(rx_RdData)
                                return ret_Data
                            else:
                                raise ValueError('Nak Error')                                   
                        else:
                            raise ValueError('InvokedID Error')     
                else:
                    raise ValueError('Received Cmmand Not Match')                   
        # handle error during request
        except XGTClient._InternalError as e:
            self._req_except_handler(e)
            return None
        
        self._InvokeID = self._InvokeID + 1


    def readContinuousData(self, addrName, readCount):
        """XGT Client ReadContinuousData (ByteType Only)       
        :param addrName:addressName(string)
        :type addrName: string ex)%MB100
        :param readCount:read Data Count
        :type readCount: int
        :returns: bits list or None if error
        :rtype: list of UINT64 or None
        """
                       
        #대문자 변환
        addrName = addrName.upper()
                      
        #입력 검사        
        if addrName[0] == '%':
            devicename = addrName[1]
            datatypename = addrName[2]
                        
            if devicename < 'A' or devicename > 'Z':
                raise ValueError('Device name Error')
                    
            if not(datatypename =='B'):
                raise ValueError('Data Type Is Not Byte Type')  
                        
            if len(addrName) > XGT_MAX_BLOCKNAMESIZE:
                raise ValueError('AddressName is too long')
        else:
            raise ValueError('Addr Format Error')
        
        ReadSingleDataSize = 1
        if(readCount < 1):
            raise ValueError('readCount Is Too small')
        
        if(readCount > 1400):
            raise ValueError('readCount Is Too Big')
                                
        BlockCount = 1
        # make request                    
        try:                                
            #Command                        
            tx_Frame = struct.pack('<HHHH', XGT_CMD_RD, XGT_DATA_CONTINUOUS, 0, BlockCount)
            #Block Only 1                                
            BlockData = bytes(addrName, 'utf-8')
            tx_Frame = tx_Frame + struct.pack('<H', len(BlockData)) + BlockData + struct.pack('<H', readCount)
                        
            #header LSIS-XGT~~~BCC                    
            DataLength = len(tx_Frame);
            CpuInfo = 0xa0
            SourceOfFrame = 0x33
            
            Header = bytes(XGT_COMPANYID, 'utf-8') + struct.pack('I', 0x00000000)
            Header += CpuInfo.to_bytes(1, 'little') + SourceOfFrame.to_bytes(1, 'little')
                       
            Header += struct.pack('<HHB', self._InvokeID, DataLength, 0)
            
            ByteCheckSum = 0
            for singleByte in Header:
                ByteCheckSum += singleByte
            ByteCheckSum = ByteCheckSum%0x100
            Header= Header + ByteCheckSum.to_bytes(1, 'little')
                                
            tx_Frame = Header + tx_Frame
                        
            self._send(tx_Frame)
            rx_Frame = self._recv(1518)
                    
            if(len(rx_Frame) >= 20 ):                    
                rx_Command = int.from_bytes(rx_Frame[XGT_HD_COMMAND:(XGT_HD_COMMAND+2)], byteorder='little')
                rx_DataType = int.from_bytes(rx_Frame[XGT_HD_DATATYPE:(XGT_HD_DATATYPE+2)], byteorder='little')
                rx_ErrorState =  int.from_bytes(rx_Frame[XGT_HD_BLOCKCNT:(XGT_HD_BLOCKCNT+2)], byteorder='little')
                rx_InvokeID = int.from_bytes(rx_Frame[XGT_HD_INVOKEID:(XGT_HD_INVOKEID+2)], byteorder='little')
                rx_BlockCnt = int.from_bytes(rx_Frame[XGT_HD_VARNAMELEN:(XGT_HD_VARNAMELEN+2)], byteorder='little')
                rx_RdDataPos = XGT_HD_DATALEN
                rxRdDataSize = 0
                rxRdData = 0
                ret_Data = []
                if rx_Command == XGT_CMD_RD_ACK:
                        if rx_InvokeID == self._InvokeID:
                            if rx_ErrorState == 0:
                                if(rx_BlockCnt == 1):
                                    rx_CoutinuousDataCount =  int.from_bytes(rx_Frame[rx_RdDataPos:(rx_RdDataPos+2)], byteorder='little')
                                    rx_RdDataPos = rx_RdDataPos + 2
                                    
                                    for j in range(0, rx_CoutinuousDataCount):
                                        rx_RdData = int.from_bytes(rx_Frame[rx_RdDataPos:(rx_RdDataPos+ReadSingleDataSize)], byteorder='little')
                                        rx_RdDataPos = rx_RdDataPos + ReadSingleDataSize                                       
                                        ret_Data.append(rx_RdData)
                                    return ret_Data                                
                                else:
                                    raise ValueError('BlockCount Error')
                            else:
                                raise ValueError('Nak Error')                                   
                        else:
                            raise ValueError('InvokedID Error')     
                else:
                    raise ValueError('Received Cmmand Not Match')                   
        # handle error during request
        except XGTClient._InternalError as e:
            self._req_except_handler(e)
            return None
        
        self._InvokeID = self._InvokeID + 1
    
    def writeData(self, addrNameList, dataList):
            """XGT Client Write individual data      
            :param addrList:address list (Max 16)
            :type addrList: list of address name ex)%MW100
            :param dataList:wirte data list(List Max 16)
            :type dataList: list of int
            :returns: bits list or None if error
            :rtype: list of UINT64 or None
            """
               
            # check params
            if len(addrNameList) > XGT_MAX_BLOCK_COUNT or len(addrNameList) == 0:
                raise ValueError('addrNameList size error 1~16')
            
            if len(dataList) > XGT_MAX_BLOCK_COUNT or len(dataList) == 0:
                raise ValueError('dataList list size error 1~16')
            
            if len(addrNameList) != len(dataList):
                raise ValueError('dataList dataList sizes do not match ')
            
            #대문자 변환
            addrNameList = [x.upper() for x in addrNameList]
                               
            #입력 검사
            for i in range(0, len(addrNameList)):
                address = addrNameList[i]
                if i==0 :
                    FirstDataType = address[2]
                else:
                    if FirstDataType != address[2]:
                        raise ValueError('data types in the list do not match')
                        
                if address[0] == '%':
                    devicename = address[1]
                    datatypename = address[2]
                        
                    if devicename < 'A' or devicename > 'Z':
                        raise ValueError('Device name Error')
                    
                    if not(datatypename =='X' or datatypename =='B' or datatypename =='W' or datatypename =='D' or datatypename =='L'):
                        raise ValueError('Data Type Error')  
                        
                    if len(address) > XGT_MAX_BLOCKNAMESIZE:
                        raise ValueError('AddressName is too long')
                else:
                    raise ValueError('Addr Format Error')
                                                     
            BlockCount = len(addrNameList);
            # make request                    
            try:                                
                #Command                        
                tx_Frame = struct.pack('<HHHH', XGT_CMD_WR, XGT_DATATYPE_DIC.get(datatypename), 0, BlockCount)
                #Block                    
                Address = 0;
                for Address in addrNameList:                                            
                    BlockData = bytes(Address, 'utf-8')
                    tx_Frame = tx_Frame + struct.pack('<H', len(BlockData)) + BlockData                                             

                for i in range(0, len(addrNameList)):
                    Address = addrNameList[i]
                    Data = dataList[i]                                            
                                                            
                    if Address[2] == 'X':
                        tx_Frame = tx_Frame + struct.pack('<H', 1) +  Data.to_bytes(1, byteorder="little")
                    elif Address[2] == 'B':
                        tx_Frame = tx_Frame + struct.pack('<H', 1) +  Data.to_bytes(1, byteorder="little")
                    elif Address[2] == 'W':    
                        tx_Frame = tx_Frame + struct.pack('<H', 2) +  Data.to_bytes(2, byteorder="little")
                    elif Address[2] == 'D':    
                        tx_Frame = tx_Frame + struct.pack('<H', 4) +  Data.to_bytes(4, byteorder="little")
                    elif Address[2] == 'L':    
                        tx_Frame = tx_Frame + struct.pack('<H', 8) +  Data.to_bytes(8, byteorder="little")
                    else :
                        raise ValueError('Addr Format Error')
                                                                      
                #header LSIS-XGT~~~BCC                    
                DataLength = len(tx_Frame);
                CpuInfo = 0xa0
                SourceOfFrame = 0x33
                
                Header = bytes(XGT_COMPANYID, 'utf-8') + struct.pack('I', 0x00000000)
                Header += CpuInfo.to_bytes(1, 'little') + SourceOfFrame.to_bytes(1, 'little')
                       
                Header += struct.pack('<HHB', self._InvokeID, DataLength, 0)
            
                ByteCheckSum = 0
                for singleByte in Header:
                    ByteCheckSum += singleByte
                ByteCheckSum = ByteCheckSum%0x100
                Header= Header + ByteCheckSum.to_bytes(1, 'little')
                                
                tx_Frame = Header + tx_Frame
                        
                self._send(tx_Frame)
                rx_Frame = self._recv(1518)
                    
                if(len(rx_Frame) >= 20 ):                    
                    rx_Command = int.from_bytes(rx_Frame[XGT_HD_COMMAND:(XGT_HD_COMMAND+2)], byteorder='little')
                    rx_DataType = int.from_bytes(rx_Frame[XGT_HD_DATATYPE:(XGT_HD_DATATYPE+2)], byteorder='little')
                    rx_ErrorState =  int.from_bytes(rx_Frame[XGT_HD_BLOCKCNT:(XGT_HD_BLOCKCNT+2)], byteorder='little')
                    rx_InvokeID = int.from_bytes(rx_Frame[XGT_HD_INVOKEID:(XGT_HD_INVOKEID+2)], byteorder='little')                                      
                    
                    if rx_Command == XGT_CMD_WR_ACK:
                        if rx_InvokeID == self._InvokeID:
                            if rx_ErrorState == 0:                                    
                                return True
                            else:
                                raise ValueError('Nak Error')                                   
                        else:
                            raise ValueError('InvokedID Error')     
                    else:
                        raise ValueError('Received Cmmand Not Match')                   
            # handle error during request
            except XGTClient._InternalError as e:
                self._req_except_handler(e)
                return False
        
            self._InvokeID = self._InvokeID + 1        

    def writeContinuousData(self, addrName, dataList):
            """XGT Client WriteContinuousData (ByteType Only)       
            :param addrName:addressName(string)
            :type addrName: string ex)%MB100
            :param dataList:read Data Count
            :type readCount: list of int
            :returns:true or false            
            """
               
            # check params            
            #대문자 변환
            addrName = addrName.upper()
                
            devicename = 'M'
            datatypename = 'W'
                
            #입력 검사            
            if addrName[0] == '%':
                devicename = addrName[1]
                datatypename = addrName[2]
                        
                if devicename < 'A' or devicename > 'Z':
                    raise ValueError('Device name Error')
                    
                if not(datatypename =='B'):
                    raise ValueError('Data Type Is Not Byte Type')  
                        
                if len(addrName) > XGT_MAX_BLOCKNAMESIZE:
                    raise ValueError('AddressName is too long')
            else:
                raise ValueError('AddrName Format Error')
            
            if len(dataList) < 1 :
                raise ValueError('dataList Size Is Too Short')
            if len(dataList) > 1400 :
                raise ValueError('dataList Size Is Too Long')
                        
            BlockCount = 1;
            # make request                    
            try:                                
                #Command                        
                tx_Frame = struct.pack('<HHHH', XGT_CMD_WR, XGT_DATA_CONTINUOUS, 0, BlockCount)
                
                #Block Only 1                                             
                BlockData = bytes(addrName, 'utf-8')
                tx_Frame = tx_Frame + struct.pack('<H', len(BlockData)) + BlockData                                             

                tx_Frame = tx_Frame + struct.pack('<H', len(dataList))
                for Data in dataList:                                                                                                              
                    tx_Frame = tx_Frame + Data.to_bytes(1, byteorder="little")
                                                                      
                #header LSIS-XGT~~~BCC                    
                DataLength = len(tx_Frame);
                CpuInfo = 0xa0
                SourceOfFrame = 0x33
                
                Header = bytes(XGT_COMPANYID, 'utf-8') + struct.pack('I', 0x00000000)
                Header += CpuInfo.to_bytes(1, 'little') + SourceOfFrame.to_bytes(1, 'little')
                       
                Header += struct.pack('<HHB', self._InvokeID, DataLength, 0)
            
                ByteCheckSum = 0
                for singleByte in Header:
                    ByteCheckSum += singleByte
                ByteCheckSum = ByteCheckSum%0x100
                Header= Header + ByteCheckSum.to_bytes(1, 'little')
                                
                tx_Frame = Header + tx_Frame
                        
                self._send(tx_Frame)
                rx_Frame = self._recv(1518)
                    
                if(len(rx_Frame) >= 20 ):                    
                    rx_Command = int.from_bytes(rx_Frame[XGT_HD_COMMAND:(XGT_HD_COMMAND+2)], byteorder='little')
                    rx_DataType = int.from_bytes(rx_Frame[XGT_HD_DATATYPE:(XGT_HD_DATATYPE+2)], byteorder='little')
                    rx_ErrorState =  int.from_bytes(rx_Frame[XGT_HD_BLOCKCNT:(XGT_HD_BLOCKCNT+2)], byteorder='little')
                    rx_InvokeID = int.from_bytes(rx_Frame[XGT_HD_INVOKEID:(XGT_HD_INVOKEID+2)], byteorder='little')                                      
                    
                    if rx_Command == XGT_CMD_WR_ACK:
                        if rx_InvokeID == self._InvokeID:
                            if rx_ErrorState == 0:                                    
                                return True
                            else:
                                raise ValueError('Nak Error')                                   
                        else:
                            raise ValueError('InvokedID Error')     
                    else:
                        raise ValueError('Received Cmmand Not Match')                   
            # handle error during request
            except XGTClient._InternalError as e:
                self._req_except_handler(e)
                return False
        
            self._InvokeID = self._InvokeID + 1

    def _send(self, frame):
        """Send frame over current socket.

        :param frame: modbus frame to send (MBAP + PDU)
        :type frame: bytes
        """
        # check socket
        if not self.is_open:
            raise XGTClient._NetworkError(XGT_STATUS_SOCK_CLOSE_ERR, 'try to send on a close socket')
        # send
        try:
            self._sock.send(frame)
        except socket.timeout:
            self._sock.close()
            raise XGTClient._NetworkError(XGT_STATUS_TIMEOUT_ERR, 'timeout error')
        except socket.error:
            self._sock.close()
            raise XGTClient._NetworkError(XGT_STATUS_SEND_ERR, 'send error')

    def _recv(self, size):
        """Receive data over current socket.

        :param size: number of bytes to receive
        :type size: int
        :returns: receive data or None if error
        :rtype: bytes
        """
        try:
            r_buffer = self._sock.recv(size)
        except socket.timeout:
            self._sock.close()
            raise XGTClient._NetworkError(XGT_STATUS_TIMEOUT_ERR, 'timeout error')
        except socket.error:
            r_buffer = b''
        # handle recv error
        if not r_buffer:
            self._sock.close()
            raise XGTClient._NetworkError(XGT_STATUS_RECV_ERR, 'recv error')
        return r_buffer

            

    def _req_init(self):
        """Reset request status flags."""
        self._last_error = 0                

    def _req_except_handler(self, _except):
        """Global handler for internal exceptions."""
        # on request network error
        self._last_error = _except.code
        self._debug_msg(_except.message)            
               
    def _debug_msg(self, msg):
        """Print debug message if debug mode is on.

        :param msg: debug message
        :type msg: str
        """
        if self.debug:
            print(msg)
           