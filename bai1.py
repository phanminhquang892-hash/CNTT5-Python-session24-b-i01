"""
1. Việc gán trực tiếp:
   order_table1.total_amount = 0
 - Vi phạm tính Đóng gói của OOP vì thuộc tính total_amount đang là public nên có thể bị sửa đổi từ bên ngoài

2. Để ngăn truy cập trực tiếp từ bên ngoài, đổi:
 thay  self.total_amount = self.__total_amount

3. Nếu muốn các phần khác của chương trình chỉ được xem tổng tiền
   mà không được phép sửa, sử dụng Decorator: @property

4. Trong hàm update_vat_rate cũ:
 - self.vat_rate = new_rate
 - Python không sửa Class Attribute vat_rate mà tạo ra một Instance Attribute mới


5. Để cập nhật VAT cho toàn bộ hóa đơn,
 - cần dùng: @classmethod và thay tham số self bằng cls
 - Khi đó:
 - cls.vat_rate = new_rate
 - sẽ thay đổi Class Attribute và mọi đối tượng đều sử dụng mức VAT mới
"""

class CoffeeOrder:
    vat_rate = 0.10
    
    def __init__(self):
        self.table_number = self.table_number
        self.__total_amount = 0
    
    def add_item(self, price):
        if price > 0:
            self.__total_amount += price
        
    @property 
    def total_amount(self):
        return self.__total_amount
    def calculate_final_bill(self):
        return self.__total_amount + (self.__total_amount * CoffeeOrder.vat_rate)
    
    @classmethod 
    def update_vat_rate(cls, new_rate):
        if 0 <= new_rate <= 1:
            cls.vat_rate = new_rate

order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")
order_table1.add_item(50000)
order_table2.add_item(30000)

print("=== Trước khi đổi VAT ===")
print(f"Tổng tiền Bàn 1: {order_table1.total_amount} VNĐ")
print(f"Tổng tiền Bàn 2: {order_table2.total_amount} VNĐ")
print(f"VAT hệ thống: {CoffeeOrder.vat_rate * 100}%")

try:
    order_table1.total_amount = 0
except AttributeError:
    print("\nKhông thể sửa total_amount trực tiếp vì thuộc tính chỉ đọc.")

CoffeeOrder.update_vat_rate(0.08)
print("\n=== Sau khi đổi VAT ===")
print(f"VAT Bàn 1: {order_table1.vat_rate * 100}%")
print(f"VAT Bàn 2: {order_table2.vat_rate * 100}%")
print(f"Tổng thanh toán Bàn 1: {order_table1.calculate_final_bill()} VNĐ")
print(f"Tổng thanh toán Bàn 2: {order_table2.calculate_final_bill()} VNĐ")