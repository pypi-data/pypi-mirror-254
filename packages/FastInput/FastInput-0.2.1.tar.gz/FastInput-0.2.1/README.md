**A Python library to simplify the input from user**

This library is a wrapper arround the input method. It allows to very the input according to the selected type, lower or upper bound provided.

*Instalation*

```
pip install FastInput
```

*Usage*
Asking for an integer value between 0 and 4:
```python
import FastInput as fi

yourChoice = fi.input_with_validation("Provide your id", InputType.INTEGER,False,0,4))
```
Asking for a string:
```python
import FastInput as fi

yourChoice = fi.input_with_validation("What is your name", InputType.STRING,False))
```
Asking for a user validation:
```python
import FastInput as fi

yourChoice = fi.input_for_confirmation("Do you agree?[Y/n]", True))
```
