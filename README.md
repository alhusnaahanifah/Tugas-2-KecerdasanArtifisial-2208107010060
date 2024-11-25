# Tugas-2-KecerdasanArtifisial-2208107010060
**Author : Alhusna Hanifah**

## Project Trash Classification menggunakan CNN

Trash Classification menggunakan CNN adalah sistem berbasis deep learning untuk mengklasifikasikan sampah secara otomatis ke dalam enam kategori: cardboard, glass, metal, paper, plastic, dan trash. Sistem ini memanfaatkan model Convolutional Neural Network (CNN) untuk mengenali gambar sampah yang diunggah oleh pengguna melalui antarmuka berbasis web. Dengan pendekatan ini, pengguna dapat mengelola sampah dengan lebih efisien dan akurat, sekaligus meningkatkan kesadaran akan pentingnya pemilahan sampah untuk mendukung daur ulang dan keberlanjutan lingkungan.


### Dataset
Dataset yang digunakan dalam proyek ini adalah TrashNet Dataset, yang dapat diakses melalui repositori GitHub: TrashNet Dataset. Dataset ini dirancang untuk mengembangkan model klasifikasi sampah berdasarkan kategori yang umum ditemukan. Dataset memiliki ketidakseimbangan data, dengan jumlah gambar kategori Trash lebih sedikit dibanding kategori lainnya.4

Link Dataset : https://github.com/garythung/trashnet/blob/master/data/dataset-resized.zip

### Keterangan 
File Tugas2.ipynb merupakan file yang berisi proses seluruh program klasifikasi, termasuk training model.
File app.py merupakan file UI untuk menjalankan program trash classfication.
Folder dataset-resized merupakan folder tempat dataset berada. 

### Notes 
Setelah beberapa kali mencoba model, model terbaik adalah trashfix_model.h5 
screenshot plot training model dapat dilihat pada file screenshotprosestraining.jpg (berdasarkan trashfix_model.h5)  
screenshot hasil akurasi model dapat dilihat pada file screenshotAkurasi.jpg (berdasarkan trashfix_model.h5)  

