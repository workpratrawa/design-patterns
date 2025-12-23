"""
Problem 1: Logging Decorators for a Data Processor
You are given a basic DataProcessor class with a method process(data) that returns processed data.

Task:
Implement the Decorator pattern to dynamically add:
    1. Execution time logging
    2. Input/output logging
    3. Error handling

Each feature should be implemented as a separate decorator class that wraps a DataProcessor object. The decorators must be stackable in any order without modifying the original DataProcessor class.
"""
from datetime import datetime
import time
from abc import ABC, abstractmethod

class IDataProcessor(ABC):

    @abstractmethod
    def process(self, data):
        pass

class DataProcessor(IDataProcessor):

    def process(self, data):
        time.sleep(2)
        if data%2==0:
            return True, data//2
        else:
            raise Exception("data is not divisible by 2")


class ILoggingDecorator(IDataProcessor):

    @abstractmethod
    def __init__(self, data_processor):
        pass
    
    @abstractmethod
    def process(self, data):
        pass


class ExecutionTimeDecorator(ILoggingDecorator):

    def __init__(self, data_processor):
        self.data_processor = data_processor
    
    def process(self, data):
        start = time.perf_counter()
        try:
            return self.data_processor.process(data)
        finally:
            end = time.perf_counter()
            print(f"Execution Time: {end - start:.4f}s")


class IOLoggingDecorator(ILoggingDecorator):

    def __init__(self, data_processor):
        self.data_processor = data_processor
    
    def process(self, data):
        print(f"Input: {data}")
        result = self.data_processor.process(data)
        print(f"Ouput: {result}")
        return result


class ExceptionLoggingDecorator(ILoggingDecorator):

    def __init__(self, data_processor):
        self.data_processor = data_processor
    
    def process(self, data):
        try:
            result = self.data_processor.process(data)
            return result
        except Exception as e:
            print(f"Exception Occured: {e}")
            raise


## Runner Code
print("=="*5, "Normal Data Processor", "=="*5)
data_processor = DataProcessor()
print(data_processor.process(2))
try:
    print(data_processor.process(3))
except:
    pass

print("=="*5, "Execution Time Processor", "=="*5)
execution_time_processor = ExecutionTimeDecorator(data_processor)
print(execution_time_processor.process(2))
try:
    print(execution_time_processor.process(3))
except:
    pass

print("=="*5, "Exception Logging Processor", "=="*5)
exception_logging_processor = ExceptionLoggingDecorator(data_processor)
print(exception_logging_processor.process(2))
try:
    print(exception_logging_processor.process(3))
except:
    pass

print("=="*5, "IO Logging Processor", "=="*5)
io_logging_processor = IOLoggingDecorator(data_processor)
print(io_logging_processor.process(2))
try:
    print(io_logging_processor.process(3))
except:
    pass

print("=="*5, "Stacked Processor", "=="*5)
stacked_processor = ExceptionLoggingDecorator(IOLoggingDecorator(ExecutionTimeDecorator(data_processor)))
print(stacked_processor.process(2))
try:
    print(stacked_processor.process(3))
except:
    pass





    

    

