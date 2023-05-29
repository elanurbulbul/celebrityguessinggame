import random
import time
import string
from PIL import Image, ImageFilter

celebrities = [
    {"file": "image1.jpg", "name": "HANDE ERCEL"},
    {"file": "image2.jpg", "name": "KEREM BURSIN"},
    {"file": "image3.jpg", "name": "CAGATAY ULUSOY"},
    {"file": "image4.jpg", "name": "MERT RAMAZAN DEMIR"},
    {"file": "image5.jpg", "name": "KIVANC TATLITUG"},
    {"file": "image6.jpg", "name": "SERENAY SARIKAYA"},
    {"file": "image7.jpg", "name": "BURAK DENIZ"},
    {"file": "image8.jpg", "name": "GOKCE BAHADIR"},
    {"file": "image9.jpg", "name": "SELAHATTIN PASALI"},
    {"file": "image10.jpg", "name": "FUNDA ERYIGIT"},
    {"file": "image11.jpg", "name": "ALI ATAY"},
    {"file": "image12.jpg", "name": "HAZAL KAYA"},
    {"file": "image13.jpg", "name": "GULSE BIRSEL"},
    {"file": "image14.jpg", "name": "SEBNEM BOZOKLU"},
    {"file": "image15.jpg", "name": "BINNUR KAYA"},
    {"file": "image16.jpg", "name": "EDA ECE"},
    {"file": "image17.jpg", "name": "BIRKAN SOKULLU"},
    {"file": "image18.jpg", "name": "ALP NAVRUZ"},
    {"file": "image19.jpg", "name": "CAGLAR ERTUGRUL"},
    {"file": "image20.jpg", "name": "FAHRIYE EVCEN"},
   
]


def choose_random_celebrity():
    return random.choice(celebrities)

def blur_image(image):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=15))
    return blurred_image


def play_game():
    
    remaining_attempts = 3
    score = 0
    print("ÜNLÜYÜ BULMA OYUNUNA HOŞGELDİNİZ!")
    print("Tahmin etmek için harf veya tam isim girin.")

    while True:
        celebrity = choose_random_celebrity()
        image_path = celebrity["file"]
        celebrity_name = celebrity["name"].upper()
        hidden_name = ["_" if ch.isalpha() else ch for ch in celebrity_name]
        guessed_letters = []
        
        image = Image.open(image_path)
        blurred_image = blur_image(image)
        blurred_image.show()
        time.sleep(2)
        blurred_image.close()

        while True:
            print("\n", " ".join(hidden_name))
            answer = input("Tahmininizi girin: ").upper()
            
            if answer.isalpha():

                if answer in celebrity_name:
                    
                    for i in range(len(celebrity_name)):
                        if celebrity_name[i] == answer:
                            hidden_name[i] = answer
                            
                    if answer in guessed_letters:
                        print("Bu harfi zaten kullandınız. Lütfen başka bir harf girin.")
                        continue

                    guessed_letters.append(answer) 
     
                    if answer == celebrity_name:
                        score+=10
                        print("Tebrikler, doğru tahmin! Skorunuz:", score)
                        break
                    
                    if "_" not in hidden_name:
                        score+=10
                        print("Tebrikler, doğru tahmin! Puanınız:", score)
                        break
                    else:
                        score +=5
                        print("Doğru harf! Kalan hakkınız:", remaining_attempts)
                else:
                    remaining_attempts -= 1
                    score-=5
                    print("Yanlış harf! Kalan hakkınız:", remaining_attempts)
                    if remaining_attempts == 0:
                        print("Üzgünüm, tahminleriniz tükendi.Oyunu kaybettiniz.")
                        print("Doğru cevap:", celebrity_name)     
                        print("Oyun Skorunuz: ", score)
                        score=0
                        break
          
            elif answer == celebrity_name:
                    score+=10
                    print("Tebrikler, doğru tahmin! Skorunuz:", score)
                    break
            else:
                print("Geçersiz giriş! Sadece harf veya tam isim girin.")
                
        response = input("Devam etmek istiyor musunuz? (E/H): ")
        if response.upper() != "E":
            print("Oyunu bitirdiniz.")
            print("Puanınız:", score)
            break


response = input("Oyunu oynamak istiyor musunuz? (E/H): ")

if response.upper() == "E":
    play_game()
elif response.upper() == "H":
    print("Oyunu oynamak istemediniz.")
else:
    print("Oyunu oynamak için sadece 'E ya da H' harflerini giriniz.")
    
