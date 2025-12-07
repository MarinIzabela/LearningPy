
colors = (
    ("Red", (255,0,0)),
    ("Green",(0,255,0)),
    ("Blue",(0,0,255)),
    ("Yellow",(255,255,0)),
    ("Cyan",(0,255,255)),
    ("Magenta",(255,0,255)),
    ("White", (255,255,255)),
    ("Black", (0,0,0))
)

print("Available colors : ")

for color in colors:
    print(color[0])

choice = input("\n Enter a color to get its RGB color: ").strip().title()

for name,rgb in colors:
    if name == choice:
        print(f"RGB color of {name} is {rgb}")
        break
else:
    print("Color not found")