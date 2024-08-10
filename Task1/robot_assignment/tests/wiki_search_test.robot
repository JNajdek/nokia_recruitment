*** Settings ***
Library    SeleniumLibrary
# including external files with variable definitions
Resource   ../resources/variables.robot
Resource   ../resources/xpath_locators.robot
Test Setup    Start TestCase
Test Teardown    Finish TestCase
*** Test Cases ***
Search For Nokia Wikipedia


    # clicks to close the cookies window using xpath to locate the deny button
    Click Element    xpath= ${deny_cookies_xpath}

    # types 'nokia wikipedia'  into browser search field
    Input Text    xpath= ${text_field_xpath}     ${SEARCH_TERM}

    # clicks search on google button
    Click Element    xpath= ${search_button_xpath}

    # retrieves list of web elements (searches) containing 'Wikipedia'
    ${elements}=    Get WebElements    xpath= ${web_elements_xpath}
    Log    ${elements}
    # error handling for the lack of Wikipedia links in search results
    Run Keyword If    '${elements}' == '[]'    Fail    "Wikipedia link not found in search results"
    Should Not Be Empty    ${elements}

    # clicks on the first search result
    Click Element    xpath= ${wikipedia_search_result_xpath}
    # captures a screenshot of the entire page
    Capture Page Screenshot     ${SCREENSHOT_FILE}
    # extracts the title an tests if it contains Nokia
    ${title}=    Get Title
    Should Contain    ${title}    Nokia
    Log    ${title}

    # extracts the founding year using xpath as a locator
    ${year_from_wiki}=    Get Text    xpath=${year_from_wiki_xpath}
    # tests if it's equal to a expected variable
    Should Be Equal    ${year_from_wiki}    ${EXPECTED_YEAR}
    Log    ${year_from_wiki}


*** Keywords ***
# This keyword sets up the test
Start TestCase

    Log    Setup action
    #sets a global timeout of 30 seconds for all Selenium operations
    Set Selenium Timeout    ${TIMEOUT}
    # opens firefox browser and connects to google homepage
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
# This keyword cleans up after the test
Finish TestCase
    Close All Browsers
    Log    Teardown action