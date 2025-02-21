# def greet(name):
#     print(f'Hello {name}')
#
# names=["Jaun", "Anke"]
# for name in names:
#     greet(name)


#positional arguments
def greet_with_location(name, location):
    print(f"Hello {name}\n"
          f"How is the weather in {location}")

#keyword arguments
greet_with_location(location="Dubai", name="Jaun")
