from ctransformers import AutoModelForCausalLM
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    AutoConfig,
    pipeline,
)

class Code_Generator:
    def __init__(self,code_format=None) -> None:
        self.llm = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-7B-Instruct-GGUF", model_file="codellama-7b-instruct.q4_K_M.gguf", model_type="llama", gpu_layers=50)
        model_name = "sagard21/python-code-explainer"
        tokenizer = AutoTokenizer.from_pretrained(model_name, padding=True)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        config = AutoConfig.from_pretrained(model_name)
        model.eval()
        self.pipe = pipeline("summarization", model=model_name, config=config, tokenizer=tokenizer)
        self.code_format = code_format
        
    def generate_code(self,user_input):
        if self.code_format == "Generator":
            print(self.llm(user_input))
        else:
            print(self.pipe(user_input)[0]['summary_text'])

class Interview:
    def __init__(self,data=None,data1=None) -> None:
        self.data = data
        self.data1 = data1
        self.coding_expaliner = Code_Generator()

    def fibonacci_series(self):
        print(self.coding_expaliner.generate_code("""
        def fibonacci_series(self):
        fibonacci = [0,1]
        for i in range(2,self.data):
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
            print(f"The sum {fibonacci[i-2]}+{fibonacci[i-1]} = {fibonacci[i-1]+fibonacci[i-2]}")
            print(fibonacci) explain this code step by step"""))
        fibonacci = [0,1]
        for i in range(2,self.data):
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
            print(f"The sum {fibonacci[i-2]}+{fibonacci[i-1]} = {fibonacci[i-1]+fibonacci[i-2]}")
            print(fibonacci)
    
    def palindrom(self):
        print(self.coding_expaliner.generate_code("""
        def palindrom(self):
        
        L = 0
        R = len(self.data)-1
        while L<R:
            print(f"{self.data[L]} == {self.data[R]}")
            if self.data[L] != self.data[R]:
                return False
            L+=1
            R-=1
        return True"""))
        L = 0
        R = len(self.data)-1
        while L<R:
            print(f"Is {self.data[L]} Equal to {self.data[R]}")
            if self.data[L] != self.data[R]:
                print("False")
            L+=1
            R-=1
        return True
    

    def bubble_sort(self):
        print(self.coding_expaliner.generate_code("""
        def bubble_sort(self):
        if isinstance(self.data,str):
            self.data = list(self.data)
        for i in range(len(self.data)-1,0,-1):
            for j in range(i):
               print(f"Is {self.data[j]} is greater than {self.data[j+1]}")
               if self.data[j] > self.data[j+1]:
                   self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
        return self.data"""))
        if isinstance(self.data,str):
            self.data = list(self.data)
        for i in range(len(self.data)-1,0,-1):
            for j in range(i):
               print(f"Is {self.data[j]} is greater than {self.data[j+1]}")
               if self.data[j] > self.data[j+1]:
                   self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
        return self.data

    def insertion_sort(self):
        print(self.coding_expaliner.generate_code("""
        def insertion_sort(self):
        for i in range(1,len(self.data)):
            temp = self.data[i]
            j = i - 1
            print(f"Is {self.data[i]} greater than {self.data[j]}")
            while temp<self.data[j] and j>-1:
                self.data[j+1] = self.data[j]
                self.data[j] = temp
                j -= 1
        return self.data"""))
        for i in range(1,len(self.data)):
            temp = self.data[i]
            j = i - 1
            print(f"Is {self.data[i]} greater than {self.data[j]}")
            while temp<self.data[j] and j>-1:
                self.data[j+1] = self.data[j]
                self.data[j] = temp
                j -= 1
        return self.data

    def anagram(self):
        print(self.coding_expaliner.generate_code("""
        def anagram(self):
        data_sorted = sorted(self.data)
        data_sorted1 = sorted(self.data1)
        for i in range(len(data_sorted)):
            print(f"Is {data_sorted[i]} equal to {data_sorted1[i]}")
            if data_sorted[i] != data_sorted1[i]:
                return False
        return True"""))
        data_sorted = sorted(self.data)
        data_sorted1 = sorted(self.data1)
        for i in range(len(data_sorted)):
            print(f"Is {data_sorted[i]} equal to {data_sorted1[i]}")
            if data_sorted[i] != data_sorted1[i]:
                print("False")
        return True

    def binary_search(self):
        print(self.coding_expaliner.generate_code("""
        def binary_search(self):
        self.data.sort()
        L = 0
        R = len(self.data)
        while L<R:
            mid = (L+R)//2
            print(f"{self.data[mid]} is equal to {self.data1}")
            if self.data[mid] == self.data1:
                return self.data[mid]
            if self.data[mid]<self.data1:
                L = mid + 1
            elif self.data[mid]>self.data1:
                R = mid - 1
        return - 1"""))
        self.data.sort()
        L = 0
        R = len(self.data)
        while L<R:
            mid = (L+R)//2
            print(f"{self.data[mid]} is equal to {self.data1}")
            if self.data[mid] == self.data1:
                return self.data[mid]
            if self.data[mid]<self.data1:
                L = mid + 1
            elif self.data[mid]>self.data1:
                R = mid - 1
        return - 1
    
    def min_(self):
        print(self.coding_expaliner.generate_code("""
        def min_(self):
        min = self.data[0]
        for i in range(len(self.data)):
            print(f"min -> {min} current_value -> {self.data[i]}")
            if min>self.data[i]:
                min = self.data[i]
        return min
        """))
        min = self.data[0]
        for i in range(len(self.data)):
            print(f"min -> {min} current_value -> {self.data[i]}")
            if min>self.data[i]:
                min = self.data[i]
        return min

    def max_(self):
        print(self.coding_expaliner.generate_code("""
        def max_(self):
        max = self.data[0]
        for i in range(len(self.data)):
            print(f"Max value -> {max} current_value-> {self.data[i]}")
            if max<self.data[i]:
                max = self.data[i]
        return max"""))
        max = self.data[0]
        for i in range(len(self.data)):
            print(f"Max value -> {max} current_value-> {self.data[i]}")
            if max<self.data[i]:
                max = self.data[i]
        return max
    
    def reverse(self):
        print(self.coding_expaliner.generate_code("""
        def reverse(self):
        for i in range(len(self.data)-1,-1,-1):
            print(self.data[i])"""))
        for i in range(len(self.data)-1,-1,-1):
            print(self.data[i])
    
    def factorial(self):
        print(self.coding_expaliner.generate_code("""
        def factorial(self):
        if self.data<0:
            return "Any number which is lesser than zero has no factorial"
        if self.data == 1:
            return 1
        result = 1
        for i in range(1,self.data+1):
            print(f"{result}X{i}={result*i}")
            result*=i
        return result"""))
        if self.data<0:
            return "Any number which is lesser than zero has no factorial"
        if self.data == 1:
            return 1
        result = 1
        for i in range(1,self.data+1):
            print(f"{result}X{i}={result*i}")
            result*=i
        return result


