# Work Progress Log

    October 25, 2021
    I am still learning how the libraries needed to make Web Scraping
    possible work and more information about how networking works.

    If I want to convert ASCII-related text, then I can use libcurl -> libtidy ->
    libxml to more easily convert the ASCII-related text into something human inter-
    pretable. However, I am also thinking of applications related to other languages
    that may use Unicode Format, so I also installed the ICU library that 
    transfers unicode format data.

    Tomorrow, let's continue reading the documentation for libcurl.
    Continue reading the examples, and then formulate a plan for making 
    a barebones functional piece of documentation.

    November 23, 2021
    For Thanksgiving break, I can focus on learning web scraping in python.
    I have decided to create this web scraper in Python since it's easier to 
    start creating projects with Python

    I'm reading through the Web Scraping book by O-Reilly, and learned
    about how web server requests work. The book used the example of Bob, a PC user who is
    requesting data from Alice, a web server owner. Bob sends a request as a bit stream that is packaged
    by his computer. This bitstream has a header that stores his PC's IP address and Alice's web server IP address,
    and a body that contains his request. This information is packaged and sent to a local router, where it will
    stop by many points along the way to find a path to Alice's web server. The specifics of why it stops by many points
    is an interesting problem as well, which connects to graph theory too.

