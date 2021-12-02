class SalesPerson:
    def __init__(self, employee_id, name):
        self.id = employee_id
        self.name = name
        sales = []
        self.sales = sales
        self.sum = 0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)
        self.sum = self.sum + sale

    def total_sales(self):
        return self.sum

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if self.total_sales() < other:
            return -1
        elif self.total_sales() > other:
            return 1
        else:
            return 0

    def __str__(self):
        return self.id + self.name + ":" + self.total_sales()
