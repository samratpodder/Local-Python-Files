import requests
import time
import fitz

creds = ["megsitec_covid19", "megsitec@12345"]


def login():
    s = requests.Session()
    s.headers.update({"X-Requested-With": "XMLHttpRequest"})
    csrf = s.get("https://ebooks.wileyindia.com/generatetoken?_={}".format(int(time.time()) + 24 * 60 * 60)).text
    csrf_tok = csrf[csrf.index('"') + 1: csrf.rindex('"')]

    # print(csrf_tok)
    resp = s.post("https://ebooks.wileyindia.com/ajaxlogin", data={"loginuser": creds[0],
                                                                   "loginpwd": creds[1],
                                                                   "task": "new-login",
                                                                   "rememberme": "on",
                                                                   "redirectUrl": "",
                                                                   "remotelogin": "on",
                                                                   "id": 0,
                                                                   "loginverificationcode": "",
                                                                   "csrfToken": csrf_tok})
    # print(resp)
    # print(resp.text)
    return s


book_name = input("Enter the book name: ")

sess = login()

book_url = "https://ebooks.wileyindia.com/pdfreader/{}".format(book_name)

book_resp = sess.get(book_url).text

start_ix = book_resp.index("bookUrl") + len("bookUrl") + 3  # Bad code
end_ix = book_resp.index('"', start_ix)

book_link = book_resp[start_ix:end_ix]

print(book_link)

print("Downloading...")

book_bytes = requests.get(book_link).content
book_xps = fitz.open("xps", book_bytes)
print("Saving XPS............")
open(book_name + ".xps", "wb+").write(book_bytes)
print("File saved as: {}".format(book_name + ".xps"))
# print("Converting XPS and saving as pdf...........")
# open(book_name + ".pdf", "wb+").write(book_xps.convertToPDF())
#print("File saved as: {}".format(book_name + ".pdf"))
