# Final Status Report
### Project Title: Project Hulk

### Team Number: 2

### Team Name: Team Batman

### Team Members: 
<ul>
  <li>Adam McWilliams</li>
    <ul>
      <li>Email: admc1043@colorado.edu</li>
      <li>Git: adamjmcwilliams</li>
    </ul>
  <li>Nathan Palmer</li>
    <ul>
        <li>Email: napa8745@colorado.edu</li>
        <li>Git: natepalmer7</li>
    </ul>
  <li>Danielle Aras</li>
    <ul>
        <li>Email: daar8381@colorado.edu</li>
        <li>Git: daras-cu</li>
    </ul>
  <li>Minh Bui</li>
    <ul>
        <li>Email: mibu4178@colorado.edu</li>
        <li>Git: Minh-Thien-Bui</li>
    </ul>
  <li>Alex Cullen</li>
    <ul>
        <li>Email: alcu6962@colorado.edu</li>
        <li>Git: anonalyx</li>
    </ul>
  </ul>
### Links: 

Project Tracker: https://www.atlassian.com/software/jira

Video: https://www.youtube.com/watch?v=9Fo9Bau6Tl8

Version Control Repository: https://github.com/anonalyx/Hulk.git

Public Hosting Site: https://hulk-d5tf.onrender.com/

### Completed Work:
Our team created a platform for fitness enthusiasts to organize their workout routines. Users can choose a particular muscle group and equipment, and upon selection they will be presented with a curated list of calisthenic exercises designed for that specific area. With our app, users can effortlessly find new exercises to try and build comprehensive full-body workout plans.

### Implementation in Progress: 
We are working on implementing a calorie counter for each of the exercises in our database. Currently, the calorie calculator only works for the “Running” exercise. We’ve already written the backend code for a calorie calculator function that will return different estimates depending on the exercise passed to it. We are in the process of implementing the front end code to give the user the option of choosing an exercise, and getting a unique calorie estimation according to their selection.

### Plans for the Future:

In the future, our team plans to create a workout plan builder that will help athletes train like the One-Punch Man. We also hope to implement a mobile version of our app for users who want to use it from their phones. Our plan is to migrate the web based deployment of Project Hulk to Heroku. We will integrate the app with wearable fitness trackers for even further accessibility. Most importantly, our team plans to recruit famous athletes such as LeBron James, Tom Brady, and Kevin Durant as sponsors for Project Hulk.

### Known Bugs and Issues:

A current problem with the exercise search page is the “Body Weight” equipment category does not work. Due to this issue, the exercise search function cannot return “Squats” or “Sit-Ups” because those two exercises require “Body Weight” as their equipment. The “Back” and “Legs” body part categories do currently work, but they’re both useless since they utilize the “Body Weight” equipment. It’s likely that the cause of this glitch is the space character in the “Body Weight” string.

