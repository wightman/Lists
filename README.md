## Welcome to Lists
This is an effort to capture a reasonable body of knowledge (technologies, frameworks, practices) for generating a restful webAPI/webservice. With time I'm hoping to deliver a browser client app as well as Android app. Hopefully this serves as a suitable model for aspiring web developers, both backend and frontend(s).

The project is intended to portray a reasonable expectation for student projects in an undergraduate university course in [programming on the web](http://www.unb.ca/academics/calendar/undergraduate/current/frederictoncourses/informationsystems/info-3103.html) or an [introduction to mobile application development](http://www.unb.ca/academics/calendar/undergraduate/current/frederictoncourses/computer-science/cs-2063.html).

You can safely assume that at any point in time this project is broken, cannot be trusted and will never put gas in the car after borrowing it - _you have been warned._ Having said that,
you're welcome to use it as the basis for your own broken or fabulously-working project. If it's the fabulously-working variety, I'd love some credit :)

## What's In Here

Building on what's gone before, this is a YATDL (**Y** et **A** nother **T** o **D** o **L** ist) application. As you're well aware, the web needs at least one more of these. Or at least one with all the parts, together.

The project has some less than perfect requirements:
+ You need to create the database tables and stored procedures. The initial user will need to be added by hand.
+ Because it's an educational experience it uses the Flask builtin webserver.

### Technologies
+ The server is made in python3 + restful-flask, communicating in json.
+ The database is mySQL. This may (should?) change to MariaDB. All DB interaction is through stored procedures.
+ The api is modeled using raml.

### Other Notes
+ Each major division _should_ have a README.md within it, outlining its own details.
