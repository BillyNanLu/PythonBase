class Phone8:
    IMEI = None  # 序列号
    producer = "Apple"  # 厂商

    def call_by_4g(self):
        print("2018年：4G通话")

class Phone16(Phone8):
    IMEI = None
    face_id = "10001"  # 面部识别ID

    def call_by_5g(self):
        print("2025年：5G+通话")

phone = Phone16()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


class NFCReader(Phone16):
    nfc_type = "第十代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class Phone17(NFCReader):
    pass

phone = Phone17()
print(phone.producer)
phone.call_by_5g()
phone.read_card()
phone.write_card()
