class PayPalService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through PayPal.")

class PaymentProcessor:
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def pay(self, amount):
        self.payment_service.process_payment(amount)

# Inject dependency
payment_service = PayPalService()
processor = PaymentProcessor(payment_service)
processor.pay(100)
