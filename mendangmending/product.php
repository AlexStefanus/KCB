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
?>
<!DOCTYPE html>
<html>
<head>
    <title><?php echo $product['title']; ?> - MendangMending.com</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<?php include 'header.php'; ?>
    <main>
        <div class="product-page">
            <img src="assets/images/product/<?php echo $product['image']; ?>" alt="<?php echo $product['title']; ?>">
            <div class="details">
                <h2><?php echo $product['title']; ?></h2>
                <p>Harga: Rp <?php echo number_format($product['price'], 2, ',', '.'); ?></p>
                <h3>Deskripsi</h3>
                <p><?php echo nl2br($product['description']); ?></p>
                <a href="edit.php?id=<?php echo $product['id']; ?>" class="btn btn-primary">Edit Produk</a>
                <a href="delete.php?id=<?php echo $product['id']; ?>" class="btn btn-danger" onclick="return confirm('Apakah Anda yakin ingin menghapus produk ini?')">Hapus Produk</a>
            </div>
        </div>
    </main>
</body>
</html>