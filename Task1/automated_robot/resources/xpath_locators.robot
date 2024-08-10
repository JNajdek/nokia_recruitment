*** Variables ***
${DENY_COOKIES_XPATH}   /html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[1]/div
${TEXT_FIELD_XPATH}     //*[@id="APjFqb"]
${SEARCH_BUTTON_XPATH}  /html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]
${WEB_ELEMENTS_XPATH}   //h3[contains(text(), 'Wikipedia')]
${WIKIPEDIA_SEARCH_RESULT_XPATH}   (//h3[contains(text(), 'Wikipedia')]/ancestor::a)[1]
${YEAR_FROM_WIKI_XPATH}    /html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[2]/tbody/tr[6]/td/p/a[2]
