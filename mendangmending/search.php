<?php
require_once 'functions.php';

$category = isset($_GET['category']) ? $_GET['category'] : null;

// Jika kategori belum dipilih, redirect ke halaman kategori
if (!$category) {
    header('Location: category.php');
    exit;
}

$search = isset($_GET['search']) ? $_GET['search'] : null;
$sortOrder = isset($_GET['sortOrder']) ? $_GET['sortOrder'] : 'asc';

$products = getProducts($category, $search, $sortOrder);
?>
<!DOCTYPE html>
<html>
<head>
    <title>Cari Produk - MendangMending.com</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <script src="assets/js/script.js" defer></script>
</head>
<body>
<?php include 'header.php'; ?>
    <main>
        <div class="search-controls">
            <div class="search-bar">
                <form onsubmit="return false;">
                    <input type="text" name="search" placeholder="Cari produk" value="<?php echo $search; ?>" onkeyup="searchProducts(this.value)">
                </form>
            </div>
            <div class="sort-control">
                <select name="sortOrder" id="sortOrder" onchange="updateSort()">
                    <option value="asc" <?php if ($sortOrder === 'asc') echo 'selected'; ?>>Harga: Rendah ke Tinggi</option>
                    <option value="desc" <?php if ($sortOrder === 'desc') echo 'selected'; ?>>Harga: Tinggi ke Rendah</option>
                </select>
            </div>
        </div>

        <div class="products" id="product-list">
            <?php foreach ($products as $product): ?>
                <div class="product" onclick="goToProduct(<?php echo $product['id']; ?>)">
                    <img src="assets/images/product/<?php echo $product['image']; ?>" alt="<?php echo $product['title']; ?>">
                    <div class="product-details">
                        <h3><?php echo $product['title']; ?></h3>
                        <p>Harga: Rp <?php echo number_format($product['price'], 2, ',', '.'); ?></p>
                    </div>
                </div>
            <?php endforeach; ?>
        </div>
    </main>
</body>
</html>