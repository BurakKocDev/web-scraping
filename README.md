Web Scraper Application
This is a simple web scraper application built with Tkinter for a graphical user interface (GUI) and BeautifulSoup for data extraction. The app fetches content from a specified URL, displays it, allows searching within the results, and provides options to save the data in CSV or JSON format.

Features
Login Functionality: Basic login form to access the application.
Fetch Data: Fetch content from a given URL, with headers to simulate a user-agent.
Display and Search Results: Shows fetched data in the output text area and allows keyword searching within the results.
Save Data: Save the extracted data as CSV or JSON files.
Auto Fetch: Automatically fetch data from the specified URL at a set interval.
Error Handling: Handles common request errors like timeouts, redirects, and HTTP errors.
Requirements
Python 3.x
Required Python libraries:
tkinter (for GUI)
requests (for HTTP requests)
beautifulsoup4 (for parsing HTML)
pandas (for data handling)
threading (for background tasks)
logging (for logging application events)
Install missing libraries using:

bash
Kodu kopyala
pip install requests beautifulsoup4 pandas
Usage
Run the Application: Run the web_scraper.py file:

bash
Kodu kopyala
python web_scraper.py
Login: Use the default login credentials (username: admin, password: password).

Enter URL and Fetch Data:

Input a URL in the "Enter URL" field and click Fetch Data.
Extracted data will display in the output area, and the table shows the fetched paragraphs.
Search within Results:

Use the "Search" field to find specific text within the extracted data.
Save Data:

CSV: Enter a filename in the CSV field and click Save as CSV.
JSON: Enter a filename in the JSON field and click Save as JSON.
Auto Fetch:

Click Auto Fetch to fetch data automatically at 1-hour intervals.
Logging
Logs are saved in web_scraper.log with details on data fetch events.

File Structure
web_scraper.py: Main application script.
web_scraper.log: Log file generated during runtime for debugging and data fetch tracking.
Error Handling
The application handles the following errors:

Timeouts: Notifies when the request times out.
Redirects: Alerts if there are too many redirects.
HTTP Errors: Specifically handles 403 (Forbidden) errors.



####TURKÇE####
Bu uygulama, Tkinter ile oluşturulmuş bir grafik arayüz (GUI) ve BeautifulSoup kullanarak veri kazıma işlemi yapan basit bir web kazıyıcıdır. Uygulama, belirtilen bir URL’den içerik çeker, içerikleri görüntüler, sonuçlar içinde arama yapmaya olanak tanır ve veriyi CSV veya JSON formatında kaydetme seçenekleri sunar.

Özellikler
Giriş İşlevselliği: Uygulamaya erişim için basit bir giriş formu.
Veri Çekme: Belirtilen URL’den veri çeker, kullanıcı temsilcisi simülasyonu için başlık bilgisi ekler.
Sonuçları Gösterme ve Arama: Çekilen veriler çıktı alanında gösterilir ve anahtar kelimelerle arama yapılabilir.
Veri Kaydetme: Çekilen verileri CSV veya JSON dosyası olarak kaydetme seçeneği.
Otomatik Veri Çekme: Belirli bir aralıkta otomatik olarak veri çekme işlevi.
Hata Yönetimi: Zaman aşımı, yönlendirme ve HTTP hataları gibi yaygın istek hatalarını yönetir.
Gereksinimler
Python 3.x
Gerekli Python kütüphaneleri:
tkinter (GUI için)
requests (HTTP istekleri için)
beautifulsoup4 (HTML işleme için)
pandas (veri işlemleri için)
threading (arka plan görevleri için)
logging (uygulama olaylarını kaydetmek için)
Eksik kütüphaneleri yüklemek için:

bash
Kodu kopyala
pip install requests beautifulsoup4 pandas
Kullanım
Uygulamayı Çalıştırın: web_scraper.py dosyasını çalıştırın:

bash
Kodu kopyala
python web_scraper.py
Giriş Yapın: Varsayılan giriş bilgilerini kullanın (kullanıcı adı: admin, şifre: password).

URL Girin ve Verileri Çekin:

"Enter URL" alanına bir URL girin ve Fetch Data butonuna tıklayın.
Çekilen veriler çıktı alanında ve tablo görünümünde gösterilecektir.
Sonuçlar İçinde Arama Yapın:

"Search" alanına anahtar kelime girerek çekilen veri içinde arama yapabilirsiniz.
Verileri Kaydedin:

CSV: CSV alanına bir dosya adı girin ve Save as CSV butonuna tıklayın.
JSON: JSON alanına bir dosya adı girin ve Save as JSON butonuna tıklayın.
Otomatik Veri Çekme:

Auto Fetch butonuna tıklayarak verileri 1 saatlik aralıklarla otomatik olarak çekebilirsiniz.
Loglama
web_scraper.log dosyasına veri çekme olayları ve hata mesajları kaydedilmektedir.

Dosya Yapısı
web_scraper.py: Ana uygulama dosyası.
web_scraper.log: Çalışma esnasında oluşturulan hata ayıklama ve veri çekme kayıt dosyası.
Hata Yönetimi
Uygulama aşağıdaki hataları yönetir:

Zaman Aşımı: İsteğin zaman aşımına uğradığını bildirir.
Yönlendirme Hataları: Çok fazla yönlendirme olduğunda uyarı verir.
HTTP Hataları: Özellikle 403 (Erişim Engellendi) hatalarını yönetir.
