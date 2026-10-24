#menentukan true or false dengan bool
#x = 100
#y = "Nasgor" \


#print(bool(x))
#print(bool(y))

#menetukan true or false dengan if/else
#a = 2000
#b = 9

#if b > a:
    #print("Lebih gede")
#else:
    #print("Lebih kecil pake cik")

#berdasarkan jawaban dari return nya apa...
#def myFunction():
    #return False

#if myFunction():
    #print("Bener woi")
#else:
    #print("salah kocak")


#Contoh nested if di machine learning
accuracy = 0.89
latency_ms = 40

if accuracy >= 0.85:
    print("✅ Tahap 1 Lolos: Akurasi bagus.")
    
    # Hanya dicek jika Tahap 1 Lolos
    if latency_ms <= 50:
        print("✅ Tahap 2 Lolos: Latency aman. Model SIAP DEPLOY!")
    else:
        print("❌ Tahap 2 Gagal: Latency lambat. Tindakan: Lakukan optimasi model.")
        
else:
    print("❌ Tahap 1 Gagal: Akurasi rendah. Tindakan: Lakukan retrain data.")