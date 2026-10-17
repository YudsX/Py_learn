distance_mi = 5
is_raining = False
has_bike = True
has_car = True 
has_ride_share_app = True

# 15. distance_mi nilainya falsy (0 / None)
if not distance_mi:
    print(False)

# 16. Jarak <= 1 DAN tidak hujan
elif distance_mi <= 1 and not is_raining:
    print(True)

# 17. Jarak <= 1 DAN hujan
elif distance_mi <= 1 and is_raining:
    print(False)

# 18. Jarak antara 1 dan 6, DAN hujan tanpa sepeda
elif distance_mi <= 6 and is_raining and not has_bike:
    print(False)

# 19. Jarak antara 1 dan 6, DAN tidak hujan tanpa sepeda
elif distance_mi <= 6 and not is_raining and not has_bike:
    print(False)

# 20. Jarak antara 1 dan 6, ada sepeda DAN tidak hujan
elif distance_mi <= 6 and has_bike and not is_raining:
    print(True)

# 21. Jarak > 6 DAN ada aplikasi ride share
elif distance_mi > 6 and has_ride_share_app:
    print(True)

# 22. Jarak > 6 DAN ada mobil
elif distance_mi > 6 and has_car:
    print(True)

# 23. Jarak > 6 tapi TIDAK ada mobil DAN TIDAK ada aplikasi ride share
elif distance_mi > 6 and not has_car and not has_ride_share_app:
    print(False)