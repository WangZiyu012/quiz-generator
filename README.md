# object oriented programming

waiter example

what he has --- attributes: holding a plate, which table being responsible, ...

what he does --- methods: take order, take payment, ...

In OOP, we try to model real world objects, which has things and can also do things as said above. Objects are just a way to combine some piece of data and some piece of data and functionality.

When we do so, we figure out what a thing can do and it has.

And we can also generate different version of a same thing we created, just like different waiters. In classical term, we call this a class or blueprint or type:

```angular2html

item = Blueprint()
item.attribute_1
item.method_1()

```

# Python package

differs from a module, package is a whole bunch of code that other people has written. search PyPI

# Python class

```angular2html
class User: # name a class should be capitalized
    pass # use pass to let python not report error from the time being

user_1 = User()

```

```angular2html
class User: 
    def __init__(self, para_1, para_2):#add para can be passed in when object get constructed

    #a special function, constructor or initialization. initialize different attributes of the class. specify starting pieces of the class. things in this initialization function will happen once the new class has been created.

    self.attribute_1 = para_1 # auto-done when initialized with para_1 input

user_1 = User()

```

# methods in the class

```angular2html

class User:

    def __init__(self):
        self.id = id
        self.name = name
        self.followers = 0

    def follow(self):
    # unlike function, method in the class always need to have a "self" as first parameter, meaning when this method being called, it knows the object that called it.

```
```angular2html
class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.follower = 0
        self.following = 0
        # self keyword becomes quite important when working with classes and objects. it's a way for us to refer to the object that's going to be created from the class inside the class blueprint. never see self when outside the class, but always seen inside the class.
    def follow(self, user):
        user.follwers += 1
        self.following += 1
```