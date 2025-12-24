# Implement Stackable Proxy Objects (Python)

## Overview

You are building a **Document Management System**.

A document:

* Is expensive to load
* May require access control
* May require logging

Instead of placing all logic in one class, you will implement **Proxy objects** that control access to a document.

Each proxy must follow a common interface and delegate work correctly.

---

## Given Code (Do Not Modify)

### Document Interface

```python
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def read(self) -> str:
        pass
```

---

### Real Document

This represents a document stored on a remote server.
Creating it is intentionally slow.

```python
import time

class RealDocument(Document):
    def __init__(self, document_name: str, content: str):
        self.document_name = document_name
        time.sleep(1)  # Simulate expensive loading
        self.content = content

    def read(self) -> str:
        return self.content
```

---

## Your Task

You must implement **three proxy classes**.
Each proxy must implement `Document`.

Some proxies **wrap another `Document`**, while others **create the real document lazily**.

---

## 1. Virtual Proxy (Lazy Loading)

### Class Name

`VirtualDocumentProxy`

### Purpose

Delay creation of `RealDocument` until it is actually needed.

### Requirements

* Implements `Document`
* Does NOT wrap another `Document`
* Must NOT create `RealDocument` in the constructor
* Must create `RealDocument` only when `read()` is called
* Must create the real document only once

### Constructor

```python
VirtualDocumentProxy(document_name: str, content: str)
```

📌 **Note:**
This proxy must be used as the **innermost object** in any proxy chain.

---

## 2. Protection Proxy (Access Control)

### Class Name

`SecureDocumentProxy`

### Purpose

Restrict access based on user role.

### Requirements

* Implements `Document`
* Wraps another `Document`
* If `user_role == "ADMIN"`, allow access
* Otherwise, immediately return:

  ```
  "ACCESS DENIED"
  ```
* Must NOT trigger document loading or logging when access is denied

### Constructor

```python
SecureDocumentProxy(document: Document, user_role: str)
```

---

## 3. Logging Proxy (Monitoring)

### Class Name

`LoggingDocumentProxy`

### Purpose

Log document access.

### Requirements

* Implements `Document`
* Wraps another `Document`
* Logs access **only when the document is actually read**
* Must NOT log if access is denied

Log format:

```
Document accessed at <ISO timestamp>
```

### Constructor

```python
LoggingDocumentProxy(document: Document)
```

---

## Valid Proxy Composition Rules (Important)

* `VirtualDocumentProxy` **must be the innermost object**
* `SecureDocumentProxy` and `LoggingDocumentProxy` must be stackable **around it in any order**

### ✅ Valid Examples

```python
LoggingDocumentProxy(
    SecureDocumentProxy(
        VirtualDocumentProxy("file.txt", "Hello"),
        "ADMIN"
    )
)

SecureDocumentProxy(
    LoggingDocumentProxy(
        VirtualDocumentProxy("file.txt", "Hello")
    ),
    "ADMIN"
)
```

### ❌ Invalid Example (Do Not Support)

```python
VirtualDocumentProxy(
    LoggingDocumentProxy(...),
    ...
)
```

---

## Example: Allowed Access

```python
doc = SecureDocumentProxy(
    LoggingDocumentProxy(
        VirtualDocumentProxy("secret.txt", "Top Secret Data")
    ),
    "ADMIN"
)

print(doc.read())
```

### Output

```
Document accessed at 2025-01-01T10:00:00
Top Secret Data
```

---

## Example: Access Denied

```python
doc = LoggingDocumentProxy(
    SecureDocumentProxy(
        VirtualDocumentProxy("secret.txt", "Top Secret Data"),
        "GUEST"
    )
)

print(doc.read())
```

### Output

```
ACCESS DENIED
```

* No delay
* No logging
* No document creation

---

## Rules

* Do NOT modify `Document` or `RealDocument`
* Each proxy must have **one clear responsibility**
* Proxies must delegate correctly
* No side effects should occur when access is denied

