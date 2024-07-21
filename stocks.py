from datetime import datetime

ticker_symbols = {
    "GE": "General Electric",
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "NTN": "Nintendo",
    "XBX": "X-Box",
    "PS": "Playstation",
    "NK": "Nokia",
    "TE": "Tiger Electronics"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 ),
    ( 'EK', 50, '1-jun-1990', 30),
    ( 'NTN', 200, '1-jun-1998', 15),
    ( 'EK', 50, '1-jun-1990', 560),
    ( 'XBX', 250, '11-nov-2001', 500),
    ( 'PS', 100, '1-jan-1998', 200),
    ( 'TE', 100, '27-jun-1992', 300),
    ( 'NK', 200, '27-jun-2002', 600), 
    ( 'XBX', 500, '11-nov-2007', 10),
    ( 'TE', 500, '27-jun-1992', 10),
    ( 'NK', 200, '27-jun-2002', 10), 

]

def generate_report(ticker_symbols, purchases):
    report = "List of all purchases\n---------------------\n"
    for purchase in purchases:
        symbol, shares, date_str, price = purchase
        full_name = ticker_symbols.get(symbol, "Unknown Company")
        full_price = shares * price
        date = datetime.strptime(date_str, '%d-%b-%Y').strftime('%d-%m-%Y')
        report += f"{full_name} stock purchased for ${full_price} on {date}\n"
    return report

print(generate_report(ticker_symbols, purchases))