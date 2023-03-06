// function pierwszaFuncja()
// {
//     document.getElementById("demo").innerHTML = "Ojtam ojtam ! :)";
// }

// function drugiZegar()
// {
//     let dzisiaj = new Date();
//     let dzien = dzisiaj.getDate();
//     let miesiac = dzisiaj.getMonth() +1 ;
//     if (miesiac<10) miesiac = "0" +miesiac;
//     let rok = dzisiaj.getFullYear();
//     let godzina = dzisiaj.getHours();
//     if (godzina<10) godzina = "0"+godzina;
//     let minuta = dzisiaj.getMinutes();
//     if (minuta<10) minuta = "0"+minuta;
//     let sekunda = dzisiaj.getSeconds();
//     if (sekunda<10) sekunda = "0"+sekunda;

//     document.getElementById("zegar").innerHTML = dzien+"/"+miesiac+"/"+rok+" | "+godzina+":"+minuta+":"+sekunda;
//     setTimeout("drugiZegar()", 1000);
// }

// function dodawanieDoBazyDanych()
// {
//  let name = document.getElementById("name").value;
//  let jednostka = document.getElementById("jednostka").value;
//  let ilosc = document.getElementById("ilosc").value;
//  let zelaznyZapas = document.getElementById("zelaznyZapas").value;
//  let kategoria = document.getElementById("kategoria").value;

//  document.getElementById("dodanyProduct").innerHTML= "Do dodania: "+name+" w ilości "+ilosc+" szt.";

// }