from address import Address
from mailing import Mailing

to_address = Address("443011", "Самара", "Советская", "221", "402")
from_address = Address("452015", "Уфа", "Салавата Юлаева", "88", "20")

mailing = Mailing(to_address, from_address, 1350, "14083866047665")

print(mailing)
