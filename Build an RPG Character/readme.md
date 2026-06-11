# Character Creator

## Description

This Python program creates a game character with three stats:

* **STR** (Strength)
* **INT** (Intelligence)
* **CHA** (Charisma)

The program validates the character data and displays the stats using filled (`●`) and empty (`○`) circles.

Example output:

```text
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

---

## Rules

### Character Name

* Must be a string.
* Cannot be empty.
* Cannot contain spaces.
* Must be 10 characters or less.

### Character Stats

* All stats must be integers.
* Each stat must be between 1 and 4.
* The total points must equal 7.

Example valid character:

```python
create_character("ren", 4, 2, 1)
```

Total points:

```text
4 + 2 + 1 = 7
```

---

## How to Run

### 1. Save the code

Create a file called:

```text
character.py
```

Paste the code into the file and save it.

### 2. Open a terminal

Navigate to the folder containing the file:

```bash
cd path/to/your/project
```

Example:

```bash
cd Desktop/python_projects
```

### 3. Run the program

```bash
python character.py
```

or

```bash
python3 character.py
```

### 4. Expected Output

```text
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

---

## Example Usage

```python
print(create_character("alex", 3, 2, 2))
```

Output:

```text
alex
STR ●●●○○○○○○○
INT ●●○○○○○○○○
CHA ●●○○○○○○○○
```

---

## Error Examples

Invalid name:

```python
create_character("", 4, 2, 1)
```

Output:

```text
The character should have a name
```

Too many points:

```python
create_character("ren", 4, 4, 4)
```

Output:

```text
The character should start with 7 points
```
