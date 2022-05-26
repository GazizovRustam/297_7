def main():
    ticketA = int(input('Please enter tickets sold category A: '))
    value = getTicketA(ticketA)
    print('$', value)


def getTicketA(ticketA):
    return ticketA * 20


main()