from sales_person import SalesPerson
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        for line in file:
            line_split = line.split(", ")
            employee_id = line_split[0]
            name = line_split[1]
            sales_person = SalesPerson(employee_id, name)
            line_splitamts = line_split[2].split(" ")

            for amt in line_splitamts:
                sales_person.enter_sale(float(amt))
            self.sales_people.append(sales_person)
        return None

    def quota_report(self, quota):
        returnlist = []
        empID = []
        empNames = []
        TotalSales =[]
        MetQuota = []
        for person in self.sales_people:
            empID.append(person.get_id())
            empNames.append(person.get_name())
            TotalSales.append(person.total_sales())
            if person.total_sales() >= quota:
                MetQuota.append(True)
            else:
                MetQuota.append(False)
        returnlist.append(empID)
        returnlist.append(empNames)
        returnlist.append(TotalSales)
        returnlist.append(MetQuota)
        return returnlist

    def top_seller(self):
        highest_sellers = []
        highest_seller = self.sales_people[0]
        highest_sale_amt = highest_seller.total_sales()
        highest_sellers.append(highest_seller)

        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales() > highest_sale_amt:
                highest_sellers.clear()
                highest_seller = self.sales_people[i]
                highest_sale_amt = highest_seller.total_sales()
                highest_sellers.append(highest_seller)
            elif self.sales_people[i].total_sales() == highest_sale_amt:
                highest_sellers.append(self.sales_people[i])
        return highest_sellers

    def individual_sales(self, employee_id):
        for spo in self.sales_people:
            if spo.get_id == employee_id:
                return spo
        return None
