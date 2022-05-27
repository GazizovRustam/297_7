def main():
    ticketA = int(input('Please enter tickets sold category A: '))
    ticketB = int(input('Please enter tickets sold category B: '))
    ticketC = int(input('Please enter tickets sold category C: '))

    priceA = 20
    priceB = 15
    priceC = 10

    valueA = getTicket(ticketA, priceA)
    valueB = getTicket(ticketB, priceB)
    valueC = getTicket(ticketC, priceC)
    totalSum = getTotalSum(valueA, valueB, valueC)
    print('$', totalSum)


def getTicket(ticket, price):
    return ticket * price

def getTotalSum(value1, value2, value3):
    return value1 + value2 + value3


main()