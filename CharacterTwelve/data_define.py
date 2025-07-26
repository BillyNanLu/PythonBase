"""
数据定义的类
"""


class Record:

    def __init__(self, date, order_id, money, province):
        self.date = date            # 订单日期
        self.order_id = order_id    # 订单ID
        self.money = money          # 订单金额
        self.province = province    # 销售省份


    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"


    # def to_json(self):
    #     d = {"date": self.date, "order_id": self.order_id, "money": self.money, "province": self.province}
    #     import json
    #     return json.dumps(d)

    def to_json(self):
        import json
        from datetime import date  # 确保导入date类

        # 自定义日期转换器
        def convert_date(obj):
            if isinstance(obj, date):
                return obj.isoformat()  # 转换为"YYYY-MM-DD"格式字符串
            raise TypeError(f"无法序列化类型: {type(obj)}")

        d = {
            "date": self.date,
            "order_id": self.order_id,
            "money": self.money,
            "province": self.province
        }
        # 使用default参数指定转换器
        return json.dumps(d, default=convert_date, ensure_ascii=False)
