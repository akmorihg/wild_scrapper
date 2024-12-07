function scrap_data(){
    let inputForm = document.getElementById("searchInput");
    let productCards = document.getElementsByClassName("product-card__wrapper");

    console.log(productCards.length);

    let items = [];

    let i = 0;
    for(let productCard of productCards) {
        let productCardMiddleWrapper = productCard.getElementsByClassName("product-card__middle-wrap")[0];

        var brandName = productCard.getElementsByClassName("product-card__brand")[0].innerText;
        
        var mayakDiv = productCardMiddleWrapper.childNodes[0].childNodes[0];

        var mayakData = mayakDiv.childNodes[0].childNodes[0];
        
        var mayakInnerData = mayakData.childNodes[1];

        var productId = mayakInnerData.childNodes[0];
        var restProductCount = mayakInnerData.childNodes[4];

        var productIdText = productId.childNodes[1].childNodes[0].innerText;
        var restProductCountText = restProductCount.childNodes[1].childNodes[0].innerText.replace(String.fromCharCode(160), "").replace("шт.", "");

        var productIdInt = parseInt(productIdText);
        var restProductCountInt = parseInt(restProductCountText)

        var item_dict = {};
        item_dict["item_name"] = inputForm.value.trim();
        item_dict["item_id"] = productIdInt;
        item_dict["brand_name"] = brandName;
        item_dict["rest_count"] = restProductCountInt;

        items[i] = item_dict;
        i += 1;
    }

    let items_dict = {};
    items_dict["items"] = items;

    // var mapObj = Object.fromEntries(items_dict);
    let jsonString = JSON.stringify(items_dict);

    console.log(jsonString);

    let BASE_URL = "http://195.49.210.199:8000/";

    let xhr = new XMLHttpRequest();
    xhr.open("POST", BASE_URL + "items/");
    xhr.setRequestHeader('Accept', 'application/json');
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr
    .onload = () => 
    {
        console.log(xhr.responseText);
        window.location.replace(BASE_URL + "excels/");
    };
    xhr.send(jsonString);
}

scrap_data();
