1st Example
===========
* go to "http://automationpractice.com/index.php"

Account creation
----------------
* click hyperlink "Sign in"
* insert random address
* click button by id "SubmitCreate"
* wait until element is present by id "submitAccount"
* click button by id "id_gender1"
* insert text "John" by id "customer_firstname"
* insert text "Smith" by id "customer_lastname"
* insert text "passwd" by id "passwd"
* click button by id "uniform-days"
* select random value from dropdown by id "days"
* click button by id "uniform-months"
* select random value from dropdown by id "months"
* click button by id "uniform-years"
* select random value from dropdown by id "years"
* click button by id "uniform-newsletter"
* click button by id "uniform-optin"
* clear text by id "firstname"
* insert text "John" by id "firstname"
* clear text by id "lastname"
* insert text "Smith" by id "lastname"
* insert text "Company" by id "company"
* insert text "Primary address line" by id "address1"
* insert text "Secondary address line" by id "address2"
* insert text "Townsville" by id "city"
* click button by id "uniform-id_state"
* select random value from dropdown by id "id_state"
* insert text "01234" by id "postcode"
* click button by id "uniform-id_country"
* select random value from dropdown by id "id_country"
* insert text "Lorem ipsum dolor sit amet, consectetur adipiscing elit." by id "other"
* insert text "012345678" by id "phone"
* insert text "876543210" by id "phone_mobile"
* clear text by id "alias"
* insert text "Home" by id "alias"
* click button by id "submitAccount"
* wait until element is present by id "center_column"
* click element by xpath "//*[@id='center_column']/div/div[1]/ul/li[4]/a/span"
* check email address
* click hyperlink "Sign out"