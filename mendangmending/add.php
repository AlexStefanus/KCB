<!DOCTYPE html>
<html>
<head>
    <title>Tambah Produk - MendangMending.com</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<?php include 'header.php'; ?>
    <main>
        <h2>Tambah Produk</h2>
        <form action="submit.php" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="category">Kategori:</label>
                <select name="category" id="category" required>
                    <option value="">Pilih Kategori</option>
                    <option value="laptop">Laptop</option>
                    <option value="smartphone">Smartphone</option>
                    <option value="keyboard">Keyboard</option>
                    <option value="mouse">Mouse</option>
                    <option value="audio">Audio</option>
                </select>
            </div>
            <div class="form-group">
                <label for="image">Gambar Produk:</label>
                <input type="file" name="image" id="image" required>
            </div>
            <div class="form-group">
                <label for="title">Judul Produk:</label>
                <input type="text" name="title" id="title" required>
            </div>
            <div class="form-group">
                <label for="price">Harga:</label>
                <input type="number" name="price" id="price" min="0" step="0.01" required>
            </div>
            <div class="form-group">
                <label for="description">Deskripsi:</label>
                <textarea name="description" id="description" rows="5" required></textarea>
            </div>
            <button type="submit">Tambah Produk</button>
        </form>
    </main>
</body>
</html>