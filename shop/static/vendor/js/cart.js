// static/js/cart.js

document.addEventListener('DOMContentLoaded', function () {
    // Найти все элементы input с типом number внутри корзины
    var quantityInputs = document.querySelectorAll('.cart input[type="number"]');

    // Для каждого input добавить слушатель события ввода
    quantityInputs.forEach(function (input) {
        input.addEventListener('input', function () {
            updateTotalPrice(this);
        });
    });

    // Функция для обновления общей цены
    function updateTotalPrice(input) {
        // Найти родительскую строку tr
        var row = input.closest('tr');

        // Найти элемент с ценой внутри строки
        var priceElement = row.querySelector('td:nth-child(2)');

        // Найти элемент с общей ценой внутри строки
        var totalElement = row.querySelector('td:nth-child(4)');

        // Получить цену продукта и количество из элементов
        var price = parseFloat(priceElement.textContent.replace('$', ''));
        var quantity = parseInt(input.value);

        // Рассчитать и установить новую общую цену
        var total = price * quantity;
        totalElement.textContent = total.toFixed(2) + '$';

        // Обновить общую цену для всех продуктов
        updateOverallTotalPrice();
    }

    // Функция для обновления общей цены для всех продуктов
    function updateOverallTotalPrice() {
        var overallTotal = 0;
        var totalElements = document.querySelectorAll('.cart tbody tr td:nth-child(4)');

        // Суммировать общие цены всех продуктов
        totalElements.forEach(function (totalElement) {
            overallTotal += parseFloat(totalElement.textContent.replace('$', ''));
        });

        // Обновить общую цену в блоке cart-total
        var cartTotalElement = document.querySelector('.cart-total p');
        cartTotalElement.textContent = 'Total: ' + overallTotal.toFixed(2) + '$';
    }
});
