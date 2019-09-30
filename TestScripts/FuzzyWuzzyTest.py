
from fuzzywuzzy import fuzz, process
arr1 = ["type", "extarctdate", "extarctrime", "storeno", "transactionno", "recordtype", "linenumber", "itemnumber", "itemdesc", "catalogueno", "uomcode", "uomdesc", "packsize", "orderqnty", "costpriceuom", "ordertype", "referenceno", "transactionqty", "reasoncode", "invoiceqty", "invoicecostuom", "taxoncost", "sellingpriceuom", "location", "signtype", "country", "source", "dt", "country", "source", "dt"]
arr2 = ["packsize", "transactionqty", "storeno", "taxoncost"]

# Word Matching Test
ratio = fuzz.partial_token_sort_ratio(arr1, arr2)
print(ratio)
# ratio = fuzz.token_sort_ratio("statusOrder", "order_status")
# print(ratio)
# ratio = fuzz.token_sort_ratio("product_code", "partner_product_code")
# print(ratio)
# ratio = fuzz.token_sort_ratio("loc_type", "location_type")
# print(ratio)
# ratio = fuzz.token_sort_ratio("order_quantity", "ordered_volume")
# print(ratio)
# ratio = fuzz.token_sort_ratio("vandeparturetimefromstore", "van_departure_time_from_store")
# print(ratio)
# ratio = fuzz.token_sort_ratio("Annual Income", "income")
# print(ratio)
# ratio = fuzz.token_sort_ratio("Spending Score", "score")
# print(ratio)

