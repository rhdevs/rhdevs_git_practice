from basic_relarg import *

# query example: "P([ca,cb], S(pizza==piz /\ ca<cb, (R(l(ca, pizza), likes) * R(li(cb, piz), likes))))"
query = ""

print_table(complete(query, db))