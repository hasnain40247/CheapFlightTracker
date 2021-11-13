class FlightData:
    def __init__(self, fromDate, toDate, originAir, destAir, originCity, destCity, sprice, oprice):
        self.sprice = sprice
        self.oprice = oprice
        self.originCity = originCity
        self.destCity = destCity
        self.originAir = originAir
        self.destAir = destAir
        self.fromDate = f"{fromDate}"
        self.toDate = f"{toDate}"
