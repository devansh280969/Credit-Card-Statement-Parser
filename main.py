
# from extractor.pdf_extractor import extract_text

# pdf_path = "data/ICICI_1.pdf"  # change this
# text2 = extract_text(pdf_path)

# print(text2[:2000])  # print first 2000 chars





# from extractor.pdf_extractor import extract_text
# from detector.issuer_detector import detect_issuer

# pdf_path = "data/Axis_1.pdf"  # change per bank
# text = extract_text(pdf_path)

# issuer = detect_issuer(text)
# print("DETECTED ISSUER:", issuer)






# from extractor.pdf_extractor import extract_text
# from detector.issuer_detector import detect_issuer
# from parsers.router import get_parser

# pdf_path = "data/Axis_1.pdf"
# text = extract_text(pdf_path)

# issuer = detect_issuer(text)
# print("ISSUER:", issuer)

# parser = get_parser(issuer)

# if not parser:
#     print("No parser available for this bank")
# else:
#     result = parser.parse(text)
#     print("PARSER OUTPUT:", result)






# from extractor.pdf_extractor import extract_text
# from utils.regex import extract_card_last4, extract_total_due, extract_due_date

# pdf_path = "data/ICICI_1.pdf"
# text = extract_text(pdf_path)

# print("CARD LAST 4:", extract_card_last4(text))
# print("TOTAL DUE:", extract_total_due(text))
# print("DUE DATE:", extract_due_date(text))






# from extractor.pdf_extractor import extract_text
# from detector.issuer_detector import detect_issuer
# from parsers.router import get_parser

# pdf_path = "data/ICICI_1.pdf"
# text = extract_text(pdf_path)

# issuer = detect_issuer(text)
# parser = get_parser(issuer)
# data = parser.parse(text)
# print(data)







# from extractor.pdf_extractor import extract_text
# from utils.regex import extract_statement_period
# pdf_path="data/ICICI_1.pdf"
# text = extract_text(pdf_path)
# print("STATEMENT PERIOD:", extract_statement_period(text))




# from extractor.pdf_extractor import extract_text
# from utils.regex import extract_transaction_count

# text = extract_text(pdf_path)
# print("TRANSACTION COUNT:", extract_transaction_count(text))


from pdf_extractor import extract_text
from issuer_detector import detect_issuer
from parsers.router import get_parser
pdf_path="data/Axis_1.pdf"
a="data/Axis_1.pdf"     
c="data/CITIBANK.pdf"   
h="data/HDFC.pdf"       
ic="data/ICICI_1.pdf"  
id="data/IDFC.pdf"      
text = extract_text(h)

issuer = detect_issuer(text)
parser = get_parser(issuer)
parsed_data = parser.parse(text)
data = {
    "bank_name": issuer,
    **parsed_data
}
print(data)
from pdf_extractor import extract_text

# text = extract_text(c)  
# print(text[:4000])
