from address import Address
from mailing import Mailing


pochta = Mailing(Address("127000", "Moscow", "Mysnitskaya", "1", "28"),
                 Address("140013", "Lubertsy", "Cheremuhina", "4", "30"),
                 600.0, "123456789RU")

print(f"Трек-номер: {pochta.track} откуда: {pochta.from_address} куда: {pochta.to_address} стоимость {pochta.cost} рублей")
