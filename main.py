import customtkinter

all_item = ('1rub', '10rub', '50rub', '100rub', '500rub', '1000rub', '5000rub', 'AluminiumBar', 'Aluminum', 'Amethyst',
            'AmethystBar', 'Anvil', 'Apple', 'Arrow', 'Axe', 'AxeDetailFoundry', 'Balloon', 'Banana', 'BarMaker', 'Barrel', 'Battery', 'Blueberries',
            'Bone', 'Bottle', 'Bow', 'Box', 'Brain', 'BreadBlock', 'BreadFoundry', 'Brick', 'Cabbage', 'Cable', 'Cacao','Carrot',
            'CementBall', 'Chest', 'ChickenRaw', 'ClayBall','ClayBrick', 'Clover', 'Coal', 'Coffee', 'Computer', 'Conveyor', 'Copper', 'CopperBar', 'Crusher',
            'Cucumber', 'Diamond', 'DiamondBar', 'Drill', 'DrillFoundry', 'Dropper', 'DynamiteStick', 'Egg', 'Embryo', 'Emerald', 'EmeraldBar', 'Engine',
            'Fan', 'Flint', 'Flour', 'Furnace', 'Gold','GoldBar', 'Grape', 'GravelBall', 'GunPowder', 'Hammer', 'Hoe', 'Honeycombs',
            'Hopper', 'Iron', 'IronBar', 'Kokos', 'Lead', 'LeadBar', 'Lemon', 'Lever', 'Mandarin', 'MelonSlice', 'Microchip', 'Motor', 'Nest',
            'NuclearBlock', 'Orange', 'Pan', 'Paper', 'PastaBall', 'Peppa', 'Pepper','Pickaxe', 'PickaxeDetail','PickaxeFoundry','Pin','Pipe',
            'PizzaFoundry', 'Plank','Plate','Platinum','PlatinumBar','Pot','Potato','PowerBank','PrimitiveTool','Rope','Rubber','Ruby','RubyBar',
            'Saltpeter','SandBall','Sapphire','SapphireBar','Sausage','Saw','SawBlock','Shovel','Silver','SilverBar','SnowBall','Spoon',
            'Spring','Stick','StoneBall','Strawberry','Stump','SugarPowder','SugarReed','Sulfur', 'Swor','SwordDetailFoundry','Syringe',
            'Table','Tank','Tin','TinBar','Titan ','TitanBar','TNT','Tomato','Topaz','TopazBar','Uran','Wheel','Yeasts''Zombie',
            'Wrench','Recept','Rocket','RocketEngine','Oil','Mattress','Ladder','Fire','Bundle','CaramelBar','ChocolateBar')

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("300x350")
app.minsize(300, 350)
app.maxsize(300, 350)
app.title("GUIToE")

#FUNCTION
def command():
    get_command = entry.get()
    x = entry1.get()
    y = entry2.get()

    if get_command not in all_item:
        item = customtkinter.CTkToplevel()
        item.title("ITEM NOT FOUND!")
        item.geometry("300x100")
        print("ITEM NOT FOUND")
    elif x == None or y == None:
        coor = customtkinter.CTkToplevel()
        coor.title("Please Write Coordinate!")
        coor.geometry("300x100")
        print("Please Write Coordinate!")
    elif get_command in all_item:
        scene = open("Theory of Everything_Data/StreamingAssets/Save/Scene.txt", "a")
        scene.write(f"{get_command}\n{x}\n{y}\n360")
        scene.close
    else:
        print("NE NORM")

#UI
label = customtkinter.CTkLabel(app, text="GUITOE", font=("Roboto", 25))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(app, placeholder_text="Please Write Command!", width=300)
entry.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(app, placeholder_text="Напишите вкоординату X(50)!", width=200)
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(app, placeholder_text="Напишите вкоординату Y(100)!", width=200)
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(app, text="SEND", command=command)
button.pack(pady=12, padx=10)

app.mainloop()
