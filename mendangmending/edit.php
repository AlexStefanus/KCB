<?php
require_once 'functions.php';

$id = isset($_GET['id']) ? $_GET['id'] : null;

if (!$id) {
    header('Location: search.php');
    exit;
}

$product = getProduct($id);

if (!$product) {
    header('Location: search.php');
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = $_POST['title'];
    $price = $_POST['price'];
    $description = $_POST['description'];
    $category = $_POST['category'];
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Edit Produk - MendangMending.com</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <?php include 'header.php'; ?>
    <main>
        <h2>Edit Produk</h2>
        <form method="post" action="edit.php?id=<?php echo $id; ?>">
            <div class="form-group">
                <label for="category">Kategori:</label>
                <select name="category" id="category" required>
                    <option value="">Pilih Kategori</option>
                    <option value="laptop" <?php if ($product['category'] === 'laptop') echo 'selected'; ?>>Laptop</option>
                    <option value="smartphone" <?php if ($product['category'] === 'smartphone') echo 'selected'; ?>>Smartphone</option>
                    <option value="keyboard" <?php if ($product['category'] === 'keyboard') echo 'selected'; ?>>Keyboard</option>
                    <option value="mouse" <?php if ($product['category'] === 'mouse') echo 'selected'; ?>>Mouse</option>
                    <option value="audio" <?php if ($product['category'] === 'audio') echo 'selected'; ?>>Audio</option>
                </select>
            </div>
            <div class="form-group">
                <label for="title">Judul Produk:</label>
                <input type="text" name="title" id="title" value="<?php echo $product['title']; ?>" required>
            </div>
            <div class="form-group">
                <label for="price">Harga:</label>
                <input type="number" name="price" id="price" min="0" step="0.01" value="<?php echo $product['price']; ?>" required>
            </div>
            <div class="form-group">
                <label for="description">Deskripsi:</label>
                <textarea name="description" id="description" rows="5" required><?php echo $product['description']; ?></textarea>
            </div>
            <button type="submit">Update Produk</button>
        </form>
    </main>
</body>
</html>