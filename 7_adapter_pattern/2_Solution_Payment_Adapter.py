from abc import ABC, abstractmethod

class IPaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class CheckoutService:
    def __init__(self, payment_processor: IPaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount: float) -> None:
        success = self.payment_processor.pay(amount)
        if success:
            print("Payment successful")
        else:
            print("Payment failed")


class LegacyBankAPI:
    def make_payment(self, cents: int) -> str:
        print(f"[LegacyBankAPI] Processing payment of {cents} cents")

        if cents <= 0:
            return "DECLINED"

        if cents > 100_000:  # arbitrary limit
            return "DECLINED"

        return "OK"


class WalletAPI:
    def send_money(self, amount: float, currency: str) -> dict:
        print(f"[WalletAPI] Sending {amount:.2f} {currency}")

        if amount <= 0:
            return {"status": "error", "reason": "invalid_amount"}

        if currency != "USD":
            return {"status": "error", "reason": "unsupported_currency"}

        if amount > 5000:
            return {"status": "error", "reason": "limit_exceeded"}

        return {"status": "success"}


class BankPaymentAdapter(IPaymentProcessor):

    def __init__(self, payment_processor: LegacyBankAPI):
        self.payment_processor = payment_processor
    
    def pay(self, amount: float) -> bool:
        cents = int(round(amount * 100))
        result = self.payment_processor.make_payment(cents)
        return result == "OK"


class WalletPaymentAdapter(IPaymentProcessor):

    def __init__(self, payment_processor: WalletAPI, currency: str = "USD"):
        self.payment_processor = payment_processor
        self.currency = currency
    
    def pay(self, amount: float) -> bool:
        result = self.payment_processor.send_money(amount, self.currency)
        return result.get("status") == "success"


bank_api = LegacyBankAPI()
bank_adapter = BankPaymentAdapter(bank_api)

wallet_api = WalletAPI()
wallet_adapter = WalletPaymentAdapter(wallet_api)

checkout1 = CheckoutService(bank_adapter)
checkout2 = CheckoutService(wallet_adapter)

checkout1.checkout(19.99)
checkout2.checkout(49.99)


