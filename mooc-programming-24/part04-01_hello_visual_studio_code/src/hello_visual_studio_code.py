# Write your solution here
while True:
    editor = input("Editor: ")
    if "visual studio code" == editor.lower():
        print("an excellent choice!")
        break
    elif "word" == editor.lower() or "notepad" == editor.lower():
        print("awful")
    else:
        print("not good")          