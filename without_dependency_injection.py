class PayPalService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through PayPal.")

class PaymentProcessor:
    def __init__(self):
        self.payment_service = PayPalService()

    def pay(self, amount):
        self.payment_service.process_payment(amount)

processor = PaymentProcessor()
processor.pay(100)
