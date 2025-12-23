
## Problem: Adapter Pattern for Payment Processing Systems

### Context

You are building a **payment processing module** for an e-commerce platform.
Your system was originally designed to work with a **standard payment interface**:

```python
class IPaymentProcessor:
    def pay(self, amount: float) -> bool:
        ...
```

Your codebase already depends on this interface in multiple places.

---

### Existing Code (DO NOT MODIFY)

```python
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
```

---

### Third-Party Libraries (You CANNOT change these)

#### 1️⃣ Legacy Bank API

```python
class LegacyBankAPI:
    def make_payment(self, cents: int) -> str:
        # returns "OK" or "DECLINED"
        ...
```

#### 2️⃣ Modern Wallet API

```python
class WalletAPI:
    def send_money(self, amount: float, currency: str) -> dict:
        # returns {"status": "success"} or {"status": "error"}
        ...
```

---

### Task

Implement the **Adapter pattern** to make **both third-party payment systems** work with your existing `CheckoutService`, **without modifying**:

* `CheckoutService`
* `IPaymentProcessor`
* Any third-party APIs

---

### Requirements

1. Create a **separate adapter class** for each third-party API
2. Each adapter must implement `IPaymentProcessor`
3. Adapters must:

   * Translate method names
   * Convert data formats (e.g., dollars → cents)
   * Normalize return values to `bool`
4. Client code (`CheckoutService`) must remain unaware of:

   * Legacy APIs
   * Wallet APIs
   * Data conversions

---

### Expected Usage

```python
bank_api = LegacyBankAPI()
bank_adapter = BankPaymentAdapter(bank_api)

wallet_api = WalletAPI()
wallet_adapter = WalletPaymentAdapter(wallet_api)

checkout1 = CheckoutService(bank_adapter)
checkout2 = CheckoutService(wallet_adapter)

checkout1.checkout(19.99)
checkout2.checkout(49.99)
```

---

## What This Question Tests (Important)

This problem evaluates whether you understand:

✔ Structural mismatch (method names, data types, return values)
✔ Why adapters exist (integration without modification)
✔ Interface preservation
✔ Object composition vs inheritance
✔ One adapter per adaptee

This is **not** a trivial wrapper problem—it mirrors real production code.

---

## Optional Stretch Challenges (for mastery)

If you want to push further after solving:

1. Add **currency support** without changing `CheckoutService`
2. Add **retry logic** *inside* adapters only
3. Create a **class adapter** variant (inheritance-based)
4. Show why Decorator is *wrong* here and Adapter is *right*

---

When you’re ready:
👉 **Paste your solution**, and I’ll review it exactly like before—line by line, with design feedback and pattern correctness analysis.
