<?php
require_once 'config.php';

function getProducts($category = null, $search = null, $sortOrder = 'asc') {
    global $conn;

    $sql = "SELECT * FROM products WHERE 1";

    if ($category) {
        $sql .= " AND category = '$category'";
    }

    if ($search) {
        $sql .= " AND (title LIKE '%$search%' OR description LIKE '%$search%')";
    }

    $sql .= " ORDER BY price " . ($sortOrder === 'asc' ? 'ASC' : 'DESC');

    $result = $conn->query($sql);
    $products = [];

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $products[] = $row;
        }
    }

    return $products;
}


function getProduct($id) {
    global $conn;

    $sql = "SELECT * FROM products WHERE id = $id";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        return $result->fetch_assoc();
    }

    return null;
}

function addProduct($category, $title, $price, $image, $description) {
    global $conn;

    $sql = "INSERT INTO products (category, title, price, image, description) VALUES ('$category', '$title', '$price', '$image', '$description')";

    if ($conn->query($sql) === TRUE) {
        return $conn->insert_id;
    }

    return false;
}

function updateProduct($id, $title, $price, $description, $category) {
    global $conn;

    $sql = "UPDATE products SET title = '$title', price = '$price', description = '$description', category = '$category' WHERE id = $id";

    if ($conn->query($sql) === TRUE) {
        return true;
    }

    return false;
}

function deleteProduct($id) {
    global $conn;

    $sql = "DELETE FROM products WHERE id = $id";

    if ($conn->query($sql) === TRUE) {
        return true;
    }

    return false;
}