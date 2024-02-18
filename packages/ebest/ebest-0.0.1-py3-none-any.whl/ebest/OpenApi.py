import asyncio
import aiohttp
import websockets
import json
from ebest.tr_code_to_path import tr_code_to_path
from ebest.code_realtime_account import code_realtime_account

BASE_URL = "https://openapi.ebestsec.co.kr:8080"
WSS_URL_REAL = "wss://openapi.ebestsec.co.kr:9443/websocket"
WSS_URL_SIMULATION = "wss://openapi.ebestsec.co.kr:29443/websocket"

class ResponseValue:
    # __slots__ = ("tr_cont", "tr_cont_key", "body")
    def __init__(
        self,
        tr_cont: str,
        tr_cont_key: str,
        body: dict,
    ) -> None:
        self.tr_cont = tr_cont
        self.tr_cont_key = tr_cont_key
        self.body = body

class OpenApi:
    def __init__(self):
        super().__init__()
        
        self._access_token = "";
        self._http = None;
        self._websocket = None;
        self._connected:bool = False;
        self._is_simulation:bool = False;
        self._last_message:str = "";
        self._mac_address : str|None = None;
    
        # 이벤트 핸들러
        self._on_message = lambda sender, msg: print(f"on_message: {msg}");
        self._on_realtime = lambda sender, trcode, key, realtimedata: print(f"on_realtime: {trcode}, {key}, {realtimedata}")
        self._is_async_on_message:bool = False;
        self._is_async_on_realtime:bool = False;

    @property
    def connected(self) -> bool:
        """Is login state.

        A readonly property.
        """
        return self._connected
    
    @property
    def is_simulation(self) -> bool:
        """server is simulation.

        A readonly property.
        """
        return self._is_simulation

    @property
    def last_message(self) -> str:
        """last error message.

        A readonly property.
        """
        return self._last_message

    @property
    def mac_address(self) -> str:
        """법인인 경우 필수 세팅"""
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value:str) : self._mac_address = value

    @property
    def on_message(self) :
        """메시지 수신 이벤트 핸들러
        on_message(sender:OpenApi, msg:str)
        """
        return self._on_message
    
    @on_message.setter
    def on_message(self, value) :
        self._is_async_on_message = asyncio.iscoroutinefunction(value);
        self._on_message = value

    @property
    def on_realtime(self) :
        """실시간 데이터 수신 이벤트 핸들러
        on_realtime(sender:OpenApi, trcode:str, key:str, realtimedata:dict)
        """
        return self._on_realtime
    
    @on_realtime.setter
    def on_realtime(self, value) :
        self._is_async_on_realtime = asyncio.iscoroutinefunction(value);
        self._on_realtime = value
    
    async def close(self) -> None:
        self._connected = False;
        if self._http and not self._http.closed:
            await self._http.close()
        if self._websocket and not self._websocket.closed:
            await self._websocket.close()

    async def login(self, appkey:str, appsecretkey:str) -> bool:
        '''
        로그인 요청
        appkey: 앱키
        appsecretkey: 앱시크릿키
        return: True: 성공, False: 실패, 실패시 last_message에 실패사유가 저장됨
        '''
        if self._connected :
            self._last_message = "aleady connected";
            return True;
        
        if appkey == "" or appsecretkey == "":
            self._last_message = "appkey or appsecretkey is empty";
            return False;
    
        # 토큰 가져오기
        httpclient = aiohttp.ClientSession();
        token_response = await httpclient.post(BASE_URL + "/oauth2/token"
                    , data={'grant_type': 'client_credentials', 'appkey': appkey, 'appsecretkey': appsecretkey, 'scope': 'oob'}
                    );
        if token_response.status != 200:
            await httpclient.close();
            self._last_message = "Failed to retrieve authentication key.";
            return False;
    
        # 인증성공
        token = (await token_response.json())['access_token'];
        httpclient.headers["Authorization"] = f"Bearer {token}";
        httpclient.headers["Content-Type"] = "application/json; charset=UTF-8";
        self._access_token = token;
        self._http = httpclient;
        self._connected = True;
        
        # 모의투자인지 실투자인지 구분한다.
        CSPAQ12300 = dict();
        CSPAQ12300['CSPAQ12300InBlock1'] = {
            "BalCreTp":"0",
            "CmsnAppTpCode":"0",
            "D2balBaseQryTp":"0",
            "UprcTpCode":"0",
        };
        
        response = await self.request("CSPAQ12300", CSPAQ12300);
        if not response :
            self._connected = False;
            self._last_message = "Failed to require CSPAQ12300";
            await httpclient.close();
            return False;
    
        rsp_msg:str = response.body["rsp_msg"];
        if rsp_msg.__contains__("모의투자"):
            self._is_simulation = True;

        # 웹소켓 연결
        self._connected = False;
        try:
            websocket = await websockets.connect(WSS_URL_SIMULATION if self._is_simulation else WSS_URL_REAL, open_timeout=3)
            self._connected = websocket.open;
        except :
            pass
    
        if not self._connected:
            await httpclient.close();
            self._last_message = "websocket connection failed.";
            return False;
    
        self._websocket = websocket;
        asyncio.create_task(self._websocket_listen());
        return True;
    

    async def request(self, tr_cd:str, data:dict
                             ,*
                             , path:str=None
                             , tr_cont:str="N"
                             , tr_cont_key:str="0"
                             ) -> ResponseValue | None:
        '''
        TR데이터 요청
        tr_cd: TR코드
        data: 데이터
        return: 성공시 ResponseValue, 실패시 None, 실패시 last_message에 실패사유가 저장됨
        '''
        self._last_message = "";
        if not self._connected:
            self._last_message = "Not connected";
            return None;

        if not path:
            if not tr_code_to_path.__contains__(tr_cd):
                self._last_message = "Not supported tr code";
                return None;
            path = tr_code_to_path[tr_cd];
    
        headers = dict();
        headers["tr_cd"] = tr_cd;
        headers["tr_cont"] = tr_cont;
        headers["tr_cont_key"] = tr_cont_key;
        if self._mac_address:
            headers["mac_address"] = self._mac_address;
        
        try:
            response = await self._http.post(BASE_URL + path, headers=headers, data=json.dumps(data));
            if response.status != 200:
                self._last_message = await response.json();
                return None;
            body = await response.json();
            return ResponseValue(response.headers["tr_cont"], response.headers["tr_cont_key"], body);
        except Exception as e:
            self._last_message = e;

        return None;        

    def add_realtime(self, tr_cd:str, tr_key:str) : return self._realtime_request(tr_cd , tr_key, "1" if code_realtime_account.__contains__(tr_cd) else "3");
    def remove_realtime(self, tr_cd:str, tr_key:str) : return self._realtime_request(tr_cd, tr_key, "2" if code_realtime_account.__contains__(tr_cd) else "4");

    async def _websocket_listen(self):
        while True:
            try:
                data = await self._websocket.recv();
                jsondata = json.loads(data);
            except Exception as e:
                self._last_message = e;
                if self._websocket.closed:
                    await self._inner_on_mesage(f"websocket closed. {e}");
                    break;
                else:
                    await self._inner_on_mesage(f"websocket exception. {e}");
                    continue;
            header = jsondata.get("header", None);
            if header != None:
                tr_cd = header.get("tr_cd", None);
                if tr_cd != None:
                    rsp_msg = header.get("rsp_msg", None);
                    if rsp_msg != None:
                        self._last_message = ""
                        await self._inner_on_mesage(f"{tr_cd}: {rsp_msg}");
                    body = jsondata.get("body", None);
                    tr_key = header.get("tr_key", None);
                    if body != None and tr_key != None:
                        await self._inner_on_realtime(tr_cd, tr_key, body)

    async def _realtime_request(self, tr_cd:str, tr_key:str, tr_type:str) -> bool:
        if not self._connected: return False;
        data = f"{{\"header\":{{\"token\":\"{self._access_token}\",\"tr_type\":\"{tr_type}\"}},\"body\":{{\"tr_cd\":\"{tr_cd}\",\"tr_key\":\"{tr_key}\"}}}}";
        await self._websocket.send(data);
        return True;

    async def _inner_on_mesage(self, msg:str):
        if self._is_async_on_message:
            await self._on_message(self, msg);
        else:
            self._on_message(self, msg);

    async def _inner_on_realtime(self, trcode:str, key:str, realtimedata):
        if self._is_async_on_realtime:
            await self._on_realtime(self, trcode, key, realtimedata);
        else:
            self._on_realtime(self, trcode, key, realtimedata);
