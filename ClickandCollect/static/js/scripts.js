/*!
* Start Bootstrap - Shop Item v5.0.6 (https://startbootstrap.com/template/shop-item)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-item/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
// 

  function showLogin() {
    document.getElementById("login-form").style.display = "block";
    document.getElementById("register-form").style.display = "none";

    document.getElementById("title-login").classList.remove("text-secondary");
    document.getElementById("title-login").classList.add("text-dark");

    document.getElementById("title-register").classList.remove("text-dark");
    document.getElementById("title-register").classList.add("text-secondary");
}

function showRegister() {
    document.getElementById("login-form").style.display = "none";
    document.getElementById("register-form").style.display = "block";

    document.getElementById("title-register").classList.remove("text-secondary");
    document.getElementById("title-register").classList.add("text-dark");

    document.getElementById("title-login").classList.remove("text-dark");
    document.getElementById("title-login").classList.add("text-secondary");
}