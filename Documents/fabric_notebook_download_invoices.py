import requests
from pathlib import Path

# Replace with where you host the PDFs, for example an Azure Blob container SAS base URL,
# a static website endpoint, or a SharePoint direct-download base URL.
BASE_URL = 'https://YOUR_PUBLIC_HOST/invoices/2026'
TARGET_DIR = Path('/lakehouse/default/Files/Invoices')  # Fabric mounted Lakehouse path
TARGET_DIR.mkdir(parents=True, exist_ok=True)

months = [
    ('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'),
    ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'),
    ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December'),
]

for mm, month in months:
    file_name = f'invoice_2026_{mm}_{month}.pdf'
    url = f'{BASE_URL}/{mm}/{file_name}'
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    out_path = TARGET_DIR / file_name
    out_path.write_bytes(response.content)
    print(f'Downloaded {file_name} from {url} to {out_path}')
