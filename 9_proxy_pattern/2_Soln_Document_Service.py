from abc import ABC, abstractmethod
import time
from datetime import datetime

class Document(ABC):
    @abstractmethod
    def read(self) -> str:
        pass


class RealDocument(Document):
    def __init__(self, document_name: str, content: str):
        self.document_name = document_name
        time.sleep(1)  # Simulate expensive loading
        self.content = content

    def read(self) -> str:
        return self.content


class VirtualDocumentProxy(Document):
    def __init__(self, document_name: str, content: str):
        self.document_name = document_name
        self.content = content
        self.document = None
    
    def read(self):
        if not self.document:
            self.document = RealDocument(self.document_name, self.content)
        return self.document.read()


class SecureDocumentProxy(Document):
    def __init__(self,document:Document, user_role:str):
        self.document = document
        self.user_role = user_role
    
    def read(self):
        if self.user_role != "ADMIN":
            return "ACCESS DENIED"
        return self.document.read()


class LoggingDocumentProxy(Document):
    def __init__(self,document:Document):
        self.document = document
    
    def read(self):
        try:
            content = self.document.read()
            if content != "ACCESS DENIED":
                print(f"Document accessed at {datetime.now()}")
            return content
        except Exception as e:
            raise
            
