# Şahmat fiqurlarının əsas sinifi
class ŞahmatFiquru:
    def __init__(self, ad):
        self.ad = ad  # Fiqurun adını saxlayır
    
    # Ümumi bir metod, alt siniflər bunu özəlləşdirə bilər
    def dəyər(self):
        raise NotImplementedError("Bu metod alt siniflərdə müəyyən edilməlidir.")

# Şah fiquru
class Şah(ŞahmatFiquru):
    def __init__(self):
        super().__init__("Şah")  # Əsas sinifin konstruktorunu çağırır
    
    def dəyər(self):
        print("Şahın dəyəri yoxdur, çünki o tutulmur.")

# Vezir fiquru
class Vezir(ŞahmatFiquru):
    def __init__(self):
        super().__init__("Vezir")  # Əsas sinifin konstruktorunu çağırır
    
    def dəyər(self):
        print("Vezirin dəyəri 9 xaldır.")

# Top fiquru
class Top(ŞahmatFiquru):
    def __init__(self):
        super().__init__("Top")  # Əsas sinifin konstruktorunu çağırır
    
    def dəyər(self):
        print("Topun dəyəri 5 xaldır.")

# Fil fiquru
class Fil(ŞahmatFiquru):
    def __init__(self):
        super().__init__("Fil")  # Əsas sinifin konstruktorunu çağırır
    
    def dəyər(self):
        print("Filin dəyəri 3 xaldır.")

# At fiquru
class At(ŞahmatFiquru):
    def __init__(self):
        super().__init__("At")  # Əsas sinifin konstruktorunu çağırır
    
    def dəyər(self):
        print("Atın dəyəri 3 xaldır.")

# Piyada fiquru
class Piyada(ŞahmatFiquru):
    def __init__(self):
        super().__init__("Piyada")  # Əsas sinifin konstruktorunu çağırır
    
    def dəyər(self):
        print("Piyadanın dəyəri 1 xaldır.")

# Fiqurları siyahı şəklində yaradın
fiqurlar = [Şah(), Vezir(), Top(), Fil(), At(), Piyada()]

# Bütün fiqurların adlarını və dəyərlərini göstər
for fiqur in fiqurlar:
    print(f"{fiqur.ad}: ", end="")
    fiqur.dəyər()  # Hər bir fiqurun dəyərini göstər
