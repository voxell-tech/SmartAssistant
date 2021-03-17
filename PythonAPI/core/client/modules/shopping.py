import bs4
import requests
import re



def handle(text, Mic, Agent):

  remove_words = ["how", "much", "is", "the", "a" "an"]
  for rw in remove_words:
    text = text.replace(rw, "")


  user_request = text

  res_google = requests.get("https://www.google.com/search?tbm=shop&q=" + user_request)

  soup_google = bs4.BeautifulSoup(res_google.text, "html.parser")


  find_price = soup_google.find_all("span", class_="HRLxBb")
  find_div = soup_google.find_all("div")
  find_title = soup_google.find_all("div", class_ = "rgHvZc")
  find_website_price = soup_google.find_all( "div" , class_= "dD8iuc")

  price_website = []
  product_name = []


  for i in find_title:
      b = (i.getText())
      product_name.append(b)


  for i in find_website_price:
      remove_class = "d1BlKc"
      if remove_class in i["class"]:
          continue
      else:
          a = (i.getText())
          price_website.append(a)
    

  print("done")

 

  print(price_website)
  print("")
  print(product_name)
  print("")



  results = "\n".join("Product: {}      Info: {}".format(x, y) for x, y in zip(product_name[0:5], price_website[0:5]))

  print(results)
  Mic.say("here are the results")



def isValid(text):
  # check if text is valid
  return (bool(re.search(r"\bhow much is \b", text, re.IGNORECASE)))