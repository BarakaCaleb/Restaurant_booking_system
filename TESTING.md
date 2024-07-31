# Project 4 -  Testing

Visit the deployed site: [Mama Jo's Booking Site](https://bookworm2022.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [Python Validator](#python-validator)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. I have checked the HTML via direct input and running the raw code through the validator.

* Base Template - No errors or warnings.
* Index Page - No errors or warnings.
* Contacts Page - no errors or warnings.
* Home Page - No errors or warnings.
* Edit Page - No errors or warnings.
* Bookings Page - No errors or warnings.

- - -

### Python Validator

[PEP8](https://pep8ci.herokuapp.com/#) was used to validate the python files. 

* views.py - No errors or warnings.
* models.py - No errors or warnings.
* forms.py - No errors or warnings.
* admin.py - No errors or warnings.
* urls.py - No errors or warnings.

- - -

## MANUAL TESTING

### Testing User Stories

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| `Client` |
|  |  |  |
| To be able to view the site on a range of device sizes. | Responsivity was implemented on all pages to endure the site remained perfectly clear on all devices. | :--- |
| To make it easy for potential customers to sign up to and make use of the site's services. | Access to sign up services or to log in is visible in the nav bar on all pages. Once the user has moved from the Home page to the Index Page, if they are not logged in they are informed that they need to do so to progress, and are directed to the service. | :--- |
| To allow people to be able to contact the Restaurant with questions or to report problems. | Users are always shown the Contacts link on the navbar regardless of their login status. | :--- |
|`New Customers`|
|  |  |  |
| I want to easily sign up to and make use of the site's services. | If a user is not logged into an account, a login/signup link is provided on the navbar at all times, and the Index page will direct them to use the same services. | :--- |
| I want to quickly and easily search for available tables. | Due to time constraints, this simpler version has not been implemented. | :--- |
| I want to be able to access other sites or socials linked to the Restuarant so as to learn more about them. | Due to time constraints, this was unable to be implemented in time, but the user can access the Contacts page and make use of its links to achieve the same goal. | :--- |
|`Returning Customers` |
|  |  |  |
| I want to be able to see, alter, or even cancel any existing bookings. | The Index page displays all Bookings the user has made, and can allow them to edit or delete them if they so wish. | :--- |
| I want to be able to specify all relevant details while booking in order to quickly book specific tables. | The Bookings page allows the user to sspecify the date, table, and time of their booking. | :--- |
| I want to be able to contact the Restaurant to report any problems that might occur. | Users are always shown the Contacts link on the navbar. | :--- |

- - -

### Full Testing

Full testing was performed on the Google Chrome browser.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Header and Navbar` |
|  |  |  |  |  |
| Mama Jo's Logo | When clicked the user will be redirected to the home page. | Clicked Logo and title | Redirected to the home page. | Pass |
| Home Page Link | When clicked the user will be redirected to the home page.| Clicked link | Redirected to the home page. | Pass |
| Contacts Link | When clicked the user will be redirected to the contacts page. | Clicked link | Redirected to the contacts page. | Pass |
| Log in Link (Only shown if user not in session) | When clicked the user will be redirected to the log in page. | Clicked link | Redirected to the log in page | Pass |
| Register Link (Only shown if user not in session) | When clicked the user will be redirected to the register page. | Clicked link | Redirected to the register page  | Pass |
| Log out Link (Logged in users only) | When clicked the user will be redirected to the log out page. | Clicked link |Redirected to the log out page. | Pass |
| `Home Page` |
|   |   |   |   |
| Link to index page in the welcoming paragraph | When clicked the user will be redirected to the index page. | Clicked link  | Redirected to the index page | Pass |
| `Log in Page` |
| Username input - empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required | Pass |
| Password input empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | tooltip tells me this field is required |  Pass |
| log in button | Saves the user to session and redirects to the profile page. Flash message shown welcoming the user | Submitted form | Redirected to the profile page and flash message shown | Pass |
| Incorrect username or password used | A flash message should display saying username/password incorrect - this is defensive programming - not letting user know which input is incorrect | Incorrect username/password entered | Message flashes to let the user know they have entered an incorrect username/password | Pass |
| Link to sign page |  This should redirect the user to the register page | Clicked link | Redirected to the register page | Pass |
| `Register Page` |
| | | | | | |
| Username input | The username should be 5 characters minimum | Entered username less than 5 characters long | tooltip lets the user know they have not entered enough characters | Pass |
| Username input - empty | The username is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| Username input | If username is in use, message should flash to user | entered an in use username | Message flashed to say username already in use | Pass|
| Email input | The email input should include an email address  | Entered plain text | Tooltip tells user to use an email address here | Pass |
| Email input - empty | The email is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| Password input | This field should be at least 8 characters long | Entered password less than 8 characters long | Tooltip tells user the password should be at least 8 characters long | Pass |
| Password input - empty | The password is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| Register button | Should redirect user to the log in page and a registration successful message flashed | Created new user and submitted form | Redirected to the log in page and message flashed | Pass |
| `Index Page` |
|   |   |   |   |  |
| Edit button | Should redirect the use to the edit page to edit the booking attached to it when pressed | Pressed the button | Was redirected to the edit page | Pass |
| Delete button | Should delete the associated booking when pressed | Pressed the button | The associated booking was deleted | Pass |
| New Booking button | Should redirect the user to the bookings page when pressed | Pressed the button | Redirected to the bookings page | Pass |
| `Bookings Page` |
|   |   |   |   |  |
| Add booking button (when booking has been taken) | When the user clicks this button the form entries they have made should be cleared and an alert should pop up informing them that their requested booking is already taken | Clicked button | Form entries cleared and alert popped up | Pass |
| Add booking button (when booking is available) | When the user clicks this button they should be redirected to the index page with their new booking added to the list of bookings | Clicked button | Redirected to the index page with the new booking added to the list | Pass |
| `Edit Page` |
|   |   |   |   |  |
| Update booking button (when new booking has been taken) | When the user clicks this button an alert should pop up informing them that their requested booking is already taken | Clicked button | Alert popped up | Pass |
| Add booking button (when booking is available) | When the user clicks this button they should be redirected to the index page with their old booking on the list of bookings replaced with the new one | Clicked button | Redirected to the index page with the new booking replacing the old one on the list | Pass |

 - - -

## BUGS

### Solved Bugs

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | When I tried to implement verification code to confirm that the booking the user wished to make was not already taken, it did not work, allowing the user to make repeat bookings for the same table at the same time on the same day. | I discovered that, although the value provided by the form could be fed into the Django provided code to correctly interact with the database without issue, the exact value provided when pulling the date from a database entry was in a different format, and so when I tried to compare the two to see if the date in question was taken, it would always say it wasn't, even if it was. To correct this issue, I simplified my verification system to instead filter the database for any entries that contained identical values to those submitted in all fields except the user, as that was not relevant, and to return a False value if any entries were found, preventing duplicate entries from occuring. |
| 2 | When I tried to deploy the Project to Heroku, it consistently refused to do so. | I discovered that the way Heroku deployment works means that I need to have a 'static' folder in the highest level. Once I realised this, I created an additional static folder, populated it with copies of other images to allow it to be commited, and then pushed it to Github, at which point my Project could be deployed. |
| 3 | When I tried to run my app from Heroku, it would crash, bringing up a ModuleNotFoundError every time. | I discovered that the missing 'module', 'django_todo', was not actually a module I had failed to install. Instead, when following guidance from a previous walkthrough project on how to deploy to Heroku, I mistakenly took it for such a module that was presumably installed when Django was installed. In actuallity, it was the name of the app made in the walkthrough project. Once I realised this, I merely had to change it to 'restaurant_booking_system' and it functioned completely normally. |

- - -