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