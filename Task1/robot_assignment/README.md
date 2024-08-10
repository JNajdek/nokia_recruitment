# Robot Framework Test Automation Task 

The project automates a Google search for "nokia wikipedia," verifies and interacts with the Wikipedia page and extracts data from it 

# Installation 

1. Copy repository using: git clone https://github.com/JNajdek/nokia_recruitment.git inside the terminal
2. Change directory to '.\nokia_recruitment\Task1\robot_assignment' and open .wiki_search_test.robot file in IDE of your choice
3. Install pytest dependencies by typing: 'pip install -r requirements.txt' inside your IDE terminal
4. Run test by typing: 'robot --outputdir ../robot_assignment/output tests/wiki_search_test.robot'


# Requirements 

- Python 3.11
- Robot Framework 6.0.1
SeleniumLibrary 6.1.0
- Firefox browser (latest stable version)
- geckodriver (compatible with the installed Firefox version)

#Project architecture

Variables are defined in .\robot_assignment\resources directory
Logs, report, screenshots if test is done correctly should be in .\robot_assignment\output directory 