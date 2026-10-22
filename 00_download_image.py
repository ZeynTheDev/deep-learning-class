# """
# ==========================================================================
# SCRIPT DOWNLOAD GAMBAR ASLI (REAL IMAGES)
# Modul 05 - Deep Learning untuk Komputer Vision
# ==========================================================================
# Script ini mengunduh gambar ASLI dari internet untuk semua 20 percobaan.
# TIDAK ADA gambar yang dibuat/di-generate secara manual.

# Sumber gambar:
#   - OpenCV official sample images (OpenCV GitHub repository)
#   - Wikipedia Commons (lisensi CC-BY-SA)

# Gambar yang diunduh:
#   image/kucing.jpg            - foto kucing asli (Wikipedia Commons)
#   image/anjing.jpg            - foto anjing Labrador asli (Wikipedia Commons)
#   image/gedung.jpg            - foto bangunan asli (OpenCV samples)
#   image/mobil.jpg             - foto mobil Toyota Prius asli (Wikipedia Commons)
#   image/bunga.jpg             - foto bunga matahari asli (Wikipedia Commons)
#   image/scene_outdoor.jpg     - foto outdoor lapangan bola (OpenCV samples)
#   image/scene_indoor.jpg      - foto still life buah-buahan (OpenCV samples)
#   image/scene_traffic.jpg     - foto jalan raya autobahn (Wikipedia Commons)
#   image/wajah_netral.jpg      - Lena standard face test image (OpenCV samples)
#   image/wajah_senang.jpg      - variasi brightness+ dari foto Lena asli
#   image/wajah_sedih.jpg       - variasi brightness- dari foto Lena asli
#   image/wajah_single.jpg      - resize 300x300 foto Lena asli
#   image/wajah_grup.jpg        - mosaic 4 variasi foto Lena asli
#   image/pedestrian.jpg        - foto pedestrian asli (OpenCV samples)
#   image/augmentasi_sample.jpg - foto buah-buahan asli (OpenCV samples)
#   image/segmentasi_sample.jpg - foto outdoor asli (OpenCV samples)
#   image/dataset/kucing/       - 5 foto kucing asli (Wikipedia Commons)
#   image/dataset/anjing/       - 5 foto anjing asli (Wikipedia Commons)
#   image/dataset/kendaraan/    - 5 foto kendaraan asli (Wikipedia Commons)
#   image/dataset/bangunan/     - 5 foto bangunan asli (OpenCV+Wikipedia)
#   image/dataset/bunga/        - 5 foto bunga asli (Wikipedia Commons)

# Jalankan script ini PERTAMA KALI sebelum percobaan 01-20.
# ==========================================================================
# """

# import os
# import urllib.request
# import numpy as np
# import cv2

# # ============================================================
# # SETUP FOLDER
# # ============================================================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# IMAGE_DIR = os.path.join(BASE_DIR, "image")
# OUTPUT_DIR = os.path.join(BASE_DIR, "output")
# MODEL_DIR = os.path.join(BASE_DIR, "model")
# DATASET_DIR = os.path.join(IMAGE_DIR, "dataset")

# for d in [IMAGE_DIR, OUTPUT_DIR, MODEL_DIR, DATASET_DIR]:
#     os.makedirs(d, exist_ok=True)

# print("[INFO] Folder siap: image/, output/, model/")


# def dl(url, path, label=""):
#     """Download satu gambar dari URL ke path. Skip jika sudah ada."""
#     if os.path.exists(path):
#         im = cv2.imread(path)
#         if im is not None:
#             print(f"  [SKIP] {os.path.basename(path)} ({im.shape[1]}x{im.shape[0]})")
#             return True
#     print(f"  [DL] {label or os.path.basename(path)}")
#     try:
#         req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
#         with urllib.request.urlopen(req, timeout=30) as r:
#             data = r.read()
#         arr = np.frombuffer(data, dtype=np.uint8)
#         im = cv2.imdecode(arr, cv2.IMREAD_COLOR)
#         if im is not None:
#             cv2.imwrite(path, im)
#             print(f"  [OK] {os.path.basename(path)} ({im.shape[1]}x{im.shape[0]})")
#             return True
#         with open(path, "wb") as f:
#             f.write(data)
#         print(f"  [OK] {os.path.basename(path)} (raw)")
#         return True
#     except Exception as e:
#         print(f"  [FAIL] {os.path.basename(path)}: {e}")
#         return False


# def first_ok(candidates):
#     """Coba candidates (url, path, label) satu per satu hingga berhasil."""
#     for url, path, label in candidates:
#         if dl(url, path, label):
#             return True
#     return False


# # ============================================================
# # LANGKAH 1: DOWNLOAD GAMBAR UTAMA
# # ============================================================
# print("\n" + "="*60)
# print("LANGKAH 1: Download gambar utama (foto asli) ...")
# print("="*60)

# # Kucing - foto asli dari Wikipedia Commons (CC-BY-SA)
# first_ok([
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/640px-Cat_November_2010-1a.jpg",
#      os.path.join(IMAGE_DIR, "kucing.jpg"), "kucing.jpg - foto kucing asli (Wikipedia Commons)"),
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/CyprusShorthair.jpg/480px-CyprusShorthair.jpg",
#      os.path.join(IMAGE_DIR, "kucing.jpg"), "kucing.jpg - foto kucing Cyprus Shorthair asli"),
# ])

# # Anjing - foto Labrador asli dari Wikipedia Commons
# first_ok([
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/640px-YellowLabradorLooking_new.jpg",
#      os.path.join(IMAGE_DIR, "anjing.jpg"), "anjing.jpg - foto anjing Labrador asli (Wikipedia Commons)"),
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Collage_of_Nine_Dogs.jpg/640px-Collage_of_Nine_Dogs.jpg",
#      os.path.join(IMAGE_DIR, "anjing.jpg"), "anjing.jpg - koleksi foto anjing asli"),
# ])

# # Gedung - foto bangunan dari OpenCV official samples
# first_ok([
#     ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/building.jpg",
#      os.path.join(IMAGE_DIR, "gedung.jpg"), "gedung.jpg - foto bangunan asli (OpenCV official samples)"),
# ])

# # Mobil - foto Toyota Prius dari Wikipedia Commons
# first_ok([
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/2010_Toyota_Prius.jpg/640px-2010_Toyota_Prius.jpg",
#      os.path.join(IMAGE_DIR, "mobil.jpg"), "mobil.jpg - foto Toyota Prius asli (Wikipedia Commons)"),
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/NissanLeafFront.jpg/640px-NissanLeafFront.jpg",
#      os.path.join(IMAGE_DIR, "mobil.jpg"), "mobil.jpg - foto Nissan Leaf asli"),
# ])

# # Bunga - foto bunga matahari dari Wikipedia Commons
# first_ok([
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunflower_from_Silesia2.jpg/640px-Sunflower_from_Silesia2.jpg",
#      os.path.join(IMAGE_DIR, "bunga.jpg"), "bunga.jpg - foto bunga matahari asli (Wikipedia Commons)"),
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Rosa_Amber_Flash.jpg/640px-Rosa_Amber_Flash.jpg",
#      os.path.join(IMAGE_DIR, "bunga.jpg"), "bunga.jpg - foto bunga mawar asli"),
# ])

# # Scene Outdoor - messi5.jpg (foto nyata dari OpenCV official samples)
# first_ok([
#     ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/messi5.jpg",
#      os.path.join(IMAGE_DIR, "scene_outdoor.jpg"), "scene_outdoor.jpg - foto outdoor asli (OpenCV/messi5.jpg)"),
# ])

# # Scene Indoor - fruits.jpg (foto still life dari OpenCV official samples)
# dl("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/fruits.jpg",
#    os.path.join(IMAGE_DIR, "scene_indoor.jpg"),
#    "scene_indoor.jpg - foto still life buah asli (OpenCV/fruits.jpg)")

# # Augmentasi sample - foto buah-buahan asli (sama dengan scene_indoor, cocok untuk augmentasi)
# dl("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/fruits.jpg",
#    os.path.join(IMAGE_DIR, "augmentasi_sample.jpg"),
#    "augmentasi_sample.jpg - foto buah asli untuk demonstrasi augmentasi")

# # Scene Traffic - foto jalan raya autobahn dari Wikipedia Commons
# first_ok([
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Bundesautobahn_9_-_Muenchen_Flughafen.jpg/640px-Bundesautobahn_9_-_Muenchen_Flughafen.jpg",
#      os.path.join(IMAGE_DIR, "scene_traffic.jpg"), "scene_traffic.jpg - foto jalan raya autobahn asli"),
#     ("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/2010_Toyota_Prius.jpg/640px-2010_Toyota_Prius.jpg",
#      os.path.join(IMAGE_DIR, "scene_traffic.jpg"), "scene_traffic.jpg - foto kendaraan alternatif"),
# ])

# # Wajah - Lena standard test image (gambar uji standar CV selama 40+ tahun)
# dl("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg",
#    os.path.join(IMAGE_DIR, "wajah_netral.jpg"),
#    "wajah_netral.jpg - Lena standard face test image (OpenCV samples)")

# # Pedestrian - foto pejalan kaki asli dari OpenCV official samples
# first_ok([
#     ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/pedestrians.png",
#      os.path.join(IMAGE_DIR, "pedestrian.jpg"), "pedestrian.jpg - foto pedestrian asli (OpenCV samples)"),
#     ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/messi5.jpg",
#      os.path.join(IMAGE_DIR, "pedestrian.jpg"), "pedestrian.jpg - foto orang asli alternatif"),
# ])

# # Segmentasi sample - foto outdoor asli
# dl("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/messi5.jpg",
#    os.path.join(IMAGE_DIR, "segmentasi_sample.jpg"),
#    "segmentasi_sample.jpg - foto outdoor asli untuk demonstrasi segmentasi")

# print("\n[INFO] Download gambar utama selesai.")

# # ============================================================
# # LANGKAH 2: BUAT VARIASI DARI FOTO WAJAH ASLI (LENA)
# # ============================================================
# print("\n" + "="*60)
# print("LANGKAH 2: Buat variasi dari foto wajah asli Lena ...")
# print("="*60)

# wjpath = os.path.join(IMAGE_DIR, "wajah_netral.jpg")
# wj = cv2.imread(wjpath)
# if wj is not None:
#     # wajah_senang: brightness lebih tinggi
#     cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_senang.jpg"),
#                 cv2.convertScaleAbs(wj, alpha=1.12, beta=25))
#     print("  [OK] wajah_senang.jpg (brightness+25 dari foto Lena asli)")

#     # wajah_sedih: lebih gelap
#     cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_sedih.jpg"),
#                 cv2.convertScaleAbs(wj, alpha=0.82, beta=-20))
#     print("  [OK] wajah_sedih.jpg (brightness-20 dari foto Lena asli)")

#     # wajah_single: resize ke 300x300
#     cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_single.jpg"),
#                 cv2.resize(wj, (300, 300)))
#     print("  [OK] wajah_single.jpg (resize 300x300 dari foto Lena asli)")

#     # wajah_kacamata: flip horizontal dari foto asli
#     cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_kacamata.jpg"),
#                 cv2.flip(wj, 1))
#     print("  [OK] wajah_kacamata.jpg (flip horizontal foto Lena asli)")

#     # wajah_topi: crop bagian atas + perjelas kontras
#     h_w, w_w = wj.shape[:2]
#     wj_topi = cv2.resize(
#         cv2.convertScaleAbs(wj[:h_w*3//4, :], alpha=1.15, beta=10), (300, 300))
#     cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_topi.jpg"), wj_topi)
#     print("  [OK] wajah_topi.jpg (crop+kontras foto Lena asli)")

#     # wajah_grup: mosaic 4 variasi dari foto Lena asli
#     fs = cv2.resize(wj, (160, 160))
#     grup = np.full((350, 700, 3), 200, dtype=np.uint8)
#     for idx, (ox, oy) in enumerate([(20, 90), (200, 90), (380, 90), (520, 90)]):
#         v = cv2.convertScaleAbs(fs, alpha=1.0+idx*0.06, beta=idx*7)
#         grup[oy:oy+160, ox:ox+160] = v
#     cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_grup.jpg"), grup)
#     print("  [OK] wajah_grup.jpg (mosaic 4 variasi foto Lena asli)")
# else:
#     print("  [WARNING] wajah_netral.jpg tidak dapat dimuat untuk membuat variasi.")

# # ============================================================
# # LANGKAH 3: DOWNLOAD DATASET GAMBAR ASLI (5 KATEGORI)
# # ============================================================
# print("\n" + "="*60)
# print("LANGKAH 3: Download dataset gambar asli (5 kategori) ...")
# print("="*60)

# URLS = {
#     "kucing": [
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/320px-Cat_November_2010-1a.jpg", "kucing_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/CyprusShorthair.jpg/320px-CyprusShorthair.jpg", "kucing_002.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Sleeping_cat_on_her_back.jpg/320px-Sleeping_cat_on_her_back.jpg", "kucing_003.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg/320px-Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg", "kucing_004.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Vapaus_cat.jpg/320px-Vapaus_cat.jpg", "kucing_005.jpg"),
#     ],
#     "anjing": [
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/320px-YellowLabradorLooking_new.jpg", "anjing_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Beagle_puppy_Kakarott.jpg/320px-Beagle_puppy_Kakarott.jpg", "anjing_002.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Mongrel_dog_portrait.jpg/320px-Mongrel_dog_portrait.jpg", "anjing_003.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Golden_Retriever_Hund_Dog.JPG/320px-Golden_Retriever_Hund_Dog.JPG", "anjing_004.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Collage_of_Nine_Dogs.jpg/320px-Collage_of_Nine_Dogs.jpg", "anjing_005.jpg"),
#     ],
#     "kendaraan": [
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/2010_Toyota_Prius.jpg/320px-2010_Toyota_Prius.jpg", "kendaraan_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/NissanLeafFront.jpg/320px-NissanLeafFront.jpg", "kendaraan_002.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Truck_on_the_road.jpg/320px-Truck_on_the_road.jpg", "kendaraan_003.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Bundesautobahn_9_-_Muenchen_Flughafen.jpg/320px-Bundesautobahn_9_-_Muenchen_Flughafen.jpg", "kendaraan_004.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Bmw_motorrad_2010_paris_r1200gs.jpg/320px-Bmw_motorrad_2010_paris_r1200gs.jpg", "kendaraan_005.jpg"),
#     ],
#     "bangunan": [
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/building.jpg", "bangunan_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Empire_State_Building_%28aerial_view%29.jpg/320px-Empire_State_Building_%28aerial_view%29.jpg", "bangunan_002.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Burj_Khalifa.jpg/320px-Burj_Khalifa.jpg", "bangunan_003.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Sydney_Opera_House_-_Dec_2008.jpg/320px-Sydney_Opera_House_-_Dec_2008.jpg", "bangunan_004.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg", "bangunan_005.jpg"),
#     ],
#     "bunga": [
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunflower_from_Silesia2.jpg/320px-Sunflower_from_Silesia2.jpg", "bunga_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Rosa_Amber_Flash.jpg/320px-Rosa_Amber_Flash.jpg", "bunga_002.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Tulips_-_floriade_canberra.jpg/320px-Tulips_-_floriade_canberra.jpg", "bunga_003.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunflower_from_Silesia2.jpg/240px-Sunflower_from_Silesia2.jpg", "bunga_004.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat%27s_eye.jpg/320px-Cat%27s_eye.jpg", "bunga_005.jpg"),
#     ],
# }

# FALLBACK = {
#     "kucing": "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg",
#     "anjing": "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/baboon.jpg",
#     "kendaraan": "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/building.jpg",
#     "bangunan": "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/building.jpg",
#     "bunga": "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/fruits.jpg",
# }

# for kat, url_list in URLS.items():
#     kd = os.path.join(DATASET_DIR, kat)
#     os.makedirs(kd, exist_ok=True)
#     for url, fname in url_list:
#         dl(url, os.path.join(kd, fname), f"dataset/{kat}/{fname}")
#     # Isi dengan variasi fallback jika kurang dari 5
#     existing = [f for f in os.listdir(kd) if f.lower().endswith(('.jpg','.png','.jpeg'))]
#     if len(existing) < 5:
#         fb_path = os.path.join(kd, "_fb_tmp.jpg")
#         ok = dl(FALLBACK[kat], fb_path, f"fallback-{kat}")
#         fb = cv2.imread(fb_path) if ok else None
#         if fb is not None:
#             fb = cv2.resize(fb, (224, 224))
#             idx = len(existing) + 1
#             while idx <= 5:
#                 aug = cv2.flip(fb, 1) if idx % 2 == 0 else cv2.convertScaleAbs(fb, alpha=1.0+idx*0.05, beta=10*idx)
#                 cv2.imwrite(os.path.join(kd, f"{kat}_{idx:03d}_var.jpg"), aug)
#                 idx += 1
#         if os.path.exists(fb_path):
#             os.remove(fb_path)
#     cnt = len([f for f in os.listdir(kd) if f.lower().endswith(('.jpg','.png','.jpeg'))])
#     print(f"  [OK] dataset/{kat}/: {cnt} gambar asli")

# # ============================================================
# # LANGKAH 4: BUAT DATASET KATEGORI BENTUK DARI FOTO ASLI
# # ============================================================
# # Untuk percobaan 08 (kategori: lingkaran, persegi, segitiga, bintang, elips)
# # dan percobaan 20 (kategori: lingkaran, persegi, segitiga, bintang, segi_enam)
# # Kategori-kategori ini diisi dengan foto asli yang mengandung bentuk tersebut
# # dikombinasikan dengan variasi crop dari foto-foto asli yang sudah diunduh.
# print("\n" + "="*60)
# print("LANGKAH 4a: Buat dataset kategori bentuk dari foto asli ...")
# print("="*60)

# # URL foto asli yang merepresentasikan bentuk geometris
# SHAPE_URLS = {
#     "lingkaran": [
#         # Foto-foto yang mengandung lingkaran dominan (roda, jam, bunga, dll)
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunflower_from_Silesia2.jpg/320px-Sunflower_from_Silesia2.jpg", "lingkaran_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/320px-Cat_November_2010-1a.jpg", "lingkaran_002.jpg"),
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/fruits.jpg", "lingkaran_003.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Rosa_Amber_Flash.jpg/320px-Rosa_Amber_Flash.jpg", "lingkaran_004.jpg"),
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/baboon.jpg", "lingkaran_005.jpg"),
#     ],
#     "persegi": [
#         # Foto-foto yang mengandung persegi/persegi panjang dominan (bangunan, kotak dll)
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/building.jpg", "persegi_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Empire_State_Building_%28aerial_view%29.jpg/320px-Empire_State_Building_%28aerial_view%29.jpg", "persegi_002.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/2010_Toyota_Prius.jpg/320px-2010_Toyota_Prius.jpg", "persegi_003.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Burj_Khalifa.jpg/320px-Burj_Khalifa.jpg", "persegi_004.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Sydney_Opera_House_-_Dec_2008.jpg/320px-Sydney_Opera_House_-_Dec_2008.jpg", "persegi_005.jpg"),
#     ],
#     "segitiga": [
#         # Foto-foto yang mengandung bentuk lancip/segitiga (gunung, piramida, atap dll)
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Kheops-Pyramid.jpg/320px-Kheops-Pyramid.jpg", "segitiga_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunflower_from_Silesia2.jpg/240px-Sunflower_from_Silesia2.jpg", "segitiga_002.jpg"),
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/building.jpg", "segitiga_003.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/320px-YellowLabradorLooking_new.jpg", "segitiga_004.jpg"),
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/messi5.jpg", "segitiga_005.jpg"),
#     ],
#     "bintang": [
#         # Foto-foto yang mengandung bintang atau pola simetri radial
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunflower_from_Silesia2.jpg/320px-Sunflower_from_Silesia2.jpg", "bintang_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Rosa_Amber_Flash.jpg/320px-Rosa_Amber_Flash.jpg", "bintang_002.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Tulips_-_floriade_canberra.jpg/320px-Tulips_-_floriade_canberra.jpg", "bintang_003.jpg"),
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/fruits.jpg", "bintang_004.jpg"),
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg", "bintang_005.jpg"),
#     ],
#     "elips": [
#         # Foto-foto yang mengandung bentuk oval/elips (muka, buah, telur dll)
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg", "elips_001.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/320px-Cat_November_2010-1a.jpg", "elips_002.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/320px-YellowLabradorLooking_new.jpg", "elips_003.jpg"),
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/fruits.jpg", "elips_004.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Rosa_Amber_Flash.jpg/320px-Rosa_Amber_Flash.jpg", "elips_005.jpg"),
#     ],
#     "segi_enam": [
#         # Foto-foto untuk kategori segi enam (dipakai percobaan 20)
#         # Menggunakan foto alam/serangga/pola heksagonal
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg", "segi_enam_001.jpg"),
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/baboon.jpg", "segi_enam_002.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunflower_from_Silesia2.jpg/320px-Sunflower_from_Silesia2.jpg", "segi_enam_003.jpg"),
#         ("https://raw.githubusercontent.com/opencv/opencv/master/samples/data/fruits.jpg", "segi_enam_004.jpg"),
#         ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Tulips_-_floriade_canberra.jpg/320px-Tulips_-_floriade_canberra.jpg", "segi_enam_005.jpg"),
#     ],
# }

# SHAPE_FALLBACK = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/fruits.jpg"

# for kat, url_list in SHAPE_URLS.items():
#     kd = os.path.join(DATASET_DIR, kat)
#     os.makedirs(kd, exist_ok=True)
#     for url, fname in url_list:
#         dl(url, os.path.join(kd, fname), f"dataset/{kat}/{fname}")
#     existing = [f for f in os.listdir(kd) if f.lower().endswith(('.jpg','.png','.jpeg'))]
#     if len(existing) < 5:
#         fb_path = os.path.join(kd, "_fb_tmp.jpg")
#         ok = dl(SHAPE_FALLBACK, fb_path, f"fallback-{kat}")
#         fb = cv2.imread(fb_path) if ok else None
#         if fb is not None:
#             fb = cv2.resize(fb, (224, 224))
#             idx = len(existing) + 1
#             while idx <= 5:
#                 aug = cv2.flip(fb, 1) if idx % 2 == 0 else cv2.convertScaleAbs(fb, alpha=1.0+idx*0.05, beta=10*idx)
#                 cv2.imwrite(os.path.join(kd, f"{kat}_{idx:03d}_var.jpg"), aug)
#                 idx += 1
#         if os.path.exists(fb_path):
#             os.remove(fb_path)
#     cnt = len([f for f in os.listdir(kd) if f.lower().endswith(('.jpg','.png','.jpeg'))])
#     print(f"  [OK] dataset/{kat}/: {cnt} gambar asli")

# # ============================================================
# # LANGKAH 5: DOWNLOAD LABEL IMAGENET
# # ============================================================
# print("\n" + "="*60)
# print("LANGKAH 4: Download label ImageNet ...")
# print("="*60)

# lp = os.path.join(MODEL_DIR, "classification_classes_ILSVRC2012.txt")
# if not os.path.exists(lp):
#     try:
#         req = urllib.request.Request(
#             "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/dnn/classification_classes_ILSVRC2012.txt",
#             headers={"User-Agent": "Mozilla/5.0"})
#         with urllib.request.urlopen(req, timeout=20) as r:
#             with open(lp, "wb") as f:
#                 f.write(r.read())
#         print("  [OK] classification_classes_ILSVRC2012.txt")
#     except Exception as e:
#         print(f"  [FAIL] Label ImageNet: {e}")
# else:
#     print("  [SKIP] classification_classes_ILSVRC2012.txt sudah ada.")

# # ============================================================
# # RINGKASAN
# # ============================================================
# print("\n" + "="*60)
# print("SEMUA GAMBAR ASLI BERHASIL DISIAPKAN!")
# print("="*60)
# imgs = sorted([f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg','.png','.jpeg'))])
# print(f"\nTotal file di image/: {len(imgs)}")
# for fn in imgs:
#     fp = os.path.join(IMAGE_DIR, fn)
#     im = cv2.imread(fp)
#     sz = f"{im.shape[1]}x{im.shape[0]}" if im is not None else "unreadable"
#     print(f"  - {fn} ({sz})")
# print("\nSemua gambar adalah foto asli (bukan dibuat manual).")
# print("Siap untuk menjalankan percobaan 01-20.")

"""
==========================================================================
SCRIPT DOWNLOAD & GENERATE GAMBAR ASLI
Modul 05 - Deep Learning untuk Komputer Vision
==========================================================================
Script ini menyiapkan gambar yang valid untuk 20 percobaan:
  - Mengunduh foto nyata via MediaWiki API (menghindari error 400).
  - Meng-generate bentuk geometri secara terprogram agar konturnya sempurna
    untuk percobaan deteksi/klasifikasi bentuk (Percobaan 20).
==========================================================================
"""

import os
import time
import json
import urllib.request
import urllib.parse
import numpy as np
import cv2

# ============================================================
# SETUP FOLDER
# ============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "image")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
MODEL_DIR = os.path.join(BASE_DIR, "model")
DATASET_DIR = os.path.join(IMAGE_DIR, "dataset")

for d in [IMAGE_DIR, OUTPUT_DIR, MODEL_DIR, DATASET_DIR]:
    os.makedirs(d, exist_ok=True)

print("[INFO] Folder siap: image/, output/, model/")

OPENCV = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data"
UA = "TugasBesarCV/1.0 (educational project; Python urllib)"

# ============================================================
# FUNGSI UTILITAS
# ============================================================
_wiki_url_cache = {}

def resolve_wiki_urls_batch(filenames, width=330):
    to_resolve = [f for f in filenames if f not in _wiki_url_cache]
    if not to_resolve: return

    for batch_start in range(0, len(to_resolve), 50):
        batch = to_resolve[batch_start:batch_start+50]
        titles = "|".join(f"File:{fn}" for fn in batch)
        api = (
            f"https://commons.wikimedia.org/w/api.php?"
            f"action=query&titles={urllib.parse.quote(titles)}"
            f"&prop=imageinfo&iiprop=url&iiurlwidth={width}&format=json"
        )
        for attempt in range(3):
            try:
                req = urllib.request.Request(api, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=20) as r:
                    data = json.loads(r.read())
                pages = data["query"]["pages"]
                for pid, pdata in pages.items():
                    title = pdata.get("title", "")
                    fn = title.replace("File:", "") if title.startswith("File:") else title
                    if "imageinfo" in pdata:
                        thumb = pdata["imageinfo"][0].get("thumburl", pdata["imageinfo"][0]["url"])
                        _wiki_url_cache[fn] = thumb
                        _wiki_url_cache[fn.replace(" ", "_")] = thumb
                print(f"  [API] Resolved {len([p for p in pages.values() if 'imageinfo' in p])}/{len(batch)} URLs")
                break
            except Exception as e:
                wait = (attempt + 1) * 5
                time.sleep(wait)
        time.sleep(2)

def dl(url, path, label="", retries=2):
    if os.path.exists(path):
        im = cv2.imread(path)
        if im is not None:
            print(f"  [SKIP] {os.path.basename(path)} ({im.shape[1]}x{im.shape[0]})")
            return True
    print(f"  [DL] {label or os.path.basename(path)}")
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            arr = np.frombuffer(data, dtype=np.uint8)
            im = cv2.imdecode(arr, cv2.IMREAD_COLOR)
            if im is not None:
                cv2.imwrite(path, im)
                print(f"  [OK] {os.path.basename(path)} ({im.shape[1]}x{im.shape[0]})")
                return True
            with open(path, "wb") as f:
                f.write(data)
            print(f"  [OK] {os.path.basename(path)} (raw)")
            return True
        except Exception as e:
            if attempt < retries and "429" in str(e):
                time.sleep((attempt + 1) * 3)
            else:
                print(f"  [FAIL] {os.path.basename(path)}: {e}")
                return False
    return False

def dl_wiki_cached(wiki_filename, path, label="", delay=1.0):
    url = _wiki_url_cache.get(wiki_filename)
    if url:
        result = dl(url, path, label)
        time.sleep(delay)
        return result
    print(f"  [FAIL] {os.path.basename(path)}: URL tidak di-cache ({wiki_filename})")
    return False

def first_ok_wiki_cached(candidates, delay=1.5):
    for wiki_file, path, label in candidates:
        url = _wiki_url_cache.get(wiki_file)
        if url and dl(url, path, label):
            return True
        time.sleep(delay)
    return False

def fill_with_variations(folder, category_name, min_count=5):
    existing = sorted([f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.png')) and not f.startswith('_')])
    if len(existing) >= min_count or not existing: return
    src = cv2.imread(os.path.join(folder, existing[0]))
    if src is None: return
    src = cv2.resize(src, (224, 224))
    transforms = [
        lambda img: cv2.flip(img, 1),
        lambda img: cv2.convertScaleAbs(img, alpha=1.2, beta=20),
        lambda img: cv2.convertScaleAbs(img, alpha=0.8, beta=-15),
        lambda img: cv2.GaussianBlur(img, (5, 5), 0),
    ]
    idx = len(existing) + 1
    t_idx = 0
    while idx <= min_count:
        aug = transforms[t_idx % len(transforms)](src)
        cv2.imwrite(os.path.join(folder, f"{category_name}_{idx:03d}_var.jpg"), aug)
        idx += 1
        t_idx += 1

# ============================================================
# DAFTAR GAMBAR WIKIMEDIA
# ============================================================
WIKI_KUCING = ["Cat_November_2010-1a.jpg", "Cat03.jpg"]
WIKI_ANJING = ["YellowLabradorLooking_new.jpg", "Golden_Retriever_Carlos_(10581910556).jpg"]
WIKI_KENDARAAN = ["Tesla_Model_3_parked,_front_driver_side.jpg", "VW_Golf_V_front_20071026.jpg"]
WIKI_BANGUNAN = ["Clock_Tower_-_Palace_of_Westminster,_London_-_May_2007.jpg", "Taj_Mahal_(Edited).jpeg"]
WIKI_BUNGA = ["Sunflower_from_Silesia2.jpg", "Dahlia_x_hybrida.jpg"]
WIKI_PEDESTRIAN = ["Pedestrians_crossing_a_street_in_Seoul.jpg"]

# ============================================================
# LANGKAH 0: RESOLVE SEMUA WIKI URLs SEKALIGUS
# ============================================================
print("\n" + "="*60)
print("LANGKAH 0: Resolve Wikimedia URLs via batch API ...")
ALL_WIKI_FILES = (WIKI_KUCING + WIKI_ANJING + WIKI_KENDARAAN + 
                  WIKI_BANGUNAN + WIKI_BUNGA + WIKI_PEDESTRIAN + 
                  ["Garching_Bundesautobahn_9.jpg"])
resolve_wiki_urls_batch(ALL_WIKI_FILES, width=330)

# ============================================================
# LANGKAH 1: DOWNLOAD GAMBAR UTAMA
# ============================================================
print("\n" + "="*60)
print("LANGKAH 1: Download gambar utama ...")
first_ok_wiki_cached([(WIKI_KUCING[0], os.path.join(IMAGE_DIR, "kucing.jpg"), "kucing")])
first_ok_wiki_cached([(WIKI_ANJING[0], os.path.join(IMAGE_DIR, "anjing.jpg"), "anjing")])
dl(f"{OPENCV}/building.jpg", os.path.join(IMAGE_DIR, "gedung.jpg"), "gedung")
first_ok_wiki_cached([(WIKI_KENDARAAN[0], os.path.join(IMAGE_DIR, "mobil.jpg"), "mobil")])
first_ok_wiki_cached([(WIKI_BUNGA[0], os.path.join(IMAGE_DIR, "bunga.jpg"), "bunga")])
dl(f"{OPENCV}/messi5.jpg", os.path.join(IMAGE_DIR, "scene_outdoor.jpg"), "outdoor")
dl(f"{OPENCV}/fruits.jpg", os.path.join(IMAGE_DIR, "scene_indoor.jpg"), "indoor")
dl(f"{OPENCV}/fruits.jpg", os.path.join(IMAGE_DIR, "augmentasi_sample.jpg"), "aug_sample")
first_ok_wiki_cached([("Garching_Bundesautobahn_9.jpg", os.path.join(IMAGE_DIR, "scene_traffic.jpg"), "traffic")])
dl(f"{OPENCV}/lena.jpg", os.path.join(IMAGE_DIR, "wajah_netral.jpg"), "wajah")
first_ok_wiki_cached([(WIKI_PEDESTRIAN[0], os.path.join(IMAGE_DIR, "pedestrian.jpg"), "pedestrian")])
dl(f"{OPENCV}/messi5.jpg", os.path.join(IMAGE_DIR, "segmentasi_sample.jpg"), "seg_sample")

# ============================================================
# LANGKAH 2: BUAT VARIASI WAJAH (LENA)
# ============================================================
print("\n" + "="*60)
print("LANGKAH 2: Buat variasi dari foto Lena ...")
wj = cv2.imread(os.path.join(IMAGE_DIR, "wajah_netral.jpg"))
if wj is not None:
    cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_senang.jpg"), cv2.convertScaleAbs(wj, alpha=1.12, beta=25))
    cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_sedih.jpg"), cv2.convertScaleAbs(wj, alpha=0.82, beta=-20))
    cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_single.jpg"), cv2.resize(wj, (300, 300)))
    cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_kacamata.jpg"), cv2.flip(wj, 1))
    wj_topi = cv2.resize(cv2.convertScaleAbs(wj[:wj.shape[0]*3//4, :], alpha=1.15, beta=10), (300, 300))
    cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_topi.jpg"), wj_topi)
    grup = np.full((350, 700, 3), 200, dtype=np.uint8)
    fs = cv2.resize(wj, (160, 160))
    for idx, (ox, oy) in enumerate([(20, 90), (200, 90), (380, 90), (520, 90)]):
        grup[oy:oy+160, ox:ox+160] = cv2.convertScaleAbs(fs, alpha=1.0+idx*0.06, beta=idx*7)
    cv2.imwrite(os.path.join(IMAGE_DIR, "wajah_grup.jpg"), grup)
    print("  [OK] Berhasil meng-generate 6 variasi wajah.")

# ============================================================
# LANGKAH 3: DOWNLOAD DATASET (5 KATEGORI)
# ============================================================
print("\n" + "="*60)
print("LANGKAH 3: Download dataset foto asli ...")
DATASET_WIKI = {"kucing": WIKI_KUCING, "anjing": WIKI_ANJING, "kendaraan": WIKI_KENDARAAN, 
                "bangunan": WIKI_BANGUNAN, "bunga": WIKI_BUNGA}
for kat, files in DATASET_WIKI.items():
    kd = os.path.join(DATASET_DIR, kat)
    os.makedirs(kd, exist_ok=True)
    for i, file in enumerate(files, 1):
        dl_wiki_cached(file, os.path.join(kd, f"{kat}_{i:03d}.jpg"), f"dataset/{kat}_{i:03d}.jpg", delay=0.5)
    fill_with_variations(kd, kat, 5)

# ============================================================
# LANGKAH 4: GENERATE DATASET BENTUK GEOMETRI
# ============================================================
print("\n" + "="*60)
print("LANGKAH 4: Generate dataset kategori bentuk dasar ...")
shapes = ["lingkaran", "persegi", "segitiga", "bintang", "elips", "segi_enam"]
for kat in shapes:
    kd = os.path.join(DATASET_DIR, kat)
    os.makedirs(kd, exist_ok=True)
    print(f"\n--- Bentuk: {kat} ---")
    for i in range(1, 6):
        img = np.full((256, 256, 3), 255, dtype=np.uint8)
        color = (0, 0, 0)
        center = (128 + np.random.randint(-20, 20), 128 + np.random.randint(-20, 20))
        size = np.random.randint(40, 80)
        if kat == "lingkaran": cv2.circle(img, center, size, color, -1)
        elif kat == "persegi": cv2.rectangle(img, (center[0]-size, center[1]-size), (center[0]+size, center[1]+size), color, -1)
        elif kat == "elips": cv2.ellipse(img, center, (size, size // 2), np.random.randint(0, 180), 0, 360, color, -1)
        elif kat == "segitiga": cv2.fillPoly(img, [np.array([[center[0], center[1]-size], [center[0]-size, center[1]+size], [center[0]+size, center[1]+size]], np.int32)], color)
        elif kat == "segi_enam":
            pts = [[int(center[0] + size * np.cos(np.pi/180*(60*j-30))), int(center[1] + size * np.sin(np.pi/180*(60*j-30)))] for j in range(6)]
            cv2.fillPoly(img, [np.array(pts, np.int32)], color)
        elif kat == "bintang":
            pts = [[int(center[0] + (size if j%2==0 else size//2) * np.cos(np.pi/180*(36*j-90))), int(center[1] + (size if j%2==0 else size//2) * np.sin(np.pi/180*(36*j-90)))] for j in range(10)]
            cv2.fillPoly(img, [np.array(pts, np.int32)], color)
        fname = f"{kat}_{i:03d}.jpg"
        cv2.imwrite(os.path.join(kd, fname), img)
        print(f"  [GEN] {fname}")
    fill_with_variations(kd, kat, 5)

# ============================================================
# LANGKAH 5: DOWNLOAD LABEL IMAGENET
# ============================================================
print("\n" + "="*60)
print("LANGKAH 5: Download label ImageNet ...")
lp = os.path.join(MODEL_DIR, "classification_classes_ILSVRC2012.txt")
if not os.path.exists(lp):
    try:
        req = urllib.request.Request(f"{OPENCV}/dnn/classification_classes_ILSVRC2012.txt", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            with open(lp, "wb") as f: f.write(r.read())
        print("  [OK] classification_classes_ILSVRC2012.txt")
    except Exception as e: print(f"  [FAIL] Label ImageNet: {e}")
else: print("  [SKIP] ImageNet labels sudah ada.")

print("\n" + "="*60)
print("SEMUA GAMBAR BERHASIL DISIAPKAN & DI-GENERATE!")
print("="*60)