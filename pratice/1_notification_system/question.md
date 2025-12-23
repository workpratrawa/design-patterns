# Problem: Notification System Using Adapter and Decorator Patterns

## Context

You are building a **notification system** for an application.
The application code is already written to depend on a single interface:

```python
class INotifier:
    def send(self, recipient: str, message: str) -> bool:
        ...
```

Your job is to integrate **multiple third-party notification providers** and add **cross-cutting features** such as logging, retries, and execution-time measurement — **without modifying existing client code or third-party SDKs**.

---

## Constraints (Very Important)

You **MUST NOT modify**:

* Client code
* The `INotifier` interface
* Any third-party SDKs

You **MUST**:

* Support multiple notification providers
* Allow features like logging and retries to be added dynamically
* Keep providers swappable at runtime
* Allow features to be stacked in **any order**

---

## Existing Client Code (DO NOT MODIFY)

```python
class NotificationService:
    def __init__(self, notifier: INotifier):
        self.notifier = notifier

    def notify(self, recipient: str, message: str) -> None:
        success = self.notifier.send(recipient, message)
        if success:
            print("Notification sent")
        else:
            print("Notification failed")
```

---

## Internal Interface (DO NOT MODIFY)

```python
from abc import ABC, abstractmethod

class INotifier(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass
```

---

## Third-Party SDKs (Mocks — DO NOT MODIFY)

### 1️⃣ Legacy Email SDK (Old system)

**Characteristics**

* Different method name
* Returns numeric status codes
* No booleans
* No exceptions

```python
class LegacyEmailSDK:
    def send_email(self, address: str, body: str) -> int:
        print(f"[LegacyEmailSDK] Sending email to {address}")

        if not address or "@" not in address:
            return 400  # Bad request

        if len(body) == 0:
            return 400

        if "fail" in body.lower():
            return 500  # Server error

        return 200  # Success
```

---

### 2️⃣ SMS Gateway SDK (Modern but incompatible)

**Characteristics**

* Different method name
* Returns dictionary responses
* Explicit success flag
* Error metadata

```python
class SmsGatewaySDK:
    def transmit(self, phone_number: str, text: str) -> dict:
        print(f"[SmsGatewaySDK] Sending SMS to {phone_number}")

        if not phone_number.startswith("+"):
            return {"ok": False, "error": "invalid_phone_number"}

        if len(text) == 0:
            return {"ok": False, "error": "empty_message"}

        if "fail" in text.lower():
            return {"ok": False, "error": "gateway_failure"}

        return {"ok": True}
```

---

## Your Tasks

---

## Part 1 — Adapter Pattern (Structural Compatibility)

Create **one adapter per SDK**:

* `EmailNotifierAdapter`
* `SmsNotifierAdapter`

Each adapter must:

1. Implement `INotifier`
2. Wrap the corresponding SDK
3. Translate:

   * Method names
   * Parameter semantics
   * Return values → `bool`
4. Hide all SDK-specific details from the client

📌 **The client must not know which SDK is being used.**

---

## Part 2 — Decorator Pattern (Cross-Cutting Behavior)

Implement the following decorators, each implementing `INotifier`:

### 1️⃣ LoggingDecorator

* Logs recipient and message before sending

### 2️⃣ RetryDecorator

* Retries sending up to `N` times on failure

### 3️⃣ ExecutionTimeDecorator

* Measures and logs how long sending takes

Decorators must:

* Wrap **any** `INotifier`
* Be stackable in **any order**
* Preserve method signature and return value
* Not modify adapters or SDKs

---

## Required Usage Example

```python
email_sdk = LegacyEmailSDK()
email_adapter = EmailNotifierAdapter(email_sdk)

notifier = ExecutionTimeDecorator(
    RetryDecorator(
        LoggingDecorator(email_adapter),
        retries=3
    )
)

service = NotificationService(notifier)
service.notify("user@example.com", "Welcome!")
```

---

## What This Problem Is Testing

| Concern                    | Pattern   | Why                |
| -------------------------- | --------- | ------------------ |
| SDK incompatibility        | Adapter   | Interface mismatch |
| Logging / retries / timing | Decorator | Behavior extension |
| Runtime composition        | Decorator | Stackability       |
| SDK isolation              | Adapter   | Encapsulation      |

🚫 **Decorator alone is insufficient**
🚫 **Adapter alone is insufficient**

Both patterns are required for a clean design.

---

## Evaluation Criteria

Your solution will be evaluated on:

✔ Correct pattern usage
✔ No modification of forbidden code
✔ Proper responsibility separation
✔ Stackable decorators
✔ Clean adapters with no leakage
✔ Correct retry and error semantics

---

## Optional Stretch Goals (Advanced)

* Add a **MetricsDecorator**
* Add **currency / locale handling** inside adapters
* Combine adapters behind a **factory**
* Show a **bad solution** and explain why it violates patterns

---

If you want:
👉 Next, you can **implement it yourself** and paste the solution
👉 Or I can provide a **reference implementation** step by step

Just tell me how you want to proceed.
