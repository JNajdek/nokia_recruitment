*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.robot
Resource   ../resources/xpath_locators.robot
Test Setup    Start TestCase
Test Teardown    Finish TestCase
*** Test Cases ***
Search For Nokia Wikipedia



    Click Element    xpath= ${deny_cookies_xpath}

    Input Text    xpath= ${text_field_xpath}     ${SEARCH_TERM}

    Click Element    xpath= ${search_button_xpath}

    ${elements}=    Get WebElements    xpath= ${web_elements_xpath}
    Log    ${elements}
    Run Keyword If    '${elements}' == '[]'    Fail    "Wikipedia link not found in search results"
    Should Not Be Empty    ${elements}

    Click Element    xpath= ${wikipedia_search_result_xpath}
    Capture Page Screenshot     ${SCREENSHOT_FILE}
    ${title}=    Get Title
    Should Contain    ${title}    Nokia
    Log    ${title}

    ${year_from_wiki}=    Get Text    xpath=${year_from_wiki_xpath}
    Should Be Equal    ${year_from_wiki}    ${EXPECTED_YEAR}
    Log    ${year_from_wiki}


*** Keywords ***
Start TestCase
    Log    Setup action
    Set Selenium Timeout    ${TIMEOUT}
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
Finish TestCase
    Close All Browsers
    Log    Teardown action