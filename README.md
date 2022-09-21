# Deli Counter Lab

## Learning Goals

- Practice building functions that use iteration and controlling their return
  values
- Practice manipulating lists (adding elements, removing elements, etc.)

***

## Key Vocab

- **Interpreter**: a program that executes other programs. Python programs
require the Python interpreter to be installed on your computer so that they
can be run.
- **Python Shell**: an interactive interpreter that can be accessed from the
command line.
- **Data Type**: a specific kind of data. The Python interpreter uses these
types to determine which actions can be performed on different data items.
- **Exception**: a type of error that can be predicted and handled without
causing a program to crash.
- **Code Block**: a collection of code that is interpreted together. Python
groups code blocks by indentation level.
- **Function**: a named code block that performs a sequence of actions when it
is called.
- **Scope**: the area in your program where a specific variable can be called.

***

## Instructions

To get started, run `pipenv install` to create your virtual environment and
`pipenv shell` to enter the virtual environment. Then run `pytest -x` to run
your tests. Use these instructions and `pytest`'s error messages to complete
your work in the `lib/` folder.

The local deli is putting in a new computerized queue to keep track of their
customers and improve productivity. At the beginning of the day, the deli is
empty so the queue should be represented by an empty list:

```py
katz_deli = []
```

Write all of your code in `lib/deli_counter.py`

### `line()`

Build the `line()` function that shows everyone their current place in the line.
If there is nobody in line, it should say `"The line is currently empty."`.

### `take_a_number()`

Build a function that a new customer will use when entering the deli. The
`take_a_number()` function should accept two arguments, the list for the current
line of people (`katz_deli`), and a string containing the name of the person
joining the end of the line. The function should call out (i.e., `print`) the
person's name along with their position in line.

**Top-Tip:** Remember that people like to count from 1, not from 0 like
computers.

### `now_serving()`

Build the `now_serving()` function which should call out (`print`) the next
person in line and then remove them from the front. If there is nobody in line,
it should call out (`print`) that `"There is nobody waiting to be served!"`.

Example usage:

```py
katz_deli = []

take_a_number(katz_deli, "Ada") #=> Welcome, Ada. You are number 1 in line.
take_a_number(katz_deli, "Grace") #=> Welcome, Grace. You are number 2 in line.
take_a_number(katz_deli, "Kent") #=> Welcome, Kent. You are number 3 in line.

line(katz_deli) #=> "The line is currently: 1. Ada 2. Grace 3. Kent"

now_serving(katz_deli) #=> "Currently serving Ada."

line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent"

take_a_number(katz_deli, "Matz") #=> Welcome, Matz. You are number 3 in line.

line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent 3. Matz"

now_serving(katz_deli) #=> "Currently serving Grace."

line(katz_deli) #=> "The line is currently: 1. Kent 2. Matz"
```

**Hint:** Review how to [add][add-to-list] and [remove][remove-from-list] list
elements as well as how to [iterate with index numbers][iterate-with-index].

***

## Resources

- [W3Schools: Add List Items][add-to-list]
- [W3Schools: Remove a List Item][remove-from-list]
- [How to Iterate a Python List With Index][iterate-with-index]

[add-to-list]: https://www.w3schools.com/python/python_lists_add.asp
[remove-from-list]: https://www.w3schools.com/python/gloss_python_remove_list_items.asp
[iterate-with-index]: https://www.techieheap.com/how-to-iterate-a-python-list-with-index/
