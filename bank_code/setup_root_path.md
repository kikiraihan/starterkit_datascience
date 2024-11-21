"""
salin kode ini diawal tiap notebook anda, 
sehingga tidak perlu lagi kesulitan saat import internal modul.

Kode ini akan menambahkan root path, ke venv berjalan, 
sehingga tidak perlu lagi atur direktori / pindah direktori ke root di notebook.
"""

```
# supaya bisa panggil tools dengan bebas
import sys
path = '/Users/mohzulkiflikatili/2latihan_python/BI_AI_FINNANCE'
if path not in sys.path: sys.path.insert(0, path)
print(sys.path)
```
