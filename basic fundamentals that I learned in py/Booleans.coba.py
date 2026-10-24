# Fire Detector Simulation 
# Tujuan: Menentukan kapan alarm harus berbunyi

suhu = 800
ada_asap = False
mode_maintance = False 
sensor = True
# 1. Bahaya Terdeteksi jika suhu > 50 ATAU ada asap
bahaya = suhu > 100 or ada_asap

# 2. Alarm berbunyi jika BAHAYA terdeteksi DAN TIDAK dalam mode maintenance
alarm = bahaya and not mode_maintance

# 3. Sensor aktif ketika ada bahaya
sensor_aktif = bahaya and sensor
# 4. SISTEM 
print("===== STATUS SISTEM KEBAKARAN =====")
print(f"Suhu                : {suhu} Celcius")
print(f"Sensor Asap         : {ada_asap}")
print(f"Mode Maintance      : {mode_maintance}")
print(f"Sensor Aktif?       : {sensor}")
print("-----------------------------------")
print(f"Sensor mendeteksi?  : {sensor_aktif}")
print(f"Alarm Berbunyi?     : {alarm}")
print()

# 5. Percabangan Output
if alarm and sensor_aktif:
    print("NYALAKAN SIRINE!! EVAKUASI GEDUNG!")
else: 
    print("Sistem aman / alarm dibekukan.")

