# Pep 8 conventions

## Bracket types
    round brackets, open brackets or parentheses: ( )
    square brackets, closed brackets or box brackets: [ ]
    curly brackets, squiggly brackets, swirly brackets, braces, or chicken lips: { }
    angle brackets, diamond brackets, cone brackets or chevrons: < > or ⟨ ⟩

## Rules:
- Any line can't exceed 80 characters

- Use four spaces for indentation

- Always use single quotes or double quotes and be consistent

- Use snake_case for variable names

- Use capital letters for CONSTANT variables, place it below any import statements

- For module use single word or seperate them with underscores

- Class should be in PascalCase

    ```python
    class TestClass(): 
        pass
    ```
- Functions should be in snake_case

    ```python
    def hello_world():
        pass
    ```
- Exceptin should follow class conventions as it is considered a class

- The first parameter in a method should be self
    ```python
    class Test:
        def test(self):
            pass
    ```

- For class method first parameter should be cls
    ```python
    @classmethod
    def cls_method(cls):
        pass
    ```

- Top level functions or classes should be seperated by two blank lines

- Methods inside class should be seperated by one lines

- Import should be on top of file and should not import two or more modules on same line

- Shouldn't do wild card import 
    ```python
    from module import *  # Don't do this
    ```
- Docstrings should be always wirtten with double quotation marks
    ```python
    """ This is a docstring """
    ```
- There shouldnt be white spaces after or before parentheses and between parentheses and commas

- Variables and operators should be used with spaces but it case of precedance spaces shouldn't be used
    ```python
    i = i + 1
    z = (x+Y) * (A+B)
    z = x*y + a*b
    i += 1
    ```

- For default values there shouldn't any spaces
    ```python
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)
    ```

- Inline comments should be two spaces right to the code and the comment should start with capital letter one space right to the # symbol
    ```python
    color = (0, 0, 0)  # This is correct
    ```

- For None checking use is dont == is:
    ```python
    x = None
    
    if x is None:
        pass
    ```
- For checking if some variable is not some value use:
    ```python 
    # Correct
    if foo is not "X":
        pass

    # Wrong
    if not (foo is "X"):
        pass
    ```

- Always accept a specific exception don't use empty except block
    ```python
    # Correct
    try:
        import module
    except ImportError:
        pass

    # Wrong
    try:
        import module
    except:
        pass
    ```

- Don's use slice to check if string starts or ends with some word or characters
    ```python
    # Correct
    if foo.startswith("bar"):
        pass

    # Wrong
    if foo[:3] == "bar":
        pass
    ```