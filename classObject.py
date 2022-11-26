                                                                                    #class and object

#Manual Attributes
class Student :
    #attributes
    Name = '';
    Age = int;

    #function
    def introduce(self) :
        print('my name is :', self.Name);


#objects

#student01
Student01 = Student()
Student01.Name = 'ali';
Student01.Age = 23;
Student01.introduce();





#Automated Attributes
class Staff :
    #attributes
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    #function
    def introduction(self) :
        print('hello my name is :', self.name, 'I am ',self.age,' years old');

#objects

#Staff01
Staff01 = Staff('Ali',22);
Staff01.introduction();


