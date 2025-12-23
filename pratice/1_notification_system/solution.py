import time
from abc import ABC, abstractmethod

class INotifier(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass


# Client Code
class NotificationService:
    def __init__(self, notifier: INotifier):
        self.notifier = notifier

    def notify(self, recipient: str, message: str) -> None:
        success = self.notifier.send(recipient, message)
        if success:
            print("Notification sent")
        else:
            print("Notification failed")


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


"""
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
"""

# Adapters
class EmailNotifierAdapter(INotifier):
    def __init__(self,notifier:LegacyEmailSDK):
        self.notifier = notifier
    
    def send(self, recipient: str, message: str):
        status = self.notifier.send_email(recipient, message)
        if status != 200:
            return False
        return True


class SmsNotifierAdapter(INotifier):
    def __init__(self,notifier:SmsGatewaySDK):
        self.notifier = notifier
    
    def send(self, recipient: str, message: str):
        status = self.notifier.transmit(recipient, message)
        return status.get("ok", False)

# Decorators
# class INotifierDecorator(INotifier):

#     def __init__(self, notifier:INotifier):
#         self.notifier = notifier
    
#     @abstractmethod
#     def send(self, recipient: str, message: str) -> bool:
#         pass

# Better to remove redundancies
class NotifierDecorator(INotifier):
    def __init__(self, notifier: INotifier):
        self.notifier = notifier


class LoggingDecorator(INotifierDecorator):
    
    def send(self, recipient: str, message: str) -> bool:
        print("Recipient:", recipient)
        print("Message:", message)
        return self.notifier.send(recipient, message)


class RetryDecorator(NotifierDecorator):
    def __init__(self, notifier: INotifier, retry_count: int = 5):
        super().__init__(notifier)
        self.retry_count = retry_count

    def send(self, recipient: str, message: str) -> bool:
        for _ in range(self.retry_count):
            if self.notifier.send(recipient, message):
                return True
        return False


class ExecutionTimeDecorator(INotifierDecorator):
    
    def send(self, recipient: str, message: str) -> bool:
        start = time.perf_counter()
        try:
            return self.notifier.send(recipient, message)
        finally:
            end = time.perf_counter()
            print(f"Execution Time: {end - start:.4f}s")
