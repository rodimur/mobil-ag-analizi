import sys
import os

# Proje kök dizinini PYTHONPATH'e ekle
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.models.database import Base, engine
from app.models.schemas import *  # Gerekirse tüm modelleri import edin

print("Veritabanı oluşturuluyor...")
Base.metadata.create_all(bind=engine)
print("Veritabanı başarıyla oluşturuldu.")
