*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***
Register With Valid Username And Password
    Click Register Link
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Register Credentials
    Page Should Contain  Welcome

Register With Too Short Username And Valid Password
    Click Register Link
    Set Username  ka
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Register Credentials
    Page Should Contain  Username or password invalid

Register With Valid Username And Invalid Password
    Click Register Link
    Set Username  kallee
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Submit Register Credentials
    Page Should Contain  Username or password invalid

Register With Nonmatching Password And Password Confirmation
    Click Register Link
    Set Username  kalleee
    Set Password  kalle456
    Set Password  kalle4567
    Submit Register Credentials
    Page Should Contain  Passwords not matching

Login After Successful Registration
    Click Register Link
    Set Username  kalleeee
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Register Credentials
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  kalleeee
    Set Password  kalle456
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Click Register Link
    Set Username  ka
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Register Credentials
    Click Link  Login
    Set Username  ka
    Set Password  kalle456
    Click Button  Login
    Page Should Contain  Invalid username or password

*** Keywords ***
Click Register Link
    Click Link  Register new user
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Register Credentials
    Click Button  Register


