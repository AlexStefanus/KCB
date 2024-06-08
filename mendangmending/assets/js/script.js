function goToProduct(productId) {
    window.location.href = 'product.php?id=' + productId;
}

function updateSort() {
    var sortOrder = document.querySelector('select[name="sortOrder"]').value;
    var search = document.querySelector('input[name="search"]').value;
    var category = getCurrentCategory();
    var url = 'search.php?category=' + category + '&search=' + search + '&sortOrder=' + sortOrder;
    window.location.href = url;
}

function searchProducts(query) {
    var category = getCurrentCategory();
    var sortOrder = document.querySelector('select[name="sortOrder"]').value;
    var url = 'search.php?category=' + category + '&search=' + query + '&sortOrder=' + sortOrder;

    fetch(url)
        .then(response => response.text())
        .then(html => {
            var parser = new DOMParser();
            var doc = parser.parseFromString(html, 'text/html');
            var productList = doc.getElementById('product-list');
            document.getElementById('product-list').innerHTML = productList.innerHTML;
        });
}

function getCurrentCategory() {
    var urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('category') || '';
}