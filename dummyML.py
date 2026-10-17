# Simulasi Training Model ML dengan Early Stopping
loss = 1.0                # Loss awal
threshold = 0.01          # Batas toleransi error (Kondisi Henti)
max_epochs = 1000         # Guard agar tidak infinite loop
epoch = 0

learning_rate = 0.1

while loss > threshold:
    epoch += 1

    # Simulasi pembaharuan bobot & penurunan loss
    loss -= loss * learning_rate

    print(f"Epoch {epoch}: Loss = {loss:.4f}")

    # Safety Check: Cegah perulangan tanpa henti
    if epoch >= max_epochs:
        print("Mencapai batas maksimum epoch! Menghentikan pelatihan.")
        break
else:
    print(f"\nModel berhasil Converge pada Epoch ke-{epoch}!")