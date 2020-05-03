#Help
import tkinter as tk

LARGE_FONT = ("Verdana", 16, "bold")
MEDIUM_FONT = ("Verdana", 14)
SMALL_FONT = ("Verdana", 12)

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

PRICE = ["$", "$$", "$$$"]

class LSM_Help(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {
            "address": tk.StringVar(),
            "zipCode": tk.StringVar(),
            "state": tk.StringVar(),
            "city": tk.StringVar(),
            "distance": tk.IntVar(),
            "pricing": tk.StringVar(),
            "cuisine": tk.StringVar(),
        }
        
        container = tk.Frame(self)
        
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, SelectionPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.showFrame(StartPage)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #weighting
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)
        self.columnconfigure(4, weight = 1)
        self.columnconfigure(5, weight = 1)
        self.columnconfigure(6, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)
        self.rowconfigure(5, weight = 1)
        self.rowconfigure(6, weight = 1)

        #title/welcome label/logo
        welcomeLabel = tk.Label(self, text = "Welcome!", font = LARGE_FONT)
        welcomeLabel.grid(row = 0, column = 0, columnspan = 4, sticky = 'n')

        self.img = tk.PhotoImage(file = "help.png")
        helpLogo = tk.Label(self, image = self.img)
        helpLogo.grid(row = 1, column = 0, columnspan = 4, sticky='n')

        #instructions
        instructionsLabel = tk.Label(self, text = "To begin, please enter the address \n for which you want to search from: \n", font = MEDIUM_FONT)
        instructionsLabel.grid(row = 2, column = 0, columnspan = 4, sticky = 'n')

        #address line 1
        addressLabel = tk.Label(self, text = "Address: ", font = SMALL_FONT)
        addressLabel.grid(row = 3, column = 0, sticky = 'e' )
        address = tk.Entry(self, width = 50, font = SMALL_FONT, textvariable = controller.shared_data["address"])
        address.grid(row = 3, column = 1, columnspan = 3, sticky = 'w')

        #city
        addressLabel = tk.Label(self, text = "City: ", font = SMALL_FONT)
        addressLabel.grid(row = 4, column = 0, sticky = 'e' )
        address = tk.Entry(self, width = 25, font = SMALL_FONT, textvariable = controller.shared_data["city"])
        address.grid(row = 4, column = 1, columnspan = 3, sticky = 'w')

        #zip code
        zipLabel = tk.Label(self, text = "Zip Code: ", font = SMALL_FONT)
        zipLabel.grid(row = 5, column = 0, sticky = 'e' )
        zipCode = tk.Entry(self, width = 15, font = SMALL_FONT, textvariable = controller.shared_data["zipCode"])
        zipCode.grid(row = 5, column = 1, sticky = 'w')

        #state
        stateLabel = tk.Label(self, text = "State: ", font = SMALL_FONT)
        stateLabel.grid(row = 5, column = 2, sticky = 'e' )
        stateCode = tk.OptionMenu(self, controller.shared_data["state"], *STATES)
        stateCode.config(width = 5, font = SMALL_FONT)
        stateCode.grid(row = 5, column = 3, sticky = 'w')

        #next button
        nextB = tk.Button(self, text = "Next", command = lambda:controller.showFrame(SelectionPage), font = SMALL_FONT)
        nextB.grid(row = 6, column = 0, columnspan = 4, pady = 20, sticky = 's')
                
        
class SelectionPage(tk.Frame):
    def __init__(self, parent, controller):
        def testing():
            address = controller.shared_data["address"].get()
            city = controller.shared_data["city"].get()
            zipCode = controller.shared_data["zipCode"].get()
            state = controller.shared_data["state"].get()
            print(address+"\n" + city + zipCode + " "+state)

            distance = controller.shared_data["distance"]
            print(distance)

        def setDist(val):
            controller.shared_data["distance"] = val

        tk.Frame.__init__(self, parent)

        #weighting
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)
        self.columnconfigure(4, weight = 1)
        self.columnconfigure(5, weight = 1)
        self.columnconfigure(6, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)
        self.rowconfigure(5, weight = 1)
        self.rowconfigure(6, weight = 1)
        
        #title label
        titleLabel = tk.Label(self, text = "Restrictions:", font = LARGE_FONT)
        titleLabel.grid(row = 0, column = 0, columnspan = 5, sticky = 'n')

        #distance
        distLabel = tk.Label(self, text = "Max distance (miles): \nFor reference:  walking: 0-1, biking: 0-3, driving: 0-25mi", font = MEDIUM_FONT)
        distLabel.grid(row = 1, column = 1, columnspan = 3, sticky = 's')
        dist = tk.Scale(self, from_= 0, to = 25, length = 300, orient = tk.HORIZONTAL, font = SMALL_FONT, command = setDist)
        dist.grid(row = 2, column = 1, columnspan = 3, sticky = 'n')


        #pricing
        priceLabel = tk.Label(self, text = "Pricing: ", font = MEDIUM_FONT)
        priceLabel.grid(row = 3, column = 1, sticky = 's')

        price = tk.OptionMenu(self, controller.shared_data["pricing"], *PRICE)
        price.config(width = 5, font = SMALL_FONT)
        price.grid(row = 4, column = 1, sticky = 'n')

        #cuisine
        cuisineLabel = tk.Label(self, text = "Cuisine: (ex. Mexican, Chinese, Italian)", font = MEDIUM_FONT)
        cuisineLabel.grid(row = 3, column = 3, sticky = 's')
        cuisine = tk.Entry(self, width = 15, textvariable = controller.shared_data["cuisine"], font = SMALL_FONT)
        cuisine.grid(row = 4, column = 3, sticky = 'n')

        
        #next/back button and labels
        nextB = tk.Button(self, text = "Next", font = SMALL_FONT, command = lambda:testing())
        nextB.grid(row = 10, column = 4, sticky = 'w')

        backB = tk.Button(self, text = "Back", font = SMALL_FONT, command = lambda:controller.showFrame(StartPage))
        backB.grid(row = 10, column = 3, sticky = 'e')

app = LSM_Help()
app.title("Help")

app.mainloop()
