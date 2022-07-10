let item = 0;
let total = 0;
let apple = 0;
let orange = 0;
let grape = 0;
let watermelon = 0;


function addApples () {
    total = total + 2.00;
    document.getElementById("cost").innerHTML = "Total cost: $" + total;

    apple = apple + 1;
    document.getElementById("apple").innerHTML = apple + " apple";
}

function removeApples () {
    total = total - 2.00;
    document.getElementById("cost").innerHTML = "Total cost: $" + total;

    apple = apple - 1;
    document.getElementById("apple").innerHTML = apple + " apple";
}

function addOranges () {
    total = total + 3.00;
    document.getElementById("cost").innerHTML = "Total cost: $" + total;

    orange = orange + 1;
    document.getElementById("orange").innerHTML = orange + " orange";
}

function removeOranges () {
    total = total - 3.00;
    document.getElementById("cost").innerHTML = "Total cost: $" + total;

    orange = orange - 1;
    document.getElementById("orange").innerHTML = orange + " orange";
}

function addGrapes () {
    total = total + 1.50;
    document.getElementById("cost").innerHTML = "Total cost: $" + total;

    grape = grape + 1;
    document.getElementById("grape").innerHTML = grape + " grape";
}

function removeGrapes () {
    total = total - 1.50;
    document.getElementById("cost").innerHTML = "Total cost: $" + total;

    grape = grape - 1;
    document.getElementById("grape").innerHTML = grape + " grape";
}

function addWatermelons () {
    total = total + 4.00;
    document.getElementById("cost").innerHTML = "Total cost: $" + total;

    watermelon = watermelon + 1;
    document.getElementById("watermelon").innerHTML = watermelon + " watermelon";
}

function removeWatermelons () {
    total = total - 4.00;
    document.getElementById("cost").innerHTML = "Total cost: $" + total;

    watermelon = watermelon - 1;
    document.getElementById("watermelon").innerHTML = watermelon + " watermelon";
}

function addCart () {
    item = item + 1;
    document.getElementById("cart").innerHTML = item + " items inside cart";
}

function removeCart () {
    item = item - 1;
    document.getElementById("cart").innerHTML = item + " items inside cart";
}
