# Numerical Methods for Engineers

Tugas Bab 11 (11.1–11.28)

Nama: Nadya Syahara
NIM: F5512510002
Kelas: Teknik Informatika A

# Daftar Isi

- Problem 11.1 — Thomas Algorithm
- Problem 11.2 — Matrix Inverse dengan LU Decomposition
- Problem 11.3 — Thomas Algorithm
- Problem 11.4 — Verifikasi Cholesky Decomposition
- Problem 11.5 — Cholesky Decomposition
- Problem 11.6 — Cholesky Decomposition
- Problem 11.7 — Cholesky Decomposition
- Problem 11.8 — Gauss-Seidel dengan Overrelaxation
- Problem 11.9 — Gauss-Seidel Method
- Problem 11.10 — Jacobi Iteration
- Problem 11.11 — Gauss-Seidel Method
- Problem 11.12 — Gauss-Seidel dengan Relaksasi
- Problem 11.13 — Gauss-Seidel dengan Overrelaxation
- Problem 11.14 — Analisis Konvergensi Gauss-Seidel
- Problem 11.15 — Analisis Konvergensi Gauss-Seidel
- Problem 11.16 — Matrix Inverse dan Condition Number
- Problem 11.17 — Sistem Persamaan Nonlinier
- Problem 11.18 — Sistem Persamaan Linear Produksi
- Problem 11.19 — Hilbert Matrix Analysis
- Problem 11.20 — Vandermonde Matrix Analysis
- Problem 11.21 — Matrix Augmentation
- Problem 11.22 — Bentuk Matriks, Transpose, dan Inverse
- Problem 11.23 — Comparison of Operation Counts
- Problem 11.24 — Thomas Algorithm Program
- Problem 11.25 — Cholesky Decomposition Program
- Problem 11.26 — Gauss-Seidel Program
- Problem 11.27 — Finite Difference Method
- Problem 11.28 — Pentadiagonal System Solver

# Problem 11.1
Metode:
Thomas Algorithm (Tridiagonal Matrix Algorithm)

File: Soal11_1.py

Hasil:
x1 = 173.750000
x2 = 245.000000
x3 = 253.750000

Kesimpulan:
Metode Thomas menyelesaikan sistem tridiagonal secara efisien dengan
forward elimination dan back substitution tanpa melakukan eliminasi
Gauss penuh.

# Problem 11.2
Metode:
Matrix inverse menggunakan LU decomposition dan unit vectors.

Langkah:
1. Gunakan matriks L dan U dari Example 11.1.
2. Bentuk empat unit vector:
   e1, e2, e3, e4.
3. Selesaikan:
   L y = e_i
   dengan forward substitution.
4. Selesaikan:
   U x = y
   dengan back substitution.
5. Setiap solusi x menjadi kolom ke-i dari A⁻¹.

File: Soal11_2.py

Hasil:
A⁻¹ =
[[0.818697 0.670141 0.548540 0.269006]
 [0.670141 1.367635 1.120895 0.548870]
 [0.548540 1.120895 1.367541 0.669898]
 [0.269006 0.548870 0.669898 0.817996]]

Kesimpulan:
Invers matriks diperoleh menggunakan LU decomposition
tanpa memanggil fungsi inverse bawaan NumPy.

# Problem 11.3
Metode:
Thomas Algorithm (Tridiagonal Matrix Algorithm)

File: Soal11_3.py

Sistem Persamaan:
A T = b

dengan:
A =
[[ 2.01475  -0.020875   0          0       ]
 [-0.020875  2.01475  -0.020875   0       ]
 [ 0        -0.020875  2.01475  -0.020875]
 [ 0         0        -0.020875  2.01475 ]]

b = [4.175, 0, 0, 2.0875]^T

Hasil:
T1 = 2.072503
T2 = 0.116558
T3 = 0.120335
T4 = 1.041246

Kesimpulan:
Thomas Algorithm menyelesaikan sistem tridiagonal secara efisien melalui proses forward elimination dan back substitution tanpa
perlu melakukan eliminasi Gauss penuh.

# Problem 11.4
Metode:
Verifikasi Cholesky Decomposition

File: Soal11_4.py

Persamaan:
A = L L^T

Hasil:
L L^T =
[[  6.0001   15.0000   55.0010]
 [ 15.0000   54.9997  224.9983]
 [ 55.0010  224.9983  978.9947]]

Kesimpulan:
Hasil perkalian L dan L^T menghasilkan matriks yang sangat mendekati matriks A pada Example 11.2. Dengan demikian, dekomposisi Cholesky yang diperoleh valid.

# Problem 11.5
Metode:
Cholesky Decomposition

File: Soal11_5.py

Langkah:
1. Dekomposisi matriks A menjadi:
   A = LLᵀ
2. Selesaikan:
   Ly = b
   menggunakan forward substitution.
3. Selesaikan:
   Lᵀa = y
   menggunakan back substitution.

Hasil:
a0 = 2.478571
a1 = 2.359286
a2 = 1.860714

Kesimpulan:
Metode Cholesky berhasil digunakan untuk menyelesaikan sistem persamaan linear simetris positif definit.

# Problem 11.6
Metode:
Cholesky Decomposition

File: Soal11_6.py

Matriks:
A =
[[ 8  20  15 ]
 [20  80  50 ]
 [15  50  60 ]]

b = [50, 250, 100]^T

Matriks Cholesky:
L =
[[2.828427 0.       0.      ]
 [7.071068 5.477226 0.      ]
 [5.303301 2.282177 5.163978]]

Hasil:
x1 = 4.038760
x2 = 2.131783
x3 = -1.046512

Kesimpulan:
Matriks berhasil didekomposisi menggunakan metode Cholesky dan solusi sistem persamaan diperoleh melalui forward substitution dan back substitution.

# Problem 11.7

Metode:
Cholesky Decomposition

File: Soal11_7.py

Matriks:
A =
[[ 9  0  0 ]
 [ 0 25  0 ]
 [ 0  0  4 ]]

Matriks Cholesky:
L =
[[3. 0. 0.]
 [0. 5. 0.]
 [0. 0. 2.]]

Hasil:
A = LLᵀ

Kesimpulan:
Karena matriks A merupakan matriks diagonal dengan elemen positif, maka matriks Cholesky diperoleh dengan mengambil akar kuadrat dari setiap elemen diagonal. Hasil ini konsisten dengan Persamaan (11.3)dan (11.4), karena semua elemen di luar diagonal bernilai nol.

# Problem 11.8

Metode:
Gauss-Seidel Method dengan Overrelaxation (λ = 1.2)

File: Soal11_8.py

Parameter:
Stopping criterion:
εs = 5%

Relaxation factor:
λ = 1.2

Hasil:
x1 = 173.996
x2 = 245.685
x3 = 253.592
Iterasi = 6

Kesimpulan:
Metode Gauss-Seidel dengan overrelaxation berhasil mencapai konvergensi dalam 6 iterasi. Nilai yang diperoleh sangat dekat dengan solusi eksak dari Problem 11.1.

# Problem 11.9

Metode:
Gauss-Seidel Method

File: Soal11_9.py

Parameter:

Stopping criterion:
εs = 5%

Hasil:
c1 = 307.087
c2 = 228.656
c3 = 317.593
Iterasi = 4

Kesimpulan:
Metode Gauss-Seidel berhasil menemukan konsentrasi pada ketiga reaktor dalam 4 iterasi dengan toleransi error 5%.

# Problem 11.10

Metode:
Jacobi Iteration

File: Soal11_10.py

Parameter:

Stopping criterion:
εs = 5%

Hasil:
c1 = 315.285
c2 = 219.066
c3 = 315.621
Iterasi = 4

Kesimpulan:
Metode Jacobi berhasil mencapai konvergensi dengan toleransi 5%. Dibandingkan Gauss-Seidel pada Problem 11.9, Jacobi membutuhkan lebih banyak iterasi karena tidak menggunakan nilai terbaru dalam perhitungannya.

# Problem 11.11

Metode:
Gauss-Seidel Method

File: Soal11_11.py

Parameter:

Stopping criterion:
εs = 5%

Hasil:
x1 = 0.500
x2 = 8.000
x3 = -6.000
Iterasi = 5

Kesimpulan:
Metode Gauss-Seidel berhasil mencapai konvergensi dan menghasilkan solusi yang memenuhi sistem persamaan dengan toleransi error 5%.

# Problem 11.12

Metode:
Gauss-Seidel Method

File: Soal11_12.py

Parameter:

Tolerance:
εs = 5%

Relaxation factor:
λ = 0.95

Hasil Tanpa Relaksasi:
x1 ≈ 3.000
x2 ≈ 0.500
x3 ≈ 4.042

Hasil Dengan Relaksasi (lambda = 0.95):
x1 ≈ 3.000
x2 ≈ 0.500
x3 ≈ 4.042

Kesimpulan:
Persamaan perlu disusun ulang agar dominan diagonal. Metode Gauss-Seidel konvergen baik dengan maupun tanpa relaksasi. Nilai λ = 0.95 memberikan underrelaxation yang sedikit memperlambat konvergensi.

# Problem 11.13

Metode:
Gauss-Seidel Method

File: Soal11_13.py

Parameter:

Tolerance:
εs = 5%

Relaxation factor:
λ = 1.2

Hasil Tanpa Relaksasi:
x1 ≈ 4.000
x2 ≈ 8.000
x3 ≈ -2.000

Hasil Dengan Relaksasi (λ/lambda = 1.2):
x1 ≈ 4.000
x2 ≈ 8.000
x3 ≈ -2.000

Kesimpulan:
Persamaan disusun ulang agar lebih dominan diagonal.Metode Gauss-Seidel berhasil konvergen baik tanpa maupun dengan overrelaxation. Nilai λ = 1.2 mempercepat proses menuju solusi.

# Problem 11.14

Metode:
Analisis Konvergensi Gauss-Seidel

Pembahasan:
Pada Gambar 11.5, syarat konvergensi Gauss-Seidel adalah:
|m| < 1

Untuk kasus:
m₁ = 1
m₂ = -1

nilai mutlak slope sama dengan 1 sehingga sistem berada tepat pada batas konvergensi.

Hasil:
Metode Gauss-Seidel tidak konvergen menuju solusi.

Untuk slope = 1, iterasi cenderung tetap pada jarak yang sama terhadap solusi.

Untuk slope = -1, iterasi berosilasi (bolak-balik) di sekitar solusi.

Kesimpulan:
Karena |m| = 1, metode berada pada kondisi netral dan tidak menghasilkan konvergensi menuju solusi.

# Problem 11.15

Metode:
Analisis Konvergensi Gauss-Seidel

File: Soal11_15.py

Hasil:

Set One:
Masih dapat dibuat konvergen.

Set Two:
Tidak memenuhi dominasi diagonal dan tidak konvergen.

Set Three:
Tidak memenuhi dominasi diagonal dan tidak konvergen.

Kesimpulan:
Set Two dan Set Three tidak dapat diselesaikan secara andal menggunakan metode iteratif Gauss-Seidel karena tidak memenuhi syarat dominasi diagonal.

# Problem 11.16

Metode:
- Matrix Inverse
- Row-Sum Norm
- Condition Number

File: Soal11_16.py

Hasil (a):
Solution:
[1.0, 1.0, 1.0]

Condition Number:
750

Residual:
[0.0, 0.0, 0.0]

Hasil (b):
Solution:
[1.114583, 0.656250, 1.343750, 0.885417]

Condition Number:
1.4186 × 10^17

Residual:
[0.0, 0.0, 0.0, 0.0]

Kesimpulan:
Pada bagian (a), solusi yang diperoleh sesuai dengan solusi teoritis dan condition number relatif kecil sehingga sistem stabil.

Pada bagian (b), condition number sangat besar (≈ 10^17) yang menunjukkan matriks sangat sensitif terhadap kesalahan pembulatan. Akibatnya solusi numerik yang diperoleh berbeda dari solusi teoritis[1, 1, 1, 1], meskipun residual tetap nol. Hal ini menunjukkan bahwa matriks tersebut bersifat ill-conditioned.

# Problem 11.17

Metode:
SciPy fsolve

File: Soal11_17.py

Persamaan:
f(x,y) = 4 - y - 2x²
g(x,y) = 8 - y² - 4x

Hasil Part (a):
Solusi 1:
x = -2
y = -4

Solusi 2:
x = 1
y = 2

Hasil Part (b):
Initial guess yang menuju solusi (-2,-4):
(-6,-6)
(-4,-4)
(-2,-2)
(-1,-1)

Initial guess yang menuju solusi (1,2):
(0,0)
(1,1)
(2,2)
(4,4)
(6,6)

Kesimpulan:
Sistem memiliki dua solusi real yaitu (-2,-4) dan (1,2).

Initial guess negatif cenderung konvergen ke solusi (-2,-4), sedangkan initial guess nol atau positif cenderung konvergen ke solusi (1,2).

# Problem 11.18

Metode:
NumPy Linear Algebra Solver

File: Soal11_18.py

Sistem Persamaan:
4x1 + 3x2 + 2x3 = 960
x1 + 3x2 + x3 = 510
2x1 + x2 + 3x3 = 610

dengan:
x1 = jumlah transistor
x2 = jumlah resistor
x3 = jumlah computer chip

Hasil:
Transistors = 120
Resistors = 100
Computer Chips = 90

Kesimpulan:
Dengan persediaan 960 unit copper, 510 unit zinc, dan 610 unit glass, perusahaan dapat memproduksi:
- 120 transistor
- 100 resistor
- 90 computer chip
yang tepat menghabiskan seluruh material yang tersedia.

# Problem 11.19

Metode:
Hilbert Matrix Analysis

File: Soal11_19.py

Matriks:
Hilbert Matrix 10 × 10

Hasil:
Spectral Condition Number:
1.602493 × 10^13

Expected Digits Lost:
13.20 digit

Solusi:
x ≈
[1.00000000,
 1.00000012,
 0.99999759,
 1.00002162,
 0.99989806,
 1.00027756,
 0.99954829,
 1.00043347,
 0.99977382,
 1.00004947]

Error Maksimum:
≈ 4.33 × 10^-4

Kesimpulan:
Hilbert Matrix 10×10 memiliki condition number yang sangat besar (≈ 10^13), sehingga sekitar 13 digit presisi dapat hilang akibat error pembulatan.Meskipun solusi teoritis adalah semua x = 1, solusi numerik menunjukkan penyimpangan kecil karena matriks sangat ill-conditioned.

# Problem 11.20

Metode:
Vandermonde Matrix Analysis

File: Soal11_20.py

Matriks:
Vandermonde Matrix 6 × 6

dengan:
x = [4, 2, 7, 10, 3, 5]

Hasil:
Spectral Condition Number:
1.4491732 × 10^7

Expected Digits Lost:
7.16 digit

Solusi:
x =
[1, 1, 1, 1, 1, 1]

Error Maksimum:
≈ 6.02 × 10^-11

Kesimpulan:
Vandermonde matrix memiliki condition number yang cukup besar (≈ 10^7), sehingga sekitar 7 digit presisi dapat hilang akibat error pembulatan.Meskipun demikian, solusi numerik yang diperoleh masih sangat dekat dengan solusi eksak [1,1,1,1,1,1], dengan error hanya sekitar 10^-11 hingga 10^-14.Dibandingkan dengan Hilbert Matrix pada Problem 11.19, Vandermonde Matrix ini jauh lebih stabil secara numerik.

# Problem 11.21

Metode:
Matrix Augmentation

File: Soal11_21.py

MATLAB Command:
Aug = [A eye(size(A))]

Hasil:
Perintah tersebut menghasilkan matriks augmentasi:
[A | I]

di mana:
- A = matriks asli
- I = matriks identitas dengan ukuran yang sama

Contoh:
Jika:
A =
[[1 2]
 [3 4]]

maka:
Aug =
[[1 2 1 0]
 [3 4 0 1]]

Kesimpulan:
Matriks augmentasi [A|I] dapat dibuat dengan menggabungkan matriks A dan matriks identitas I secara horizontal menggunakan perintah MATLAB: 
Aug = [A eye(size(A))]

Matriks augmentasi ini sering digunakan dalam metode eliminasi Gauss-Jordan untuk menghitung invers matriks dan menyelesaikan sistem persamaan linear.

# Problem 11.22

Metode:
NumPy Linear Algebra

File: Soal11_22.py

Bentuk Matriks:
Ax = b

A =
[[ 0   7  -5]
 [ 0   4   7]
 [-4   3  -7]]

b =
[-50
 -30
  40]

Hasil:
Solusi:
x1 = -15.181159
x2 = -7.246377
x3 = -0.144928
Transpose:
Aᵀ =
[[ 0   0  -4]
 [ 7   4   3]
 [-5   7  -7]]

Inverse:
A⁻¹ =
[[ 0.177536 -0.123188 -0.250000]
 [ 0.101449  0.072464  0.000000]
 [-0.057971  0.101449  0.000000]]

Kesimpulan:
Sistem persamaan berhasil ditulis dalam bentuk matriks dan diselesaikan menggunakan metode aljabar linear. Selain solusi variabel, diperoleh pula transpose dan inverse dari matriks koefisien sesuai dengan yang diminta pada soal.

# Problem 11.23

Metode:
Comparison of Operation Counts

File: Soal11_23.py

Persamaan:
Gaussian Elimination:
Operations ≈ (2/3)n³

Thomas Algorithm:
Operations = 8n − 7

Hasil:
Program menghitung jumlah operasi yang diperlukan oleh Gaussian Elimination dan Thomas Algorithm untuk ukuran sistem n = 2 sampai n = 20.

Contoh hasil yang diperoleh:
| n | Gaussian Elimination | Thomas Algorithm |
|---|---------------------:|-----------------:|
| 2 | 5.33 | 9 |
| 5 | 83.33 | 33 |
| 10 | 666.67 | 73 |
| 15 | 2250.00 | 113 |
| 20 | 5333.33 | 153 |

Analisis Grafik:
Grafik menunjukkan bahwa jumlah operasi Gaussian Elimination meningkat sangat cepat seiring bertambahnya ukuran sistem. Kurva Gaussian berbentuk kubik karena kompleksitasnya adalah: O(n³).Sebaliknya, Thomas Algorithm hanya meningkat secara linear: O(n).

Pada n = 20, Gaussian Elimination membutuhkan sekitar 5333 operasi, sedangkan Thomas Algorithm hanya membutuhkan sekitar 153 operasi.

Perbedaan ini menunjukkan bahwa Thomas Algorithm jauh lebih efisien untuk sistem persamaan tridiagonal.

Kesimpulan:
Thomas Algorithm memiliki kompleksitas O(n), sedangkan Gaussian Elimination memiliki kompleksitas O(n³).

Berdasarkan hasil perhitungan dan grafik, Thomas Algorithm memerlukan jauh lebih sedikit operasi dibandingkan Gaussian Elimination. Semakin besar ukuran sistem, semakin besar pula keunggulan Thomas Algorithm. Oleh karena itu, Thomas Algorithm lebih cocok digunakan untuk menyelesaikan sistem persamaan tridiagonal berukuran besar.

# Problem 11.24

Metode:
Thomas Algorithm

File: Soal11_24.py

Data Uji:
Sistem tridiagonal dari Problem 11.1:
0.8x1 − 0.4x2 = 41
−0.4x1 + 0.8x2 − 0.4x3 = 25
−0.4x2 + 0.8x3 = 105

Hasil:
x1 = 173.750000
x2 = 245.000000
x3 = 253.750000

Analisis:
Program menggunakan dua tahap utama, yaitu:
1. Forward Elimination
   - Menghilangkan elemen sub-diagonal.
   - Memodifikasi diagonal utama dan vektor ruas kanan.
2. Back Substitution
   - Menghitung solusi dimulai dari variabel terakhir.
   - Dilanjutkan hingga variabel pertama.

Metode Thomas merupakan penyederhanaan eliminasi Gauss yang khusus digunakan untuk matriks tridiagonal sehingga lebih efisien dalam penggunaan operasi dan memori.

Kesimpulan:
Program Thomas Algorithm berhasil menyelesaikan sistem persamaan tridiagonal dari Problem 11.1.

Hasil yang diperoleh adalah:
x1 = 173.75
x2 = 245.00
x3 = 253.75

Nilai tersebut memenuhi seluruh persamaan sehingga
implementasi Thomas Algorithm telah berjalan dengan benar.

# Problem 11.25

Metode:
Cholesky Decomposition

File: Soal11_25.py

Data Uji:
A =
[[  6   15   55]
 [ 15   55  225]
 [ 55  225  979]]

b =
[152.6
 585.6
2488.8]

Hasil:
Matriks Cholesky (L):
[[ 2.449490  0.000000  0.000000]
 [ 6.123724  4.183300  0.000000]
 [22.453656 20.916501  6.110101]]

Solusi:
a0 = 2.478571
a1 = 2.359286
a2 = 1.860714

Analisis:
Program melakukan dekomposisi matriks menjadi:
A = LLᵀ

Kemudian sistem diselesaikan melalui:
1. Forward Substitution
2. Back Substitution

Metode Cholesky sangat efisien untuk matriks simetris positif definit karena hanya memerlukan setengah jumlah operasi dibandingkan eliminasi Gauss.

Kesimpulan:
Program Cholesky Decomposition berhasil dibuat dan diuji menggunakan data dari Example 11.2. Hasil yang diperoleh sesuai dengan solusi sistem, sehingga implementasi metode Cholesky telah berjalan dengan benar.

# Problem 11.26

Metode:
Gauss-Seidel Method

File: Soal11_26.py

Sistem Persamaan:
15c1 − 3c2 − c3 = 3800
−3c1 + 18c2 − 6c3 = 1200
−4c1 − c2 + 12c3 = 2350

Toleransi:
εs = 5%

Hasil:
Iterations = 4

c1 = 319.325
c2 = 226.540
c3 = 321.153

Analisis:
Metode Gauss-Seidel menggunakan nilai terbaru yang dihitung pada iterasi yang sama sehingga konvergensinya lebih cepat dibandingkan metode Jacobi.
Pada toleransi 5%, solusi telah memenuhi kriteria konvergensi setelah 4 iterasi.

Kesimpulan:
Metode Gauss-Seidel berhasil digunakan untuk menyelesaikan sistem persamaan linear yang diberikan.

Dengan toleransi εs = 5%, diperoleh: 
c1 = 319.325
c2 = 226.540
c3 = 321.153

Hasil tersebut telah memenuhi syarat konvergensi yang ditentukan.

# Problem 11.27

Metode:
Finite Difference Method

File: Soal11_27.py

Persamaan:
0 = D(d²c/dx²) − U(dc/dx) − kc

dengan:
D = 2
U = 1
k = 0.2
Δx = 2

Boundary Conditions:
c(0) = 80
c(10) = 20

Hasil:
Distribusi konsentrasi yang diperoleh:
| x | c |
|---|------:|
| 0 | 80.0000 |
| 2 | 59.1013 |
| 4 | 43.6860 |
| 6 | 32.3892 |
| 8 | 24.4099 |
| 10 | 20.0000 |

Analisis:
Persamaan diferensial diubah menjadi sistem persamaan linear menggunakan metode finite difference.

Hasil menunjukkan bahwa konsentrasi menurun secara bertahap dari 80 pada x = 0 menjadi 20 pada x = 10.

Grafik concentration versus distance memperlihatkan profil konsentrasi yang terus menurun sepanjang kanal akibat proses difusi, konveksi, dan peluruhan kimia.

Kesimpulan:
Metode finite difference berhasil digunakan untuk menyelesaikan persamaan diferensial yang diberikan.

Distribusi konsentrasi menunjukkan penurunan dari 80 menjadi 20 sepanjang kanal, dan hasilnya berhasil divisualisasikan dalam grafik concentration versus distance sesuai dengan yang diminta pada soal.

# Problem 11.28

Metode:
Pentadiagonal System Solver

File: Soal11_28.py

Sistem Persamaan:
[ 8  -2  -1   0   0 ]
[-2   9  -4  -1   0 ]
[-1  -3   7  -1  -2 ]
[ 0  -4  -2  12  -5 ]
[ 0   0  -7  -3  15 ]

x=
[5
 2
 0
 1
 5]

Hasil:
x1 = 1.000000
x2 = 1.000000
x3 = 1.000000
x4 = 1.000000
x5 = 1.000000

Analisis:
Matriks koefisien memiliki struktur pentadiagonal,yaitu hanya lima diagonal yang berisi elemen tak nol.Sistem berhasil diselesaikan menggunakan metode aljabar linear dan menghasilkan solusi yang sangat sederhana, yaitu seluruh variabel bernilai 1.Verifikasi menunjukkan bahwa solusi tersebut memenuhi seluruh persamaan pada sistem.

Kesimpulan:
Sistem pentadiagonal berhasil diselesaikan dan diperoleh:
x1 = x2 = x3 = x4 = x5 = 1

Hasil tersebut memenuhi seluruh persamaan yang diberikan sehingga solusi dinyatakan benar.

# Kesimpulan Akhir

Bab 11 membahas berbagai metode penyelesaian sistem persamaan linear dan nonlinier, termasuk Thomas Algorithm, Cholesky Decomposition, Gauss-Seidel, Jacobi Iteration, analisis condition number, serta aplikasi finite difference.

Seluruh problem 11.1–11.28 telah diimplementasikan menggunakan Python dan diverifikasi melalui hasil numerik yang sesuai dengan teori metode numerik.