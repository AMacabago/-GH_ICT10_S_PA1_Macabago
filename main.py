from pyscript import display, document

def check(event=None): 
    fahrenheit = float(document.getElementById("fahrenheit").value)
    celsius = (fahrenheit - 32) * 5 / 9

    if celsius >= 37.8:
        result = "Fever."
    else:
        result = "Normal."

    document.getElementById("output").innerHTML = (
        f"Temperature in Celsius: {celsius:.2f}°C | {result}"
    )