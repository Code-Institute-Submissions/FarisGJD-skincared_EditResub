// User Profile Dropdown 
const userProfileIcon = document.querySelectorAll('.profile-icon');
const userProfileDropDown = document.querySelectorAll('.user-profile-drop-down-menu');

for (let i = 0; i < userProfileIcon.length; i++) {
    userProfileIcon[i].addEventListener("click", function() {
        for (let i = 0; i < userProfileDropDown.length; i++) {
            userProfileDropDown[i].classList.toggle("profile-active");
        }
    })
}

// Main Navigation

const navButtonSkin = document.querySelectorAll(".js-nav-button-skincare");
const navDropDownSkin = document.querySelector(".skincare-container");

for (let i = 0; i < navButtonSkin.length; i++) {
    navButtonSkin[i].addEventListener("mousemove", () => {
        navDropDownSkin.classList.add("main-nav-js");
    })
}

window.addEventListener("mouseout", () => {
    navDropDownSkin.classList.remove("main-nav-js");
})

const navButtonBrand = document.querySelectorAll(".js-nav-button-brands");
const navDropDownBrand = document.querySelector(".brands-container");

for (let i = 0; i < navButtonBrand.length; i++) {
    navButtonBrand[i].addEventListener("mousemove", () => {
        navDropDownBrand.classList.add("main-nav-js");
    })
}

window.addEventListener("mouseout", () => {
    navDropDownBrand.classList.remove("main-nav-js");
})


const navButtonSkinType = document.querySelectorAll(".js-nav-button-skin-type");
const navDropDownSkinType = document.querySelector(".skin-type-container");

for (let i = 0; i < navButtonSkinType.length; i++) {
    navButtonSkinType[i].addEventListener("mousemove", () => {
        navDropDownSkinType.classList.add("main-nav-js");
    })
}

window.addEventListener("mouseout", () => {
    navDropDownSkinType.classList.remove("main-nav-js");
})

const navButtonSkinConcern = document.querySelectorAll(".js-nav-button-skin-concern");
const navDropDownSkinConcern = document.querySelector(".skin-concern-container");

for (let i = 0; i < navButtonSkinConcern.length; i++) {
    navButtonSkinConcern[i].addEventListener("mousemove", () => {
        navDropDownSkinConcern.classList.add("main-nav-js");
    })
}

window.addEventListener("mouseout", () => {
    navDropDownSkinConcern.classList.remove("main-nav-js");
})


// Mobile Navigation Dropdown 
const hamburger = document.querySelector(".burger-menu");
const navMenu = document.querySelector(".mobile-navigation-container");

hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("mobile-nav-active");
})

// Mobile Serach Bar Dropdown 
const searchIcon = document.querySelector(".search-bar-mobile");
const search = document.querySelector(".mobile-serach-bar-container");

searchIcon.addEventListener("click", () => {
    search.classList.toggle("search-active");
})

// Signup Form 

const signupFormButton = document.querySelector(".signup-form-button");
const signupForm = document.querySelector(".signup-form");

signupFormButton.addEventListener("click", () => {
    signupForm.classList.toggle("signup-form-active");
})