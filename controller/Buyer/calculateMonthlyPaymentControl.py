class CalculateMonthlyPaymentControl:
    def __init__(self):
        pass


    # 39 As a buyer, I want to be able to calculate the monthly payments based on the price of the property, interest rate, and other relevant factors so that I can know if the property is within my budget.
    def calculateMonthlyPayment(self,house_price, interest_rate, loan_years, down_payment_rate):
        try:
            house_price = float(house_price)
            interest_rate = float(interest_rate)
            loan_years = int(loan_years)
            down_payment_rate = float(down_payment_rate)
        except Exception:
            return False
        if loan_years < 1 or down_payment_rate > 1 or interest_rate < 0:
            return False
        # 计算首付金额
        down_payment = house_price * down_payment_rate
        # 计算贷款金额
        loan_amount = house_price - down_payment
        # 将年利率转换为月利率
        monthly_interest_rate = interest_rate / 12
        # 将贷款年数转换为总还款月数
        total_payments = loan_years * 12
        # 使用等额本息法计算每月还款金额
        monthly_payment = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments \
                          / ((1 + monthly_interest_rate) ** total_payments - 1)
        return int(monthly_payment)


# 示例用法
# house_price = 1000000
# interest_rate = 0.03
# loan_years = 5
# down_payment_rate = 0.25
# print(CalculateMonthlyPaymentControl().calculateMonthlyPayment(house_price, interest_rate, loan_years,down_payment_rate))

