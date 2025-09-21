CFLAGS = -g -Wno-unused-parameter
CC = gcc

PROGRAMS =  exo1 exo2 exo3

.PHONY: all clean

all : $(PROGRAMS)

exo1: Rendu3.o main_1.o
	$(CC) -o $@ $(CFLAGS) $^

exo2: Rendu3.o main_2.o 
	$(CC) -o $@ $(CFLAGS) $^

exo3: Rendu3.o main_3.o 
	$(CC) -o $@ $(CFLAGS) $^

Rendu3.o: Rendu3.o 
	$(CC) $(CFLAGS) -c Rendu3.c

main_1.o:
	$(CC) $(CFLAGS) -c main_1.c

main_2.o:
	$(CC) $(CFLAGS) -c main_2.c

main3.o:
	$(CC) $(CFLAGS) -c main_3.c 

clean:
	rm -f *.o *~ $(PROGRAMS)

