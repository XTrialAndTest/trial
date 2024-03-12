from oscar.apps.catalogue.categories import create_from_breadcrumbs

categories = (
"Home>Home Decor>Curtains & Draperies",
"Home>Home Decor>Area Carpets>Rug Pads",
"Home>Home Decor>Area Carpets>Rugs&Carpet>Rags",
"Home>Home Decor>Area Carpets>Rugs&Carpet>Carpets",
"Home>Bedding>Mattresses",
"Home>Bedding>Bed Pillows & Positioners>Bed Pillows",
"Home>Bedding>Bedding Accessories",
"Home>Bedding>Comforters & Sets",
"Home>Bedding>Duvets, Covers & Sets",
"Home>Bedding>Kids' Bedding",
"Home>Bedding>Mattress Pads & Protectors",
"Home>Bedding>Mattress Toppers",
"Home>Bedding>Nursery Bedding",
"Home>Bedding>Sheets & Pillowcases",
"Home>Bedding>Mosquito Net",

)
for breadcrumbs in categories:
    create_from_breadcrumbs(breadcrumbs)


print('this has worked')