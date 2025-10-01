# assessment-twitch-selenium-pytest

A GIF and a .mp4 recoeding showing the test running locally is added in the project framework with names: selenium_test.gif and selenium_recording.mp4
Test can be run using 'make report' command from the project root folder
An allure report is generated after test run which will automatically run in the browser once the test completes. A screenshot is attached to the report if in case test fails.
Screenshot of one streamer will be generated in screenshots folder.

Test Case flow: 
 a) Open twitch.tv
 b) Click in the search box and enter 'StarCraft II'
 c) Click on search icon
 d) Scroll down the page twice 
 e) Click on the video stream 
 d) Take the screenshot:
   i) Of the video streamer page with video playing
   ii) or the subscribe to watch video page

