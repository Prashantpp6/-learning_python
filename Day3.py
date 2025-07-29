import pandas as pd 

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, None, 30],
    'salary': [55000, 48000, 51000],
    'gender': ['Female', 'Male', 'Female'],
    'email': ['alice@gmail.com', 'bob_at_email.com', 'charlie@gmail.com']
}

df = pd.DataFrame(data)


if 'age' in df.columns:
    print("age is exits in data set")