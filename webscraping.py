import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading
import logging
import json

# Loglama yapılandırması
logging.basicConfig(filename='web_scraper.log', level=logging.INFO)

def log_message(message):
    logging.info(message)

# Veri çekme fonksiyonu
def fetch_data():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "URL field cannot be empty")
        return

    try:
        # User-Agent ile istek
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Accept-Language": "tr-TR,tr;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        # Proxy kullanmadan doğrudan istek
        response = requests.get(url, headers=headers, timeout=10)  # Timeout süresini 10 saniye olarak ayarladık
        response.raise_for_status()
    except requests.exceptions.Timeout:
        messagebox.showerror("Error", "Request timed out. Please check the URL or your internet connection.")
        return
    except requests.exceptions.TooManyRedirects:
        messagebox.showerror("Error", "Too many redirects. Please check the URL.")
        return
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 403:
            messagebox.showerror("Error", "403 Forbidden: You may not have access to this resource.")
        else:
            messagebox.showerror("Error", f"HTTP error occurred: {err}")
        return
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Başlık ve meta açıklama
    title = soup.title.string if soup.title else "No title"
    meta_desc = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc["content"] if meta_desc else "No description"

    results = soup.find_all('p')  # Örnek: Tüm paragrafları çekme

    # Çekilen veriyi saklama
    global fetched_data
    fetched_data = []
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Title: {title}\n")
    output_text.insert(tk.END, f"Description: {meta_desc}\n\n")

    for result in results:
        text = result.get_text(strip=True)
        text = text.replace("\n", " ").replace("\r", "")
        output_text.insert(tk.END, text + '\n')
        fetched_data.append({'Paragraph': text})

    log_message(f"Fetched data from {url}")
    display_table(fetched_data)

# Çok iş parçacıklı veri çekme
def fetch_data_threaded():
    threading.Thread(target=fetch_data).start()

# Veriyi tablo olarak göster
def display_table(data):
    df = pd.DataFrame(data)
    tree = ttk.Treeview(frame, columns=list(df.columns), show='headings')
    
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

# CSV kaydetme
def save_to_csv():
    if not fetched_data:
        messagebox.showerror("Error", "No data to save.")
        return
    
    filename = csv_filename_entry.get()
    if not filename:
        messagebox.showerror("Error", "Please enter a filename.")
        return

    df = pd.DataFrame(fetched_data)
    df.to_csv(f"{filename}.csv", index=False)
    messagebox.showinfo("Success", f"Data saved as {filename}.csv")

# JSON kaydetme
def save_to_json():
    if not fetched_data:
        messagebox.showerror("Error", "No data to save.")
        return
    
    filename = json_filename_entry.get()
    if not filename:
        messagebox.showerror("Error", "Please enter a filename.")
        return

    with open(f"{filename}.json", "w") as f:
        json.dump(fetched_data, f, indent=4)
    messagebox.showinfo("Success", f"Data saved as {filename}.json")

# Otomatik veri çekme
def auto_fetch(interval=3600):
    fetch_data_threaded()
    threading.Timer(interval, auto_fetch).start()

# Giriş kontrolü
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Success", "Logged in successfully")
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Arama fonksiyonu
def search_in_results():
    keyword = search_entry.get()
    if not keyword:
        messagebox.showerror("Error", "Search field cannot be empty")
        return
    
    filtered_results = [result['Paragraph'] for result in fetched_data if keyword.lower() in result['Paragraph'].lower()]
    
    output_text.delete("1.0", tk.END)
    for result in filtered_results:
        output_text.insert(tk.END, result + '\n')

# GUI ayarları
app = tk.Tk()
app.title("Web Scraper")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Giriş formu
ttk.Label(frame, text="Username:").grid(row=0, column=0, sticky=tk.W)
username_entry = ttk.Entry(frame, width=20)
username_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Password:").grid(row=1, column=0, sticky=tk.W)
password_entry = ttk.Entry(frame, show="*", width=20)
password_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

login_button = ttk.Button(frame, text="Login", command=login)
login_button.grid(row=1, column=2, sticky=tk.W)

# URL Girişi ve Arama
ttk.Label(frame, text="Enter URL:").grid(row=2, column=0, sticky=tk.W)
url_entry = ttk.Entry(frame, width=50)
url_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

fetch_button = ttk.Button(frame, text="Fetch Data", command=fetch_data_threaded)
fetch_button.grid(row=2, column=2, sticky=tk.W)

# Arama kutusu
ttk.Label(frame, text="Search:").grid(row=3, column=0, sticky=tk.W)
search_entry = ttk.Entry(frame, width=50)
search_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

search_button = ttk.Button(frame, text="Search", command=search_in_results)
search_button.grid(row=3, column=2, sticky=tk.W)

# Çıktı alanı
output_text = tk.Text(frame, wrap="word", height=20, width=80)
output_text.grid(row=4, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

# Kaydetme seçenekleri
ttk.Label(frame, text="CSV Filename:").grid(row=5, column=0, sticky=tk.W)
csv_filename_entry = ttk.Entry(frame, width=20)
csv_filename_entry.grid(row=5, column=1, sticky=(tk.W, tk.E))

save_csv_button = ttk.Button(frame, text="Save as CSV", command=save_to_csv)
save_csv_button.grid(row=5, column=2, sticky=tk.W)

ttk.Label(frame, text="JSON Filename:").grid(row=6, column=0, sticky=tk.W)
json_filename_entry = ttk.Entry(frame, width=20)
json_filename_entry.grid(row=6, column=1, sticky=(tk.W, tk.E))

save_json_button = ttk.Button(frame, text="Save as JSON", command=save_to_json)
save_json_button.grid(row=6, column=2, sticky=tk.W)

# Otomatik veri çekme (1 saatlik aralıklarla)
auto_fetch_button = ttk.Button(frame, text="Auto Fetch", command=lambda: auto_fetch(3600))
auto_fetch_button.grid(row=7, column=0, sticky=tk.W)

# Tablonun ayarları
frame.columnconfigure(1, weight=1)
frame.rowconfigure(4, weight=1)

# Global değişken
fetched_data = []

app.mainloop()

