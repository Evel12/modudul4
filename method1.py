class HitungVokal:
    def __init__(self, teks):
        self.teks = teks

    def hitung_vokal(self):
       
        teks_lower = self.teks.lower()

        
        jumlah_vokal = 0

        
        for karakter in teks_lower:
            
            if karakter in 'aiueo':
                
                jumlah_vokal += 1

        return jumlah_vokal


teks_input = input("Masukkan sebuah teks: ")
hitung_vokal = HitungVokal(teks_input)
jumlah_vokal = hitung_vokal.hitung_vokal()
print("Jumlah huruf vokal dalam teks adalah:", jumlah_vokal)
