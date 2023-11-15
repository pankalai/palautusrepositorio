*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input New Command And Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command And Input Credentials  ka  kalle123
    Output Should Contain  Username or password invalid

Register With Enough Long But Invalid Username And Valid Password
    Input New Command And Input Credentials  ka222  kalle123
    Output Should Contain  Username or password invalid

Register With Valid Username And Too Short Password
    Input New Command And Input Credentials  kalle  kalle1
    Output Should Contain  Username or password invalid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Input Credentials  kalle  kalleeeee
    Output Should Contain  Username or password invalid


*** Keywords ***
Input New Command And Input Credentials
    [Arguments]  ${username}  ${password}
    Input New Command
    Input Credentials  ${username}  ${password}
    