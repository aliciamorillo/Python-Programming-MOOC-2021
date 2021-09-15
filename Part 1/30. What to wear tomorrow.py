#Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing
# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

print("What is the weather forecast for tomorrow?")

temperature = int(input("Temperature:"))
rain = input("Will it rain (yes/no):")

if temperature > 20:
    print("Wear jeans and a T-shirt")

if temperature <= 20 and temperature > 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")

if temperature <= 10 and temperature > 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")

if temperature <= 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if rain == "yes":
    print("Don't forget your umbrella!")