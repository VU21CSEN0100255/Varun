#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Define the quadratic equation for temperature modeling
def temperature_modeling(a, b, c, time):
    # Calculate temperature based on time using the quadratic equation
    temperature = a * time**2 + b * time + c
    return temperature


# In[2]:


# Hard-coded coefficients for temperature modeling
a_hardcoded, b_hardcoded, c_hardcoded = 0.1, 2, 10

# Display results
print("Step 1: Hard-coded Variables for Weather Modeling")
time_hardcoded = 5  # Example time value
print("Temperature for hardcoded coefficients at time", time_hardcoded, "hours:", temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded, time_hardcoded))
print("\n")


# In[3]:


# Get coefficients from user input
a_keyboard = float(input("Enter coefficient a: "))
b_keyboard = float(input("Enter coefficient b: "))
c_keyboard = float(input("Enter coefficient c: "))

# Get time from user input
time_keyboard = float(input("Enter time in hours: "))

# Display results
print("Step 2: Keyboard Input for Weather Modeling")
print("Temperature for keyboard input coefficients at time", time_keyboard, "hours:", temperature_modeling(a_keyboard, b_keyboard, c_keyboard, time_keyboard))
print("\n")


# In[4]:


# Assume coefficients and time are stored in a file named 'weather.txt'
with open('weather.txt', 'r') as file:
    lines = file.readlines()
    a_file, b_file, c_file, time_file = map(float, lines[0].split())

# Display results
print("Step 3: Read from a File for Weather Modeling")
print("Temperature for file input coefficients at time", time_file, "hours:", temperature_modeling(a_file, b_file, c_file, time_file))
print("\n")


# In[ ]:




