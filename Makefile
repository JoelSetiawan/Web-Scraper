# Make file should compile all the webscraper files and make sure that we can build in one step.
# ------------------------------------------------------------------------------------------------------------------------
# Variables for simplification, you can simply object files, and their prerequisites
cc = g++
cflags = -Wall -g
objects = webscraper.o 
# ------------------------------------------------------------------------------------------------------------------------
# Target for main program
webscraper: $(objects)
	cc -o webscraper $(objects)

# ------------------------------------------------------------------------------------------------------------------------
# Out Files
webscraper.o : webscraper.h

# ------------------------------------------------------------------------------------------------------------------------
# Phony allows us to do an action.
.PHONY : clean
clean : 
	rm webscraper $(objects)