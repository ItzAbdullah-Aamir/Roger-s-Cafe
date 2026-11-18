def cafe():
  Menu = {
    "Coffee":250,"Tea":100,"Iced-Latte":250,
    "Cheesecake":1000,
    "Croissant":250,
    "Chocolate Cake":1500,
    }
  Receipt = {}
  total = 0
  print("----------------ROGER'S MENU----------------------")
  for item,price in Menu.items():
       print(f"{item} : Rs.{price}")

  while True:
      costumer_order = input("Enter the thing u want or remove or done: ").title()
      if costumer_order == "Done":
         break
      elif costumer_order == "Remove":
          remove_item=input("which item u want to remove: ").title()
          if remove_item in Receipt:
              del Receipt[remove_item]
              print(f"Removed {remove_item} from the list")
          else:
              print("The item is not in your receipt")
      elif costumer_order in Menu:
          number_of = int(input("Number of that item u want: "))
          if costumer_order in Receipt:
              Receipt[costumer_order]["qty"] += number_of
              Receipt[costumer_order]["price"] += Menu[costumer_order] * number_of
          else:
              Receipt[costumer_order] = {"qty":number_of,"price":Menu[costumer_order] * number_of}
      else:
          print("Sorry We dont have that Item")
  for item,details in Receipt.items():
      print(f"{details['qty']}x {item}: Rs.{details['price']}")
      total += details["price"]
  if total == 0:
      print("No items ordered, Thank you for visiting")
      return
  Promocode = input("Enter a promo code or type skip: ").upper()
  discount = 0
  if Promocode == "ROGERBOOM":
      discount = total * 0.50
      print("50% Discount Applied")
  elif Promocode != "" and Promocode != "SKIP":
      print("WAN WAN Invalid Code")
  final_total = total - discount
  print("---------------------The Legend's Receipt------------------------------")
  print(f"SUBTOTAL     :      {total}")
  print(f"DISCOUNT     :      {discount}")
  print(f"THE FINALE   :      {final_total}")
  with open("sales.txt", "a") as file:
      for item,details in Receipt.items():
       file.write(f"{details['qty']}x {item}: Rs.{details['price']}\n")
      file.write(f"Final Total: Rs.{final_total}\n")
      file.write("-------------------------\n")

cafe()
