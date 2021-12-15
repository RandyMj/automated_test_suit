# Automated Test Suit/ Test Plan and HTML Report

Simple automated test plan in [Python](https://www.python.org) with [Selenium](https://www.selenium.dev/) framework using HtmlTestRunner for reporting the outputs of the test. We use 3 pages to test some things like sending keys to a search box, scrolling down a page and clicking links and buttons.

## Features

- First test is opening [Google](https://www.google.com) find the search box, clear it and send "selenium" keys, then find the first link by the xpath and click it.
- Second test is opening [WeSchools](https://www.w3schools.com) find a link by it link name ands click it.
- Third test is opening [Amazon](https://www.amazon.com) send keys into the search box and scrolling down the page to the end.

> Note: `Time` module is to make the automation to wait for the page to load (this is not the optimal way to do it).