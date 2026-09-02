result: main.o calculator.o
	g++ -o result main.o calculator.o
main.o: main.cpp calculator.h
	g++ -c main.cpp 
calculator.o: calculator.cpp calculator.h
	g++ -c calculator.cpp 
clean:
	rm *.o result 