# **S**kin**C**ared

![Preview](static/docs/rm-site-responsiveness.png)

[View Live Website Here](https://skincared.herokuapp.com/)

***
# Introduction

The beauty and cosmetics industry has been an ever growing market since its inception. Worldwide revenue from cosmetics alone were £825 million in 2022. The market is anticipated to grow at a rate of 6.85% each year through 2023 – 2026 showing how lucrative it can be. 

Skincare falls under the category of cosmetic products, which are specifically designed to care and protect the skin. This includes topicals such creams, serums, toners and sunscreen for the body and face; with the most popular products being Korean, Japanese & Western skincare. 

As a result of this demand SkinCared was born. SkinCared is a B2C E-commerce website, focussing in procurement and selling of skincare products from around the world. Specifically SkinCared specialises in Eastern & Western skincare which account for most of the overall market share. 

[Back To Top](#skincared)

# Table Of Contents

1. [Introduction](#introduction)
2. [Site Goals](#site-goals)
    * [Site Goals](#site-goals)
    * [User Goals](#user-goals)
3. [Development Planes](#development-planes)
   * [Strategy](#strategy)
        * [Ideal User](#ideal-user)
        * [Epics](#epics)
        * [User Stories](#user-stories)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
         * [Database Schema](#database-schema)

***
# Site Goals
## Site & User Goals 
### Site Goals
-	To deliver an ecommerce solution for the high demand in skincare products.
- To provide potential and existing consumers a ‘one stop shop’ in skincare, specifically Eastern & Western cosmetics
- To enable SkinCared and its employees to easily update and maintain the overall site and its content, especially the owner/manager
- To generate sales by providing the user an intuitive, hassle free experience in terms of finding, selecting and buying products
- Showcase & promote the wide variety of brands SkinCared houses in terms of their ethos and product selection 

### User  Goals
- Buy skincare products that suite their skins needs or find new ones that intrigue them 
- Learn about the different skin types and products that coincide with said skin type as to build an effective skincare routine 
- Have an seamless user experience in terms on finding, discovering and purchasing skincare products 

[Back To Top](#skincared)

***
# Development Planes 
## Strategy
SkinCared strategy for competing in the saturated skincare market is to provide the user with a singlar point of sale for Eastern & Western skincare products. This coupled with SkinCared ethos for teaching the customer about skincare and the brands it sells makes it unique within the market place. 

### Ideal User 
- Intrest in skincare weather be novice or expert 
- Have a current skincare issue and want a soltion 
- Want to learn more about general skincare or how to aid what is currently afflicting them 
- Someone looking to add to their skincare arsenal 
- Interested in Eastern or Western skincare

## Epics 
9 epics were created which were further developed into  9 User Stories and 47 tasks respectivley. For more details please check the project tab of this repository. 

1. [#12](https://github.com/FarisGJD/skincared/issues/12) Initial workspace setup for early deployment - As a developer, I can **create and setup my workspace in terms of files, folders, packages and applications**, so that I can deploy my workspace early.

2. [#14](https://github.com/FarisGJD/skincared/issues/14)Create home app & base tempalte - As a **user**, I can **check SkinCared's landing page**, so that **I can determine whether the site is suited to my needs and navigate accordingly.**


3. [#16](https://github.com/FarisGJD/skincared/issues/16) Create products (skincare) app - As a **user**, I can **view SkinCared products range**, so that **I can find an item that will fit my needs.**

4. [#18](https://github.com/FarisGJD/skincared/issues/18) Create bag app - As a **user**, I can **add items to my bag and keep them there**, so that **I can purchase now or later.**

5. [#20](https://github.com/FarisGJD/skincared/issues/20)
Create Create checkout app - As a **user**, I can **finalize the checkout process**, so that **I can complete my intended purchase.**

6. [#22](https://github.com/FarisGJD/skincared/issues/22)
Add Stripe, Stripe Elements & Stripe Webhooks functionality - As a **user**, I can **use a secure payment system such as Stripe**, so that **I can feel safe in handing over sensitive information.**

7. [#24](https://github.com/FarisGJD/skincared/issues/24)
Create profile app and customise allauth - As a **user**, I can **signup or login to my SkinCared account**, so that **I can update my personal details and look at my order history.**


8. [#25](https://github.com/FarisGJD/skincared/issues/25)
Add product management functionality - As a **site owner**, I can **manipulate the admin through the site**, so that **I have ease of use.**


9. [#28](https://github.com/FarisGJD/skincared/issues/28)
Add web marketing and seo - As a **site owner**, I can **user SEO and web marketing techniques**, so that **I can target my audience more effectively and precisely.**

## User Stories 
From the Epics 9 User Stories were created and 47 tasks respectively. All predicted tasks and stories were able to be completed as this is the first release of SkinCared and is to act as a minimal viable product with the core functionality in place to achieve said User Stories.

1. ### Initial workspace setup for early deployment 
    * [#13](https://github.com/FarisGJD/skincared/issues/13) As a **developer**, I can **I can setup Django and install the supporting libraries and packages I need**, so that **so I can start the development process.**

2. ### Create home app & base tempalte
    * [#15](https://github.com/FarisGJD/skincared/issues/15) As a **user**, I can **head to the site's landing page and use its navigation menu**so that **I can traverse the website in the hopes of buying something.** 

3. ### Create products (skincare) app
    * [#17](https://github.com/FarisGJD/skincared/issues/17) As a **user**, I can **checkout SkinCareds product lines as well as the brands that they house and more information about skincare**, so that **I can make an informed purchase.**

4. ### Create bag app
    * [#19](https://github.com/FarisGJD/skincared/issues/19) As a **user**, I can **manage and house the items I am interested in purchasing at one location**so that **I can continue to the checkout menu now or in the future.**

5. ### Create Create checkout app
    * [#21](https://github.com/FarisGJD/skincared/issues/21) As a **user**, I can **continue the purchase process from the bag to the checkout**, so that **I can purchase my items.**

6. ### Add Stripe, Stripe Elements & Stripe Webhooks functionality
    * [#23](https://github.com/FarisGJD/skincared/issues/23) As a **user**, I can **make a secure purchase with my card details**, so that **my sensitive information stays private and I can build trust with SkinCared.**

7. ### Create profile app and customise allauth
    *[#24](https://github.com/FarisGJD/skincared/issues/24)As a **user**, I can **signup or log in to an existing account**, so that **I can look at my historical purchases as well as update my contact info.**


8. ### Add product management functionality
    * [#26](https://github.com/FarisGJD/skincared/issues/26) As a **site owner**, I can **perform full CRUD functionality on the server side**, so that **I can manipulate the database easily.**

9. ### Add web marketing and seo
    * [#27](https://github.com/FarisGJD/skincared/issues/27)
    As a **site owner**, I can **include a signup form building my list of contacts and add descriptive meta tags**, so that **I can directly communicate with my consumers and achieve higher rankings in search results.**

[Back To Top](#skincared)

***
# Scope
## Planned Functionality 
* Skincare Products – View full list of the sites products as well as a detailed look at the product when clicked on 

* Product Search – By product type, usage and a search bar that takes extensive search critera such as brand name or ingredient 

* Brands - Look up information about the brands SkinCared hosts, what they are about and their ethos 

* Shopping Bag - A bag where the user can add the items they want to or intend to purchase, as well as upadte or delete them

* Chekout - Securley takes the users delivery and payment information as well as option to save the users delivery details 

* Checkout Success - Informs the user of successful payment and confirms order as well as sends confirmation email

* User Profile - Houses the users information as well as historical orders. User can Create, Read, Update & Delete thier info 

* Login & Singup - Users can create an account, login, logout and signup to a SkinCared account

* Product Management - Site owner can add, update and delete products from the server side 

* Authentication – Different levels of functionality for customer compared to an admin 

* Newsletter Signup Form - The use of a newsletter signup form so that the user can be emailed about promotions 

* Contact Details & Social Media - 

* Feedback - Pop up window with appropriate message for when the user is performing an action on the site 

* Account Recovery - Users can reset their password, email address and delivery address 

[Back To Top](#skincared)

***
# Structure
Since the website uses the Django programming language, the site has an MVC (model, view, template) structure and uses object relational mapping to convert data between the relational databases present. Therefore, the site is divided into apps which then contain the html pages. This makes the structure extreemly inuit

## Main Template 
1. base.html - One of the main 'pages' which holds the header, navbar and footer and newsletter signup form 

## Home App 
2. index.html - Landing page which immediately informs the user what the website is about and its offerings

## Skincare App 
3. all-products.html - Contains a list of all the sites products and when clicked on leads to the products-details.html

4. products-details.html - Contains a detailed view of the product, the brand it comes from and important information such as weather the product is vegan or cruelty free. Furthermore allows the user to add a product to their bag or the admin to update and delete a product 

5. add-products.html - A UI element on the server side that allows the admin to add a product without accessing the admin

6. edit-products.html - A UI element on the server side that allows the admin to edit a product without accessing the admin 

7. brands.html - A page that shows a full list of brand names which when clicked on take you to the full-brands.html page 

8. full-brands.html - Contains detailed information about the brands that are hosted on SkinCared and will contain future functionality that allows user to filter products by brands

9. skin-type.html - Showcases the different skin types and what products would suite said skin type. Again this will have future filtering functionality 

## Bag App 

10. bag.html - A page where the user can store, update and delete current or future purchases ready for the checkout 

## Checkout App 

11. checkout.html -  A page where the user can securely enter the personal and card details as well as the option to save personal details to the profile page 

12. checkout-success.html - A page that appears after the checkout process is complete and confirms to the user the status of the order as well as sends out confirmation emails 


## Profile App 
13. profile.html - A page where the user can find, edit and update their personal information as well as look at thier historical purchases 

## Skincared App 
14. 404.html - A page that pops up when there is a 404 error

[Back To Top](#skincared)
***
# Skeleton
Mock-ups from similar/competitor E-commerce websites were procured to inform the layout of SkinCared. Typically wireframes would be created but I did not have access to Balsamiq as my subscription expired. Each page mentioned in the mock-ups achieves the goals set out and defined in the structure plane 

### Home Page Mockup 
![Preview](static/docs/home-page-mockup.png)


#### Full Products Mockup 
![Preview](static/docs/full-products-mockup.png)

### Product Details Mockup 
![Preview](static/docs/product-details-mockup.png)
![Preview](static/docs/product-detail-mockup-2.png)

### Full Brands Mockup 
![Preview](static/docs/full-brands-mockup.png)

### Brand Details Mockup 
![Preview](static/docs/brand-details-mockup.png)

### Skin Type Mockup 
![Preview](static/docs/skin-type-mockup.png)

### Bag Mockup 
![Preview](static/docs/bag-mockup.png)

### Secure Checkout Mockup 
![Preview](static/docs/secure-checkout-mockup.png)
![Preview](static/docs/secure-checkout-mockup-2.png)

### Secure Checkout Success Mockup 
![Preview](static/docs/secure-checkout-success-mockup.png)

### User Profile Mockup 
![Preview](static/docs/user-profile-mockup.png)

## Database Schema
Since SkinCared is an site that sells skincare products, several relational custom models were used as it was deemed the easiest way to filter through products and map relationships between objects such as a Brands and their Skincare products. In total there are 5 custom models. Due to time constraints only 4 were used. The ones that haven’t been used were purposely left in the code for future releases. 

### Brand 
    - Rows:
            * name - programmatic brand name 
            * freindly_name - friendly brand name 
            * character_identifier - a single letter (e.g. e) used to identify the brand and separate them accordingly 
            * about - description about the brand 
            * image - container the banner image of the brand 
            * slug - used in url's to make them easier to read, but also to     make them more search engine friendly


### Skin Type 
    - Rows:
            * type - name of skin type 
            * description - summary about the skin type containing useful information and suggestions of what product to buy if your skin coincides with said type 
            * image - container a banner image for the specific skin type 
            * slug - used in url's to make them easier to read, but also to     make them more search engine friendly


### Product Type 
    - Rows:
            * name - programmatic product type name 
            * freindly_name - friendly product type name 
            * about - summary about the different product types containing useful information 
            * image - product type banner image 


### Skincare 
    - Rows:
            * brand - has a foreign key relationship with the Brands model
            * about - summary about the brand that the product pertains to 
            * name - name of the product 
            * usage - area of face or body product to be used on 
            * quantity - the size (e.g. ml)
            * price - price of product
            * image - product image 
            * description - summary of what the product is and dose
            * directions - directions on how to use the product 
            * ingredients - full product ingredients list 
            * product_type - has a foreign key relationship with the Product Type model 
            * product_subtype - further details about the product type, programattic name  
            * product_subtype_friendly_name - further details about the product type, friendly name  
            * star_ingredient - list of star ingredient will be used for filtering in future releases 
            * skin_type - many to many relationship with skin type model since one product can be used for many different skin types. Will be used for filtering in future releases 
            * skin_concern - many to many relationship with skin concern model since one product can be used for many skin conc erns. Will be used for filtering in future releases 
            * cruelty_free - cruelty free status 
            * vegan - vegan status 
            * alcohol_free - alchol free status 
            * fragrance_free - fragrance free status 
            * sku - unqiue product number 
            * rating - product rating, will be used in future releases
            
### Skin Concern 
    - Rows:
        * concern - programmatic skin concern name 
        * concern_freindly_name - friendly skin concern name 
        * description - summary about the different types of skin concern containing useful information 
        * image - skin concern banner image 











