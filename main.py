from utils import Parsing
from utils import Dom

url = "https://www.booking.com/hotel/ma/campanile-casablanca-centre-ville.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaIwBiAEBmAEJuAEXyAEM2AEB6AEB-AELiAIBqAIDuAK-rPGKBsACAdICJDc2OTFjZmNhLTA4NjktNGYwOS1hMGIxLWM3YjFkM2JlOTIzMdgCBuACAQ;sid=308495cd2b88ce9f23273eea7f4530b2;dest_id=-28159;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=3;hpos=3;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1633441378;srpvid=53ad6071ae92010d;type=total;ucfs=1&#hotelTmpl"


Booking_Dom = Dom(url)
ParseBooking = Parsing(Booking_Dom.GetDom())
Header_Elements = ParseBooking.GetHeaderData()
Header_text = []

for element in Header_Elements:
    elem_text = element.get_text().strip()
    Header_text.append(elem_text)

print(Header_text)
