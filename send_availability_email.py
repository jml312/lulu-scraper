from helpers.get_product_details import get_product_details
from helpers.send_email import send_email

def send_availability_email(lulu_data):
  findings = []
  for (url, size_to_check, item_name) in lulu_data:
    try:
      item_name = " ".join(item_name.split("_"))
      is_available, price = get_product_details(url, size_to_check)
      
      if is_available == None:
        continue
      
      text = f"<a href='{url}'>{item_name}</a> ({price}) in size {size_to_check.upper()} is {'AVAILABLE ✅' if is_available else 'NOT AVAILABLE ❌'}"
      findings.append((text, is_available))  
    except Exception:
      continue
    
  if all(not f[1] for f in findings):
    return "Nothing available", 400
    
  title = "Lulu Availability Report"
  body = "<ul>"
  for text, _ in findings:
    body += f"<li>{text}</li>" 
  body += "</ul>"
  
  return send_email(title, body)