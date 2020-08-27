from tkinter import *
import requests
import json
import environ
pycrypto = Tk()
pycrypto.title("Portfolio")
pycrypto.iconbitmap("favicon.ico")
def font_color(amount):
    if amount>=0:
        return "green"
    else:
        return "red"




def my_portfolio():
    api_request =requests.get(env(API_KEY))
    api = json.loads(api_request.content)
    print("--------------------------------")
    print("--------------------------------")


    coins = [
        {
            "symbol":"BTC",
        "amount_owned": 2,
        "price_per_coin": 9200
        },
        {
        "symbol":"ETH",
        "amount_owned":100,
        "price_per_coin":242.5
        }
        ]

    total_pl = 0
    coin_row = 1

    for i in range (0,5):
        for coin in coins:
            if  api["data"][i]["symbol"] == coin["symbol"]:
                total_paid= coin["amount_owned"] * coin["price_per_coin"]
                current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
                pl_per_coin= api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_per_coin * coin["amount_owned"]
                total_pl = total_pl + total_pl_coin


                #print(api["data"][i]["name"]+" -- "+api["data"][i]["symbol"])
                #print("Current Price : $ {0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                #print("Number of Coins: ",coin["amount_owned"])
                #print("Total Amount Paid: ","${0:.2f}".format(total_paid))
                #print("Current Value: ","${0:.2f}".format(current_value))
                #print("Profit & Loss per coin: ","${0:.2f}".format(pl_per_coin))
                #print("Total Profit & Loss with coin : ","${0:.2f}".format(total_pl_coin))
                #print("--------------------------------")
                name = Label(pycrypto,text=api["data"][i]["name"],bg='light slate gray',fg="white", font="Lato 12", padx=2,pady=2,borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=0, sticky =N+S+E+W)

                price = Label(pycrypto,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),bg='light slate gray',fg="white", font="Lato 12", padx=2,pady=2,borderwidth=2,relief="groove")
                price.grid(row=coin_row, column=1, sticky =N+S+E+W)

                no_coins = Label(pycrypto,text=coin["amount_owned"],bg='light slate gray',fg="white", font="Lato 12 ", padx=2,pady=2,borderwidth=2,relief="groove")
                no_coins.grid(row=coin_row, column=2, sticky =N+S+E+W)

                amount_paid = Label(pycrypto,text="${0:.2f}".format(total_paid),bg='light slate gray',fg="white", font="Lato 12 ", padx=2,pady=2,borderwidth=2,relief="groove")
                amount_paid.grid(row=coin_row, column=3, sticky =N+S+E+W)

                current_val = Label(pycrypto,text="${0:.2f}".format(current_value),bg='light slate gray',fg="white", font="Lato 12 ", padx=2,pady=2,borderwidth=2,relief="groove")
                current_val.grid(row=coin_row, column=4, sticky =N+S+E+W)

                pl_coin = Label(pycrypto,text="${0:.2f}".format(pl_per_coin),bg='light slate gray',fg=font_color(float("{0:.2f}".format(pl_per_coin))), font="Lato 12", padx=2,pady=2,borderwidth=2,relief="groove")
                pl_coin.grid(row=coin_row, column=5, sticky =N+S+E+W)

                totalpl_coin = Label(pycrypto,text="${0:.2f}".format(total_pl_coin),bg='light slate gray',fg=font_color(float("{0:.2f}".format(total_pl_coin))), font="Lato 12", padx=2,pady=2,borderwidth=2,relief="groove")
                totalpl_coin.grid(row=coin_row, column=6, sticky =N+S+E+W)

                coin_row+=1


    totalpl = Label(pycrypto,text="${0:.2f}".format(total_pl),bg='light slate gray',fg=font_color(float("{0:.2f}".format(total_pl))), font="Lato 12", padx=2,pady=2,borderwidth=2,relief="groove")
    totalpl.grid(row=coin_row, column=6, sticky =N+S+E+W)

    api=""

    update = Button(pycrypto,text="Update",bg='DodgerBlue2',fg="white",command=my_portfolio, font="Lato 12 bold", padx=2,pady=2,borderwidth=2,relief="groove")
    update.grid(row=coin_row+1, column=6, sticky =N+S+E+W)

name = Label(pycrypto,text="Coin Name",bg='DodgerBlue2',fg="white", font="Lato 12 bold", padx=5,pady=5,borderwidth=2,relief="groove")
name.grid(row=0, column=0, sticky =N+S+E+W)

price = Label(pycrypto,text="Price",bg='DodgerBlue2',fg="white", font="Lato 12 bold", padx=5,pady=5,borderwidth=2,relief="groove")
price.grid(row=0, column=1, sticky =N+S+E+W)

no_coins = Label(pycrypto,text="No. of Coins",bg='DodgerBlue2',fg="white", font="Lato 12 bold", padx=5,pady=5,borderwidth=2,relief="groove")
no_coins.grid(row=0, column=2, sticky =N+S+E+W)

amount_paid = Label(pycrypto,text="Total Amount Paid",bg='DodgerBlue2',fg="white", font="Lato 12 bold", padx=5,pady=5,borderwidth=2,relief="groove")
amount_paid.grid(row=0, column=3, sticky =N+S+E+W)

current_val = Label(pycrypto,text="Current Value",bg='DodgerBlue2',fg="white", font="Lato 12 bold", padx=5,pady=5,borderwidth=2,relief="groove")
current_val.grid(row=0, column=4, sticky =N+S+E+W)

pl_coin = Label(pycrypto,text="P/L Per Coin",bg='DodgerBlue2',fg="white", font="Lato 12 bold", padx=5,pady=5,borderwidth=2,relief="groove")
pl_coin.grid(row=0, column=5, sticky =N+S+E+W)

totalpl = Label(pycrypto,text="Total P/L With Coin",bg='DodgerBlue2',fg="white", font="Lato 12 bold", padx=5,pady=5,borderwidth=2,relief="groove")
totalpl.grid(row=0, column=6, sticky =N+S+E+W)



my_portfolio()

pycrypto.mainloop()
