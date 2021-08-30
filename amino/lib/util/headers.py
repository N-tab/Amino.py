from amino.lib.util import device

sid = None

#by N_F (N-tab)

class Headers:
    def __init__(self, dev = device.DeviceGenerator(),data = None, type = None, sid = None):
        headers = {
            "NDCDEVICEID": dev.device_id,
            "NDCLANG": "ru",
            "Accept-Language": "ru-RU",
            "SMDEVICEID": "6e28d4c5-2d25-4977-93ec-9a4ce077fb7b",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8 Build/PKQ1.190616.001; com.narvii.amino.master/3.4.33578)",
            "Host": "service.narvii.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }

        if data: headers["Content-Length"] = str(len(data))
        if sid: headers["NDCAUTH"] = sid
        if type: headers["Content-Type"] = type
        self.headers = headers
