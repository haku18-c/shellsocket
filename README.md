# shellsocket
python3 TCP backdoor program ini mampu mengeksekusi komputer server dengan baris perintah yang dikirim dari klien lalu server akan mengeksekusi perintah tersebut dan mengirimkan kembali output kepada client yang terkoneksi

program ini menerima beberapa parameter 
-type
 parameter ini menunjukan program akan beroperasi sebagai server atau client value dari parameter ini adalah "client" atau "server"
 -t
 parameter ini menunjukan host target host yang akan diikat di server(sisi server) atau target host yang akan diakses(sisi client)
 -p
 parameter ini menunjukan target port yang akan diikat di server atau target port yang akan diakses

 contoh penggunaan program
 python shellshock.py -type server -t localhost -p 8888
 python shellshock.py -type client -t localhost -p 8888
