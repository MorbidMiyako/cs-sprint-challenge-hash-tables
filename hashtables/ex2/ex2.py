#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    tickets_dict = {}

    for i in range(length):
        tickets_dict[tickets[i].source] = tickets[i].destination

    last_ticket = "NONE"
    route = []

    last_ticket = tickets_dict[last_ticket]
    route.append(last_ticket)

    while last_ticket != "NONE":
        last_ticket = tickets_dict[last_ticket]
        route.append(last_ticket)

    return route
