class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def moarefi(self):
        return (f"Esme man {self.name} ast va {self.age} sale hastam")
        
class Programmer(Person):
    def __init__(self, p_language, p_level, name, age):
        super().__init__(name, age)
        self.p_language = p_language
        self.p_level = p_level
    
    def moarefi(self):
        return (f"man {self.name} hastam va {self.age} sale hastam va ba zaban {self.p_language} kar mikonam va dar sathe {self.p_level} hastam.")

class Manager(Person):
    def __init__(self, name, age, m_level):
        super().__init__(name, age)
        self.m_level = m_level
        
    def moarefi(self):
        return (f"Man {self.name} hastam va {self.age} sale hastam va sathe modiriati ye man {self.m_level} ast")

class Tech_manager(Manager, Programmer):
    def __init__(self, name, age, m_level, p_level, p_language):
        Manager.__init__(self, name, age, m_level)
        Programmer.__init__(self, name, age, p_level, p_language)
        
    def moarefi(self):
        return (f"Man {self.name} hastam va {self.age} sale hastam va dar barname nevisi dar sathe {self.p_level} hastam va ba zaban {self.p_language} hastam va dar modiriat dar sathe {self.m_level} hastam")
