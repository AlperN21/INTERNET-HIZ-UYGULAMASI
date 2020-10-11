print(0)

import os


import time

import colorama
from colorama import Fore, Back, Style
colorama.init()
#print("000")
from speedtest import Speedtest

st = Speedtest()


print("İnternet değerleriniz ölçülüyor...")
time.sleep(1)
print("İndirme Hızı", st.download()/1000000, "Mbps")
print("Yükleme hızı ", st.upload()/1000000, "Mbps")
time.sleep(1)
print("Detay Bilgiler", st.get_config())

time.sleep(1)

print("league of legends tr serveri ping değeri ölçülüyor....")

time.sleep(1)

while True:
    def check_ping():
        hostname = "195.175.112.163"
        response = os.system("ping -n 1 " + hostname)
        # and then check the response...
        if response == 0:
            pingstatus = "Network Active"
        else:
            pingstatus = "Network Error"

        return pingstatus


    pingstatus = check_ping()

    time.sleep(5)




